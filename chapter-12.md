# Chapter 12: Useful Prompt Examples (Your Prompt Library)

---

> **[IMAGE PLACEHOLDER: An open book with pages flying out. Each page has a different prompt written on it like a recipe card. Style: whimsical illustration.]**

---

## Why You Need This Chapter

Every time you want Hermes to do something, you need to type a **prompt**. A prompt is just a sentence that tells Hermes what you want.

This chapter gives you **copy-paste prompts** for everything you will ever need. You do not need to memorize them. Just bookmark this chapter and come back when you need a prompt.

---

## Category 1: Creating Agents

### Prompt 1.1: Create a Basic RSI Agent

```
Create a trading agent for [STOCK_SYMBOL] using RSI strategy in SIMULATE mode.
Buy when RSI < 30, sell when RSI > 70.
Check every 30 minutes during US market hours.
```

**Example:** Replace `[STOCK_SYMBOL]` with `NVDA`, `AAPL`, `TSLA`, etc.

---

### Prompt 1.2: Create a Bollinger Bands Agent

```
Create a trading agent for [STOCK_SYMBOL] using Bollinger Bands strategy in SIMULATE mode.
Buy when price touches lower band, sell when price touches upper band.
Check every 30 minutes during US market hours.
```

---

### Prompt 1.3: Create an EMA Crossover Agent

```
Create a trading agent for [STOCK_SYMBOL] using EMA crossover strategy in SIMULATE mode.
Buy when price crosses above 20-day EMA, sell when price crosses below 20-day EMA.
Check every 30 minutes during US market hours.
```

---

> **[IMAGE PLACEHOLDER: Three recipe cards side by side. Card 1: "RSI Recipe - Buy < 30, Sell > 70". Card 2: "Bollinger Recipe - Buy lower, Sell upper". Card 3: "EMA Recipe - Buy above, Sell below". Style: clean card illustration.]**

---

## Category 2: Checking Status

### Prompt 2.1: Check All Running Agents

```
Show me all my running trading agents
```

---

### Prompt 2.2: Check a Specific Agent's Status

```
Show me the status of my [AGENT_NAME] agent
```

---

### Prompt 2.3: Check Account Balance

```
What is my moomoo account balance?
```

---

### Prompt 2.4: Check Current Holdings

```
What stocks do I currently own?
```

---

## Category 3: Trade Logs

### Prompt 3.1: Show Today's Trades

```
Show me today's trade log
```

---

### Prompt 3.2: Show Trades for a Specific Stock

```
Show me all trades for [STOCK_SYMBOL]
```

---

### Prompt 3.3: Show Profit and Loss Summary

```
What is my total PnL across all agents?
```

---

> **[IMAGE PLACEHOLDER: A sample trade log table with columns: Time, Agent, Side, Qty, Price, PnL. Some rows have green (+$) and some have red (-$) values. Style: clean table illustration.]**

---

## Category 4: Controlling Agents

### Prompt 4.1: Stop a Specific Agent

```
Stop my [AGENT_NAME] agent
```

---

### Prompt 4.2: Stop ALL Agents (The Panic Button)

```
Stop all trading agents immediately
```

**Important:** This is your emergency button. If something goes wrong, type this.

---

### Prompt 4.3: Start an Agent

```
Start my [AGENT_NAME] agent
```

---

### Prompt 4.4: Change an Agent's Strategy

```
Change my NVDA agent to use Bollinger Bands strategy instead of RSI
```

---

## Category 5: Scanning and Research

### Prompt 5.1: Scan for Unusual Volume

```
Scan the market for stocks with unusual volume today
```

---

### Prompt 5.2: Check a Stock's RSI

```
What is the current RSI of [STOCK_SYMBOL]?
```

---

### Prompt 5.3: Find Top Gainers

```
Show me the top gaining stocks today
```

---

## Category 6: Dashboard and Visualization

### Prompt 6.1: Create a Dashboard

```
Create a trading dashboard showing all my agents, trades, and PnL
```

---

### Prompt 6.2: Show Dashboard

```
Open my trading dashboard
```

---

### Prompt 6.3: Export Trade History

```
Export my trade history to a CSV file
```

---

## Category 7: Advanced Prompts

### Prompt 7.1: Create a Multi-Stock Agent

```
Create an agent that trades NVDA and AAPL using RSI strategy in SIMULATE mode
```

---

### Prompt 7.2: Set a Stop-Loss

```
Set a 5% stop-loss on all my positions
```

---

### Prompt 7.3: Backtest a Strategy

```
Backtest RSI strategy on NVDA for the past 30 days
```

---

## How to Modify These Prompts

All prompts follow a pattern:

```
[Action] + [What] + [Details] + [Options]
```

Examples:
- **Action:** "Create" / "Show" / "Stop" / "Change"
- **What:** "a trading agent" / "my balance" / "the trade log"
- **Details:** "for NVDA" / "using RSI" / "today"
- **Options:** "in SIMULATE mode" / "every 30 minutes"

Mix and match to create your own prompts.

---

## Common Prompt Mistakes

| Mistake | Wrong | Right |
|---------|-------|-------|
| Too vague | "Do something" | "Check NVDA RSI" |
| Missing environment | "Buy NVDA" | "Buy NVDA in SIMULATE mode" |
| Too many things at once | "Create agent for NVDA and AAPL and TSLA and..." | "Create agent for NVDA" (then repeat) |
| Missing stock name | "Check RSI" | "Check NVDA RSI" |

---

## Chapter 12 Summary

| Category | What It Does |
|----------|-------------|
| Creating Agents | Set up new trading agents |
| Checking Status | See what your agents are doing |
| Trade Logs | View your buy/sell history |
| Controlling Agents | Start, stop, or modify agents |
| Scanning & Research | Find trading opportunities |
| Dashboard | Visual overview of everything |
| Advanced | Multi-stock, backtesting, stop-loss |

---

Now let's learn how to read the results your agent gives you.

---
