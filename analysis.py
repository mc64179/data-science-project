"""Generate the figures used in the stock-trend project."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
FIGURE_DIR = ROOT / "visualizations"
TICKERS = ["GOOGL", "FB", "AAPL", "AMZN", "MSFT"]


def load_prices() -> pd.DataFrame:
    frames = []
    for ticker in TICKERS:
        path = DATA_DIR / f"{ticker}_data.csv"
        frame = pd.read_csv(path, parse_dates=["date"])
        frame["ticker"] = ticker
        frames.append(frame[["date", "close", "ticker"]])
    return pd.concat(frames, ignore_index=True)


def save_closing_prices(prices: pd.DataFrame) -> None:
    pivot = prices.pivot(index="date", columns="ticker", values="close")
    ax = pivot[TICKERS].plot(figsize=(11, 6), linewidth=1.5)
    ax.set(title="Closing Prices of Five Technology Companies", xlabel="Date", ylabel="Closing price (USD)")
    ax.grid(alpha=0.25)
    ax.legend(title="Company", ncol=3)
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "closing-price-trends.png", dpi=180)
    plt.close()


def save_growth_comparison(prices: pd.DataFrame) -> None:
    pivot = prices.pivot(index="date", columns="ticker", values="close")
    normalized = pivot.div(pivot.iloc[0]).mul(100)
    ax = normalized[TICKERS].plot(figsize=(11, 6), linewidth=1.7)
    ax.axhline(100, color="#444444", linewidth=0.8, linestyle="--")
    ax.set(title="Growth of a $100 Equivalent Investment", xlabel="Date", ylabel="Indexed value (start = 100)")
    ax.grid(alpha=0.25)
    ax.legend(title="Company", ncol=3)
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "normalized-growth.png", dpi=180)
    plt.close()


def main() -> None:
    FIGURE_DIR.mkdir(exist_ok=True)
    prices = load_prices()
    save_closing_prices(prices)
    save_growth_comparison(prices)
    print(f"Generated two figures in {FIGURE_DIR}")


if __name__ == "__main__":
    main()
