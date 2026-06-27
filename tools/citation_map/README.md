## Citation Map

This site uses the `CitationMap` project from <https://github.com/ChenLiu-1996/CitationMap>
to generate a static HTML citation map.

### Generate the map locally

```bash
python3 -m venv .venv-citation-map
source .venv-citation-map/bin/activate
pip install -r tools/citation_map/requirements.txt
python tools/citation_map/update_citation_map.py
```

Outputs:

- `files/citation_map.html`
- `files/citation_info.csv`

Notes:

- `CitationMap` currently relies on a local Chrome session and may trigger a Google
  Scholar CAPTCHA popup during crawling.
- If you manually clean `files/citation_info.csv`, rerun with `--parse-csv` to rebuild
  the HTML from the edited CSV without crawling Scholar again.
