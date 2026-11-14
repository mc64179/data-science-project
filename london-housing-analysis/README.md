# London Housing Prices and Crime Patterns

## Research question

How do average housing prices and recorded crime counts vary across years and areas in the supplied London housing dataset?

## What the analysis does

The notebook converts dates, derives year and month fields, compares yearly price extremes, summarizes crime counts by area, and identifies areas with lower-priced records.

## Main limitation

The results describe patterns in the supplied exercise data but do not establish that crime causes housing prices or that the data represent every London transaction.

## Files

- [`analysis.ipynb`](analysis.ipynb)
- [`data/`](data/) contains the supplied CSV dataset.
- [`figures/yearly-price-range.svg`](figures/yearly-price-range.svg) is a line chart of yearly England price ranges.
- [`figures/crime-by-area.svg`](figures/crime-by-area.svg) is a labelled bar chart of maximum recorded crime counts by area.
- [`figures/`](figures/) also contains notebook evidence images.

## Reproduce the analysis

From this project folder, create a Python 3 environment and install the root dependencies with `pip install -r ../requirements.txt`. Open the notebook with Jupyter and run the cells in order. The notebook uses the relative `data/` path, so it does not depend on the original computer's folders.

## Data source and sharing note

The CSV files are the datasets supplied with the CISC7204 Suggested Exercise 05 materials. Each project retains the original exercise filename and records the transformation performed in the notebook. Before publishing, verify the original provider and redistribution terms for each file and add the required attribution. No passwords, API keys, or private records are included.
