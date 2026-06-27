from __future__ import annotations

import argparse
import multiprocessing
from pathlib import Path

from citation_map import generate_citation_map


DEFAULT_SCHOLAR_ID = "Tb3rc34AAAAJ"
REPO_ROOT = Path(__file__).resolve().parents[2]
FILES_DIR = REPO_ROOT / "files"
CACHE_DIR = Path(__file__).resolve().parent / "cache"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a static citation map HTML page and CSV."
    )
    parser.add_argument(
        "--scholar-id",
        default=DEFAULT_SCHOLAR_ID,
        help="Google Scholar user id. Defaults to Tianqing Fang's profile.",
    )
    parser.add_argument(
        "--parse-csv",
        action="store_true",
        help="Reuse and re-parse files/citation_info.csv instead of crawling Scholar.",
    )
    parser.add_argument(
        "--conservative",
        action="store_true",
        help="Use conservative affiliation matching for better precision.",
    )
    parser.add_argument(
        "--num-processes",
        type=int,
        default=4,
        help="Worker processes for affiliation matching.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    multiprocessing.freeze_support()
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    generate_citation_map(
        scholar_id=args.scholar_id,
        output_path=str(FILES_DIR / "citation_map.html"),
        csv_output_path=str(FILES_DIR / "citation_info.csv"),
        parse_csv=args.parse_csv,
        cache_folder=str(CACHE_DIR),
        affiliation_conservative=args.conservative,
        num_processes=args.num_processes,
    )


if __name__ == "__main__":
    main()
