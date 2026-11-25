"""Generate deterministic SVG figures from the supplied CSV."""
from html import escape
from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent
DATA = BASE / "data" / "5. London Housing Data.csv"
FIG = BASE / "figures"
FIG.mkdir(exist_ok=True)

def text(x, y, value, size=11, anchor="middle", weight="normal", rotate=None):
    transform = f' transform="rotate({rotate} {x:.1f} {y:.1f})"' if rotate else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" '
            f'font-family="Arial" font-size="{size}" font-weight="{weight}"{transform}>'
            f'{escape(str(value))}</text>')

def start(width, height, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}"><rect width="100%" height="100%" fill="white"/>'
            + text(width / 2, 30, title, 20, weight="bold"))

def price_chart(price):
    W, H, L, R, T, B = 1000, 580, 90, 35, 78, 70
    x = lambda year: L + (year - 1995) / 25 * (W - L - R)
    y = lambda value: T + (300000 - value) / 300000 * (H - T - B)
    svg = start(W, H, "England Average House Prices by Year")
    svg += text(W / 2, 51, "Monthly minimum and maximum within each year", 11)
    for tick in range(0, 300001, 50000):
        yy = y(tick)
        svg += f'<line x1="{L}" y1="{yy:.1f}" x2="{W-R}" y2="{yy:.1f}" stroke="#ddd"/>'
        svg += text(L - 10, yy + 4, f"£{tick:,.0f}", 10, "end")
    svg += f'<line x1="{L}" y1="{T}" x2="{L}" y2="{H-B}" stroke="black"/>'
    svg += f'<line x1="{L}" y1="{H-B}" x2="{W-R}" y2="{H-B}" stroke="black"/>'
    for year in range(1995, 2021, 5): svg += text(x(year), H-B+22, year, 10)
    rows = list(price.itertuples())
    low = " ".join(f"{x(r.year):.1f},{y(r.minimum_monthly_price):.1f}" for r in rows)
    high = " ".join(f"{x(r.year):.1f},{y(r.maximum_monthly_price):.1f}" for r in rows)
    area = " ".join([f"{x(r.year):.1f},{y(r.maximum_monthly_price):.1f}" for r in rows] + [f"{x(r.year):.1f},{y(r.minimum_monthly_price):.1f}" for r in rows[::-1]])
    svg += f'<polygon points="{area}" fill="#4472C4" fill-opacity="0.14"/>'
    svg += f'<polyline fill="none" stroke="#4472C4" stroke-width="2" points="{low}"/>'
    svg += f'<polyline fill="none" stroke="#C00000" stroke-width="2" points="{high}"/>'
    svg += text(W / 2, H-14, "Year", 12) + text(20, H / 2, "Average price (£)", 12, rotate=-90)
    for yy, color, legend in [(H-34, '#4472C4', 'Lowest monthly average price'), (H-16, '#C00000', 'Highest monthly average price')]:
        svg += f'<line x1="{W-300}" y1="{yy}" x2="{W-280}" y2="{yy}" stroke="{color}" stroke-width="3"/>' + text(W-274, yy+4, legend, 10, "start")
    (FIG / "yearly-price-range.svg").write_text(svg + "</svg>", encoding="utf-8")

def bar_chart(series, filename, title, xlabel, color, note, max_value, width, height):
    L, R, T, B = 230, 80, 65, 55
    row_h = (height - T - B) / len(series)
    # Use rounded, visible tick marks and leave room for the largest bar label.
    tick_step = max(1, int(__import__('math').ceil(max_value / 4)))
    axis_max = tick_step * 4
    x = lambda value: L + value / axis_max * (width - L - R)
    svg = start(width, height, title)
    for tick in range(0, axis_max + 1, tick_step):
        xx = x(tick)
        svg += f'<line x1="{xx:.1f}" y1="{T}" x2="{xx:.1f}" y2="{height-B}" stroke="#ddd"/>' + text(xx, height-B+22, f"{tick:,}", 10)
    for i, (name, value) in enumerate(series.items()):
        yy = T + (i + .5) * row_h
        svg += text(L-10, yy+4, name.title(), 10, "end")
        svg += f'<rect x="{L}" y="{yy-row_h*.3:.1f}" width="{x(value)-L:.1f}" height="{row_h*.6:.1f}" fill="{color}"/>' + text(x(value)+8, yy+4, f"{int(value):,}", 10, "start")
    svg += text(width/2, height-12, xlabel, 12) + text(width/2, 48, note, 11)
    (FIG / filename).write_text(svg + "</svg>", encoding="utf-8")

df = pd.read_csv(DATA, parse_dates=["date"])
df["year"] = df["date"].dt.year
price = df[df["area"].eq("england")].groupby("year")["average_price"].agg(minimum_monthly_price="min", maximum_monthly_price="max").reset_index()
price_chart(price)
boroughs = ["city of london", "barking and dagenham", "barnet", "bexley", "brent", "bromley", "camden", "croydon", "ealing", "enfield", "greenwich", "hackney", "hammersmith and fulham", "haringey", "harrow", "havering", "hillingdon", "hounslow", "islington", "kensington and chelsea", "kingston upon thames", "lambeth", "lewisham", "merton", "newham", "redbridge", "richmond upon thames", "southwark", "sutton", "tower hamlets", "waltham forest", "wandsworth", "westminster"]
crime = df[df["area"].isin(boroughs)].groupby("area")["no_of_crimes"].max().dropna().sort_values()
bar_chart(crime, "crime-by-borough.svg", "Maximum Monthly Recorded Crime Count by London Borough", "Maximum recorded crimes in one month", "#4472C4", "Boroughs only; aggregate regional rows excluded", 8000, 1000, 820)
low = df[df["area"].isin(boroughs) & (df["average_price"] < 100000)].groupby("area").size().sort_values()
bar_chart(low, "low-price-records.svg", "Records with Average Price Below £100,000", "Number of monthly records", "#70AD47", "London boroughs only", int(low.max()), 900, 760)
print(f"created {len(price)} yearly rows, {len(crime)} borough rows, and {len(low)} low-price rows")
