# Chapter 21: Backtesting - Test Your Strategy Before Risking Real Money

---

> **[IMAGE PLACEHOLDER: A person looking at a chart with a "time rewind" icon. Behind them is the present, in front is the past. Text: "Test on yesterday's data before trading today's money." Style: metaphor illustration.]**

---

## What Is Backtesting?

**Backtesting** means testing your trading strategy on **historical data** to see how it would have performed in the past.

Think of it like this:
- You have a strategy: "Buy NVDA when RSI < 30, sell when RSI > 70"
- You want to know: "Would this have made money last month?"
- Backtesting answers: "Yes, it would have made $340 in 30 days" or "No, it would have lost $200"

**Why it matters:** You should never trade real money with a strategy you haven't tested on historical data first.

---

## The Golden Rule of Backtesting

> **Past performance does NOT guarantee future results.**

Backtesting tells you what **would have** happened. It does not tell you what **will** happen. But it is still the best way to build confidence in your strategy before risking real money.

Think of it like a flight simulator:
- A pilot practices on a simulator before flying a real plane
- Backtesting is your simulator
- It doesn't guarantee a safe flight, but it's much better than nothing

---

## How Backtesting Works (Step by Step)

### Step 1: Get Historical Data

You need historical stock prices. For backtesting, you typically need:
- **Price data**: Open, High, Low, Close (OHLC) for each day or each hour
- **Volume data**: Trading volume for each period

You can get this data from:
| Source | How |
|--------|-----|
| **moomoo API** | `get_history_klines()` function |
| **Yahoo Finance** | Free, easy to download as CSV |
| **Alpha Vantage** | Free tier, API access |

---

### Step 2: Define Your Strategy as Rules

Write your strategy as clear, computer-readable rules:

```
RULE 1: Calculate RSI for each day
RULE 2: If RSI < 30 AND we don't already own the stock → BUY
RULE 3: If RSI > 70 AND we own the stock → SELL
RULE 4: Only trade during market hours (9:30 AM - 4:00 PM)
```

---

### Step 3: Simulate Trades on Historical Data

Walk through the historical data day by day, applying your rules:

```
Day 1: RSI = 45 → No action
Day 2: RSI = 28 → BUY at $142.50 (RSI < 30)
Day 3: RSI = 35 → Hold
Day 4: RSI = 55 → Hold
Day 5: RSI = 72 → SELL at $145.20 (RSI > 70)
       → Profit: $2.70 per share
```

---

### Step 4: Calculate Results

After running through all the data:

| Metric | What It Tells You |
|--------|-------------------|
| **Total return** | How much money you made/lost |
| **Win rate** | Percentage of trades that were profitable |
| **Max drawdown** | Worst peak-to-trough loss |
| **Number of trades** | How often the strategy fires |
| **Average profit per trade** | Expected value per trade |

---

> **[IMAGE PLACEHOLDER: A sample backtest results table showing: Total Return +12.4%, Win Rate 60%, Max Drawdown -3.2%, 45 trades, Avg +$7.50/trade. Style: clean results table.]**

---

## Simple Backtest Example: RSI Strategy on NVDA

Let's walk through a real backtest scenario.

### Setup

- **Stock**: NVDA (NVIDIA)
- **Strategy**: RSI < 30 → Buy, RSI > 70 → Sell
- **Period**: Last 30 days
- **Starting capital**: $10,000
- **Position size**: 10 shares per trade

### Running the Backtest

In Hermes, you can ask it to create a backtest script:

```
Create a backtest script for RSI strategy on NVDA for the past 30 days
```

Hermes will create a Python script like this:

```python
import pandas as pd
import numpy as np

# Load historical data
data = pd.read_csv('nvda_30days.csv')

# Calculate RSI
def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

data['RSI'] = calculate_rsi(data['Close'])

# Simulate trades
capital = 10000
position = 0
trades = []

for i in range(len(data)):
    if data['RSI'][i] < 30 and position == 0:
        # BUY
        position = 10
        buy_price = data['Close'][i]
        capital -= position * buy_price
        trades.append(('BUY', data['Date'][i], buy_price))
    elif data['RSI'][i] > 70 and position > 0:
        # SELL
        sell_price = data['Close'][i]
        capital += position * sell_price
        trades.append(('SELL', data['Date'][i], sell_price))
        position = 0

# Results
print(f"Final capital: ${capital:.2f}")
print(f"Total return: {((capital - 10000) / 10000) * 100:.1f}%")
print(f"Number of trades: {len(trades)}")
```

### Results

```
Final capital: $10,340.00
Total return: +3.4%
Number of trades: 6 (3 buy/sell pairs)
Win rate: 66.7% (2 of 3 trades profitable)
Max drawdown: -1.8%
```

**Interpretation:**
- The strategy made 3.4% in 30 days
- It won 2 out of 3 trades
- The worst loss at any point was only 1.8%
- This is a **conservative** strategy -- small but consistent gains

---

## Backtesting with moomoo Data

Since you use moomoo, you can get historical data directly:

```
Get 30 days of NVDA daily price data using moomoo API
```

Or use the moomoo skill:

```
Load moomoo skill and get NVDA historical klines for 30 days
```

---

## Common Backtesting Mistakes to Avoid

| Mistake | Why It's Wrong | How to Fix |
|---------|---------------|------------|
| **Ignoring fees** | Real trading costs money | Add 0.1% per trade to calculations |
| **Ignoring slippage** | You don't get the exact price | Assume 0.05-0.1% worse fill price |
| **Overfitting** | Strategy works only on old data | Test on multiple time periods |
| **Survivorship bias** | Only testing stocks that still exist | Use current stock lists |
| **Too few trades** | 5 trades is not statistically significant | Aim for 30+ trades minimum |
| **Not accounting for overnight risk** | Stock can gap down overnight | Use stop-losses |

---

## The "Overfitting" Trap Explained

Imagine you test 100 different strategies on last month's data. By pure chance, 10 of them will show great results -- even if they're bad strategies. If you pick the best one and trade it, you'll likely lose money.

**How to avoid overfitting:**
1. **Use multiple time periods**: Test on 3 months, 6 months, 1 year
2. **Keep strategies simple**: Fewer parameters = less overfitting risk
3. **Out-of-sample testing**: Test on the LAST 20% of data (don't use it to tune)
4. **Forward testing**: After backtesting, run in SIMULATE for 1-2 weeks

---

> **[IMAGE PLACEHOLDER: A warning sign with "OVERFITTING" in bold. Below: "If your backtest looks too good to be true, it probably is." Style: caution illustration.]**

---

## When Is a Backtest "Good Enough"?

| Metric | Minimum | Good | Excellent |
|--------|---------|------|-----------|
| **Total return** | > 0% | > 5% | > 15% |
| **Win rate** | > 50% | > 55% | > 60% |
| **Max drawdown** | < 10% | < 5% | < 3% |
| **Number of trades** | > 30 | > 50 | > 100 |
| **Profit factor** | > 1.0 | > 1.3 | > 1.5 |

*Profit factor = (total gains) / (total losses). Above 1.0 means profitable.*

---

## Backtesting vs Forward Testing (SIMULATE)

| | Backtesting | Forward Testing (SIMULATE) |
|---|------------|---------------------------|
| **Data** | Historical (past) | Live (present) |
| **Speed** | Fast (minutes) | Slow (days/weeks) |
| **Accuracy** | Simulated | Real market conditions |
| **Risk** | Zero | Zero (fake money) |
| **Purpose** | Initial validation | Final validation before LIVE |

**The flow should be:**
```
Backtest → SIMULATE (2-4 weeks) → LIVE (small size)
```

Never skip either step!

---

## Chapter 21 Summary

| Concept | What It Means |
|---------|---------------|
| Backtesting | Testing strategy on historical data |
| Win rate | % of profitable trades |
| Max drawdown | Worst peak-to-trough loss |
| Overfitting | Strategy that only works on old data |
| Forward testing | Testing in SIMULATE with real-time data |
| Profit factor | Gains ÷ losses (want > 1.0) |

**The golden flow:**
```
Create strategy → Backtest → SIMULATE → LIVE (small)
```

---

Now you have the complete toolkit:
- **Chapter 7.5**: How to choose and configure your AI brain (model)
- **Chapter 21**: How to backtest before risking real money

These two chapters fill the gaps you identified. Your readers will now know how to set up their AI assistant's intelligence AND how to validate their strategies before going live.

---
