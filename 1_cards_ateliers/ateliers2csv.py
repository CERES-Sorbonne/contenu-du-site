from datetime import datetime
from pathlib import Path
from typing import Dict

import frontmatter
import polars as pl

mds = list(Path.cwd().rglob("*/*.md"))
fields_to_keep = ["title", "tags", "author", "uuid"]

def get_md_fields(md_path: Path) -> dict:
    with open(md_path, 'r') as f:
        md = frontmatter.load(f)
    return {k: md[k] for k in fields_to_keep if k in md.keys()}

def get_date(md_path: Path) -> Dict[str, str | int]:
    date = md_path.parent.name.split('_')[0]
    date = datetime.strptime(date, '%Y-%m-%d')
    return {
        'date': date.strftime('%Y-%m-%d'),
        'year': date.year,
        'month': date.month,
        'day': date.day
    }

def lst_to_str(lst: list) -> str:
    return ' | '.join(lst)

all_ateliers = []
for md in mds:
    all_ateliers.append({**get_md_fields(md), **get_date(md)})

df = pl.DataFrame(all_ateliers)
df.write_ndjson("ateliers.jsonl")

df = df.with_columns(
    pl.col("tags").map_elements(lst_to_str, return_dtype=pl.String).alias("tags"),
)

df.write_csv("ateliers.csv")
