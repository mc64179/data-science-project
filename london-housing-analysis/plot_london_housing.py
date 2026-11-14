from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
DATA = BASE / 'data' / '5. London Housing Data.csv'
FIG = BASE / 'figures'
FIG.mkdir(exist_ok=True)
df = pd.read_csv(DATA, parse_dates=['date'])
df['year'] = df['date'].dt.year

# The supplied file contains England and London aggregate rows as well as boroughs.
england = df[df['area'].eq('england')].copy()
price = england.groupby('year')['average_price'].agg(minimum_monthly_price='min', maximum_monthly_price='max').reset_index()
fig, ax = plt.subplots(figsize=(10, 5.8), constrained_layout=True)
ax.plot(price['year'], price['minimum_monthly_price'], label='Lowest monthly average price', linewidth=2)
ax.plot(price['year'], price['maximum_monthly_price'], label='Highest monthly average price', linewidth=2)
ax.set_title('England Average House Prices by Year')
ax.set_xlabel('Year')
ax.set_ylabel('Average price (£)')
ax.grid(axis='y', alpha=.25)
ax.legend(frameon=False)
ax.yaxis.set_major_formatter(lambda x, pos: f'£{x:,.0f}')
fig.savefig(FIG / 'yearly-price-range.svg', format='svg', dpi=160)
fig.savefig(FIG / 'yearly-price-range.png', dpi=160)
plt.close(fig)

boroughs = ['city of london','barking and dagenham','barnet','bexley','brent','bromley','camden','croydon','ealing','enfield','greenwich','hackney','hammersmith and fulham','haringey','harrow','havering','hillingdon','hounslow','islington','kensington and chelsea','kingston upon thames','lambeth','lewisham','merton','newham','redbridge','richmond upon thames','southwark','sutton','tower hamlets','waltham forest','wandsworth','westminster']
crime = (df[df['area'].isin(boroughs)].groupby('area', as_index=False)['no_of_crimes'].max().dropna().sort_values('no_of_crimes'))
fig, ax = plt.subplots(figsize=(10, 8), constrained_layout=True)
ax.barh(crime['area'].str.title(), crime['no_of_crimes'], color='#4472C4')
ax.set_title('Maximum Monthly Recorded Crime Count by London Borough')
ax.set_xlabel('Maximum recorded crimes in one month')
ax.set_ylabel('London borough')
ax.grid(axis='x', alpha=.25)
for i, v in enumerate(crime['no_of_crimes']): ax.text(v + max(crime['no_of_crimes'])*.01, i, f'{int(v):,}', va='center', fontsize=8)
fig.savefig(FIG / 'crime-by-borough.svg', format='svg', dpi=160)
fig.savefig(FIG / 'crime-by-borough.png', dpi=160)
plt.close(fig)

low = (df[df['area'].isin(boroughs) & (df['average_price'] < 100000)].groupby('area').size().sort_values(ascending=True))
fig, ax = plt.subplots(figsize=(9, 6), constrained_layout=True)
ax.barh(low.index.str.title(), low.values, color='#70AD47')
ax.set_title('Records with Average Price Below £100,000')
ax.set_xlabel('Number of monthly records')
ax.set_ylabel('London borough')
ax.grid(axis='x', alpha=.25)
fig.savefig(FIG / 'low-price-records.svg', format='svg', dpi=160)
fig.savefig(FIG / 'low-price-records.png', dpi=160)
plt.close(fig)
print('created', price.shape, crime.shape, low.shape)
