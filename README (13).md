# COVID-19 Regional Case Summary

## Research question

How do confirmed, death, and recovered case counts differ across regions in the supplied COVID-19 snapshot?

## What the analysis does

The notebook filters low-count records, compares regional totals, identifies maximum and minimum values, and examines India records through the supplied date.

## Main limitation

The data are a historical snapshot and reporting differences, timing, and changing definitions limit comparisons across regions.

## Files

- [`analysis.ipynb`](analysis.ipynb)
- [`data/`](data/) contains the supplied CSV dataset.
- [`figures/`](figures/) contains selected readable result images.

## Reproduce the analysis

From this project folder, create a Python 3 environment and install the root dependencies with `pip install -r ../requirements.txt`. Open the notebook with Jupyter and run the cells in order. The notebook uses the relative `data/` path, so it does not depend on the original computer's folders.

## Data source and sharing note

The CSV files are the datasets supplied with the CISC7204 Suggested Exercise 05 materials. Each project retains the original exercise filename and records the transformation performed in the notebook. Before publishing, verify the original provider and redistribution terms for each file and add the required attribution. No passwords, API keys, or private records are included.
