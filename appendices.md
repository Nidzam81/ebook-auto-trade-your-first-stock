# APPENDICES

---

# Appendix A: Glossary

---

> **[IMAGE PLACEHOLDER: An open dictionary page with "Trading Dictionary" at the top. Words and definitions are laid out in a clean format. Style: dictionary illustration.]**

---

| Term | Definition (In Plain English) |
|------|-------------------------------|
| **Agent** | A robot program that trades stocks for you automatically |
| **API** | A way for two computer programs to talk to each other |
| **Backtest** | Testing a strategy on old data to see if it would have worked |
| **Bollinger Bands** | Lines on a chart that show if a stock is too cheap or too expensive |
| **Broker** | The company (like moomoo) that lets you buy and sell stocks |
| **Cron Job** | An alarm clock for your computer -- it runs tasks on a schedule |
| **Dashboard** | A web page that shows all your trading info in one place |
| **EMA** | Exponential Moving Average -- a smoothed-out line showing a stock's trend |
| **Environment** | Whether you are using SIMULATE (practice) or LIVE (real money) |
| **Entry** | The price at which you bought a stock |
| **Kill Switch** | A command that stops all agents immediately |
| **LIVE** | Real trading with real money |
| **moomoo** | A trading app/broker used in this book |
| **OpenD** | The bridge program that connects Hermes to moomoo |
| **PnL** | Profit and Loss -- how much money you made or lost |
| **Position** | How many shares of a stock you currently own |
| **Prompt** | A sentence you type to tell Hermes what to do |
| **RSI** | Relative Strength Index -- a number showing if a stock is cheap or expensive |
| **SIMULATE** | Practice mode with fake money -- zero risk |
| **Stop-Loss** | An automatic sell order that limits your losses |
| **Strategy** | A set of rules that tells the agent when to buy and sell |
| **Trade Log** | A record of every buy and sell the agent makes |
| **Volatility** | How much a stock's price goes up and down |
| **Win Rate** | The percentage of trades that make money |

---

# Appendix B: Keyboard Shortcuts & Commands Cheat Sheet

---

## Hermes Keyboard Shortcuts

| Shortcut | What It Does |
|----------|-------------|
| **Enter** | Send your message |
| **Shift + Enter** | Add a new line without sending |
| **Ctrl + C** | Copy selected text |
| **Ctrl + V** | Paste text |
| **Ctrl + Z** | Undo |
| **Up Arrow** | Recall your previous message |

---

## Essential Commands (Copy-Paste Ready)

### Emergency
```
Stop all trading agents immediately
```

### Daily Use
```
Show me my running agents
What is my account balance?
What is my PnL today?
Show me today's trade log
```

### Creating Agents
```
Create a trading agent for [STOCK] using RSI strategy in SIMULATE mode
```

### Research
```
What is the current RSI of [STOCK]?
Scan for stocks with unusual volume
```

### Dashboard
```
Create a trading dashboard
Open my trading dashboard
```

---

# Appendix C: Recommended Stocks for Beginners

---

## US Stocks (High Volume, Clear Trends)

| Stock | Symbol | Sector | Why It's Good |
|-------|--------|--------|---------------|
| NVIDIA | NVDA | Technology | Active trading, clear trends |
| Apple | AAPL | Technology | Most liquid stock, stable |
| Microsoft | MSFT | Technology | Steady performer |
| Amazon | AMZN | Consumer/Retail | High volume, good for beginners |
| Tesla | TSLA | Automotive | Very active, lots of signals |
| Meta | META | Technology | Popular, good volume |

---

## KLSE Stocks (Malaysia)

| Stock | Code | Sector | Why It's Good |
|-------|------|--------|---------------|
| Unisem | 0050 | Technology | Active, good volume |
| Gamuda | 5398 | Construction | Large cap, liquid |
| IOI Corp | 1961 | Plantation | Stable, well-known |
| QL Resources | 7084 | Consumer | Consistent performer |

---

## Tips for Choosing Stocks

1. **Pick stocks you know** -- companies you have heard of
2. **Check volume** -- trade stocks that have lots of daily trading activity
3. **Avoid penny stocks** -- stocks under $1 are very risky
4. **Start with 1-2 stocks** -- do not try to trade 10 at once

---

# Appendix D: Template Prompts Library

---

## Template 1: Create RSI Agent
```
Create a trading agent for [STOCK] using RSI strategy in SIMULATE mode.
Buy [Qty] shares when RSI < 30.
Sell [Qty] shares when RSI > 70.
Check every [Minutes] minutes during [MARKET] market hours.
```

## Template 2: Create Bollinger Bands Agent
```
Create a trading agent for [STOCK] using Bollinger Bands strategy in SIMULATE mode.
Buy when price touches lower band.
Sell when price touches upper band.
Check every [Minutes] minutes.
```

## Template 3: Create EMA Crossover Agent
```
Create a trading agent for [STOCK] using EMA crossover strategy in SIMULATE mode.
Buy when price crosses above [N]-day EMA.
Sell when price crosses below [N]-day EMA.
Check every [Minutes] minutes.
```

## Template 4: Multi-Stock Agent
```
Create a trading agent that trades [STOCK1] and [STOCK2] using [STRATEGY] strategy in SIMULATE mode.
Allocate [Amount] to each stock.
```

## Template 5: Stop-Loss Setup
```
Set a [N]% stop-loss on all my [ENVIRONMENT] positions.
```

## Template 6: Backtest
```
Backtest [STRATEGY] strategy on [STOCK] for the past [N] days.
Show me the results including total return and win rate.
```

## Template 7: Dashboard Creation
```
Create a trading dashboard showing:
- Account balance
- All active agents and their PnL
- Today's trade log
- Performance chart
Auto-refresh every [N] seconds.
```

---

# Appendix E: Where to Get Help

---

## Official Resources

| Resource | URL | What You'll Find |
|----------|-----|-----------------|
| Hermes Agent Docs | hermes-agent.nousresearch.com/docs | Official documentation |
| moomoo Support | moomoo.com/support | Account help, trading questions |
| moomoo API Docs | moomooapi.readthedocs.io | Technical API reference |

---

## Community

| Platform | Where | What You'll Find |
|----------|-------|-----------------|
| Reddit | r/moomoo | moomoo user community |
| Reddit | r/algotrading | Algorithmic trading discussion |
| Discord | Search "moomoo trading" | Real-time chat with traders |

---

## When to Ask for Help

Ask for help when:
- You have tried the troubleshooting steps in Chapter 18
- You have checked the connection (moomoo + OpenD + Hermes all running)
- You have read the error message carefully

Do NOT ask for help when:
- You haven't tried restarting your computer (try that first)
- You haven't checked if moomoo is open (check that first)
- The answer is in this book (use the table of contents)

---

## How to Ask a Good Question

When asking for help, include:

1. **What you were trying to do** (e.g., "I was trying to create an NVDA agent")
2. **What happened** (e.g., "Hermes said 'Connection failed'")
3. **What you already tried** (e.g., "I restarted moomoo and checked OpenD")
4. **The exact error message** (copy-paste it)

Bad question: "Help it not working"
Good question: "Hermes says 'Connection failed' when I try to check my balance. I have moomoo open and enabled OpenD. I restarted both programs. Error message: 'Cannot reach localhost:18888'"

---
