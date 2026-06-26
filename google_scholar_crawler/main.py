from datetime import datetime
import json
import os

from scholarly import scholarly


author = scholarly.search_author_id(os.environ["GOOGLE_SCHOLAR_ID"])
scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
author["updated"] = str(datetime.now())
author["publications"] = {
    item["author_pub_id"]: item for item in author["publications"]
}

os.makedirs("results", exist_ok=True)

with open("results/gs_data.json", "w") as outfile:
    json.dump(author, outfile, ensure_ascii=False)

with open("results/gs_data_shieldsio.json", "w") as outfile:
    json.dump(
        {
            "schemaVersion": 1,
            "label": "citations",
            "message": f"{author['citedby']}",
        },
        outfile,
        ensure_ascii=False,
    )
