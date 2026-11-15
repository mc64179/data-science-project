# London Housing Prices and Crime Patterns

## Research question

How do housing prices change over time in the England aggregate series, and how do recorded crime counts and lower-price records vary across London boroughs in the supplied housing dataset?

## Key findings

- England's maximum monthly average price rose from **£53,901 in 1995** to **£250,410 in 2019**. The 2020 value is **£247,355**, based on one month only.
- Maximum monthly recorded crime counts were **Westminster (7,461)**, **Lambeth (4,701)**, and **Camden (4,558)**.
- **104 zero-crime records** all came from **City of London** between 2001 and 2010; its maximum was 10 and minimum was 0.
- Records below £100,000 were most frequent in **Barking and Dagenham (85)**, **Newham (72)**, and **Bexley/Waltham Forest (64 each)**.

## Files

- [`analysis.ipynb`](analysis.ipynb) contains the exercise steps and the final reproducible plotting section.
- [`plot_london_housing.py`](plot_london_housing.py) regenerates the three figures from the CSV.
- [`data/5. London Housing Data.csv`](data/5.%20London%20Housing%20Data.csv) is the supplied exercise copy.
- [`figures/yearly-price-range.svg`](figures/yearly-price-range.svg) shows England monthly price extrema by year.
- [`figures/crime-by-borough.svg`](figures/crime-by-borough.svg) shows maximum monthly crime counts for London boroughs only.
- [`figures/low-price-records.svg`](figures/low-price-records.svg) shows counts of borough-month records below £100,000.

## Reproduce the analysis

From the repository root, install the pinned dependencies with `pip install -r requirements.txt`, then open this notebook. If running from this folder, use `pip install -r ../requirements.txt`. The notebook and script use the relative `data/` path and do not depend on a local computer folder.

## Data source and sharing note

The CSV is a course-provided exercise copy appears to correspond to the public Kaggle dataset [London Housing Data](https://www.kaggle.com/datasets/rohitgrewal/london-housing-data). The supplied file contains no licence or attribution statement, so this repository does not claim an open licence. Confirm the original provider's redistribution and attribution terms before reusing the raw CSV. No passwords, API keys, or private records are included.

## Limitation

The data are descriptive exercise records. The file includes aggregate rows such as England and Inner London as well as borough rows; the borough charts explicitly exclude aggregate rows. The results do not establish that crime causes housing prices or represent every London transaction.

## Feedback and Responsible Sharing

Liu Yuechi (MC640935) asked for concrete numerical findings rather than a methods-only description. This revision reports the values above and connects them to reproducible, labelled charts. The broader technical review is recorded as implementation work and is not attributed to Liu.
