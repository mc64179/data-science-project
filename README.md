# CISC7204 Data Science Project Collection

**Course:** CISC7204 Data Science and Data Visualization  
**Status:** Completed semester collection

This public repository documents my semester work in data cleaning, exploratory analysis, visual communication, interactive graphics, geospatial methods, and statistical reasoning. Assignment 01, Assignment 02, and Midterm materials remain separate.

## Featured project: London Housing Prices and Crime Patterns

**Research question:** How do housing prices change over time in the England aggregate series, and how do recorded crime counts and lower-price records vary across London boroughs in the supplied housing dataset?

The analysis converts dates, derives year and month fields, filters London boroughs explicitly for borough comparisons, and creates the figures with reproducible Python code. England's maximum monthly average price rose from **£53,901 in 1995** to **£250,410 in 2019**; the 2020 value is **£247,355** from one month only. Westminster had the highest maximum monthly crime count (**7,461**), followed by Lambeth (**4,701**) and Camden (**4,558**). There were **104 zero-crime records**, all from City of London between 2001 and 2010. Records below £100,000 were most frequent in Barking and Dagenham (**85**), Newham (**72**), and Bexley/Waltham Forest (**64 each**).

![Yearly housing prices](london-housing-analysis/figures/yearly-price-range.svg)

![Crime by borough](london-housing-analysis/figures/crime-by-borough.svg)

## Project collection

| Project | Research focus |
|---|---|
| [London Housing Analysis](london-housing-analysis/README.md) | Housing prices and London borough crime patterns |
| [Police Data Analysis](police-data-analysis/README.md) | Violations, searches, stop duration, and age distributions |
| [Weather Analysis](weather-analysis/README.md) | Weather conditions and grouped measurement summaries |
| [Cars Data Analysis](cars-analysis/README.md) | Vehicle origins, weight, and fuel economy |
| [COVID-19 Analysis](covid-19-analysis/README.md) | Regional confirmed, death, and recovered cases |

## Course learning areas

- [Visualization basics](visualization-basics/README.md)
- [Advanced visualization](advanced-visualization/README.md)
- [Geospatial visualization](geospatial-visualization/README.md)
- [Interactive visualization](interactive-visualization/README.md)
- [Statistical reasoning](statistical-reasoning/README.md)

## Reproduce the featured analysis

From the repository root:

```text
python -m venv .venv
# activate .venv, then:
pip install -r requirements.txt
jupyter notebook london-housing-analysis/analysis.ipynb
```

Run the notebook cells in order. The final plotting section writes the three SVG figures in `london-housing-analysis/figures/`. The standalone `plot_london_housing.py` script performs the same plotting calculations.

## Data sources and responsible sharing

The CSV files are course-provided exercise copies. The London Housing file matches the public Kaggle dataset identified as [London Housing Data](https://www.kaggle.com/datasets/rohitgrewal/london-housing-data), but the course copy does not include a machine-readable licence or attribution statement. The original provider and redistribution terms for the Police, Weather, Cars, and COVID files were not included in the supplied materials. I therefore retain the source note, do not claim an open licence, and include no passwords, API keys, or private records. Anyone redistributing the raw CSV files should confirm the original provider's permission and attribution requirements first.

## Feedback and improvement

Liu Yuechi (MC640935) asked for concrete numerical findings instead of a methods-only description. This revision adds the numerical results above, labelled charts, explicit borough filtering, and code that regenerates the figures. The technical review comments used to make these changes are documented as implementation checks, not attributed to the peer reviewer.
