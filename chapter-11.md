# Chapter 11: Creating Your First Trading Agent with Hermes

---

> **[IMAGE PLACEHOLDER: A person sitting at a computer, typing. Above their head: a thought bubble showing a robot with a cape holding a "BUY" and "SELL" sign. Style: cartoon excitement illustration.]**

---

## The Moment of Truth

You have your plan. Now let's tell Hermes to build your agent.

Open Hermes Agent and type the following prompt. I will explain what each part means after.

---

## The Master Prompt (Copy This!)

```
Create a trading agent for NVDA using RSI strategy in SIMULATE mode.

Rules:
- Buy 10 shares of NVDA when RSI drops below 30
- Sell 10 shares of NVDA when RSI goes above 70
- Use my moomoo SIMULATE account
- Check every 30 minutes during US market hours (9:30 AM - 4:00 PM ET)
- Log all trades to a trade log file
```

---

## What Hermes Does Behind the Scenes

After you press Enter, Hermes will do several things. Do not worry if you do not understand all of this yet -- just know that Hermes is working:

1. **Creates a strategy script** -- a small program that checks RSI and decides when to buy/sell
2. **Sets up a cron job** -- the alarm clock that runs every 30 minutes
3. **Connects to your moomoo account** -- through OpenD
4. **Creates a trade log** -- a file that records every buy and sell
5. **Starts the agent** -- it is now running in the background

This usually takes 30-60 seconds.

---

> **[IMAGE PLACEHOLDER: A progress bar or loading animation with steps: "1. Creating strategy... ✓", "2. Setting up cron job... ✓", "3. Connecting to moomoo... ✓", "4. Creating trade log... ✓", "5. Starting agent... ✓", "Agent is LIVE!". Style: clean progress illustration.]**

---

## What Hermes Will Say

When it is done, Hermes will reply with something like:

```
Trading agent created successfully!

Agent: NVDA-RSI
Stock: NVDA (NVIDIA)
Strategy: RSI (Buy < 30, Sell > 70)
Environment: SIMULATE
Schedule: Every 30 minutes (9:30 AM - 4:00 PM ET)
Trade log: C:\Trading\trades-nvda-rsi.csv

Your agent is now running. It will check NVDA's RSI every 30 minutes
and place trades automatically. You can check the trade log anytime.
```

---

## Verify It Is Running

To make sure your agent is actually working, type:

```
Show me my running agents
```

Hermes will list your active agents. You should see `NVDA-RSI` in the list.

---

## Check Your First Trade

Wait 30 minutes (or the next market open if it is after hours). Then type:

```
Show me my trade log for NVDA
```

If the agent found a good RSI signal, you will see your first trade recorded:

```
# | Time     | Agent   | Side | Qty | Price  | Entry | PnL
1 | 10:00 AM | NVDA-RSI| BUY  | 10  | $142.50| $142.50| --
2 | 2:30 PM  | NVDA-RSI| SELL | 10  | $145.20| $142.50| +$27.00
```

Congratulations. Your first automated trade just happened. While you were reading this book, your agent was working for you.

---

## What If There Are No Trades Yet?

Do not worry. The agent only trades when the RSI signal is right. Sometimes that takes hours or even days. The agent is patient. It waits for the right moment.

If you want to test that everything is working, type:

```
Force a test trade for NVDA in SIMULATE mode
```

This will make the agent place a fake trade immediately so you can see how it works.

---

## Chapter 11 Summary

| Step | Status |
|------|--------|
| Typed the master prompt | ☐ Done |
| Hermes created the agent | ☐ Done |
| Verified agent is running | ☐ Done |
| Saw my first trade in the log | ☐ Done (or waiting for signal) |

---

Now let's build your prompt library -- a collection of useful prompts you will use over and over.

---
