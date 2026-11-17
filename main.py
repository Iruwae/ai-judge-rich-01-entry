# ai-judge-rich-01 entry (Python 3.13, standard library only): writes one fixed
# plan - the plan an AI agent would follow to turn $100, a computer with internet
# access and 30 days into the most money - to /output/entry.txt. The gate takes
# UTF-8 text of 1 to 1,000 characters that is not only white space, and the judge
# reads exactly the bytes written, line ends included, so write no line end you do
# not mean to show. The program runs twice with no network, and both runs must
# write the same bytes.
#
# Put this file at the root of your repository as main.py, with no main.ts beside
# it: a repository with both at its root is refused.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = 'Day 1: buy a domain and publish a one-page site: messy spreadsheets cleaned and enriched, $39 flat, delivered in 24 hours, first 100 rows free, paid by card link. No calls, no meetings.\nDays 2-5: answer 30 spreadsheet-help posts a day on X, Reddit r/excel and Indie Hackers, offering the free 100 rows; each sample is done by code in minutes.\nDays 6-30: run every paid job with the same script - dedupe, fill gaps from public sources, format - and ask each buyer for a one-line review to post on the site.\nSpend $40 of the $100 on the domain, hosting and API calls; keep $60 in reserve; drop any channel with no paying buyer after five days.\nFirst paid job lands around day 6; after that about one a day is realistic, roughly $500-$700 by day 30 after costs. Nothing here needs luck, a meeting, or a skill I do not have - the work is code, the sample sells it, and the price is fixed.'

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
