# PART 4: BUILDING YOUR FIRST TRADING AGENT

---

# Chapter 10: Planning Your First Agent

---

> **[IMAGE PLACEHOLDER: A person standing at a whiteboard with "My First Trading Agent" written at the top. Below: "Stock?", "Strategy?", "How much?". They hold a marker thinking. Style: cartoon planning scene.]**

---

## Why Plan First?

You would not build a house without a blueprint. You would not cook a meal without knowing the recipe. And you should not create a trading agent without a plan.

Planning takes 5 minutes. It saves you hours of confusion later.

---

## The Three Questions

Before you create your agent, answer these three questions:

### Question 1: What Stock Will You Trade?

Pick **one stock** to start. Just one. Do not try to trade ten stocks on your first day.

Good starter stocks (liquid, well-known, not too volatile):

| Stock | Symbol | Why It's Good for Beginners |
|-------|--------|---------------------------|
| NVIDIA | NVDA | Popular, lots of trading volume, clear trends |
| Apple | AAPL | Most famous stock, stable movement |
| Microsoft | MSFT | Steady, predictable |
| Amazon | AMZN | High volume, active trading |

**Recommendation for your first agent:** Start with **NVDA** (NVIDIA). It is active enough to give you signals to trade, but not so wild that you will panic.

---

### Question 2: What Strategy Will You Use?

From Chapter 8, pick one strategy. For your first agent:

**Pick RSI.** It is the easiest to understand and works well.

Your rules:
- **Buy** when RSI drops below 30 (stock is cheap)
- **Sell** when RSI goes above 70 (stock is expensive)

---

### Question 3: How Much "Money" Will You Use?

In SIMULATE mode, you get fake money (usually $1,000,000 virtual). You do not need to worry about running out.

But decide: how much of your virtual money will you allocate to this one agent?

**Recommendation:** Start with $100,000 of your virtual $1,000,000. That is 10%. If the agent works well, you can add more later.

---

> **[IMAGE PLACEHOLDER: A simple worksheet/form with three sections filled in: "Stock: NVDA", "Strategy: RSI (Buy < 30, Sell > 70)", "Virtual Capital: $100,000". Style: clean document illustration.]**

---

## Write Down Your Plan

Seriously. Get a piece of paper or open Notepad and write:

```
My First Trading Agent Plan
===========================
Stock: NVDA (NVIDIA)
Strategy: RSI
- Buy when RSI < 30
- Sell when RSI > 70
Virtual Capital: $100,000
Environment: SIMULATE
Schedule: Every 30 minutes during US market hours
```

Keep this paper near your computer. It is your blueprint.

---

## Chapter 10 Summary

| Decision | My Choice |
|----------|-----------|
| Stock | NVDA |
| Strategy | RSI |
| Virtual Capital | $100,000 |
| Environment | SIMULATE |
| Schedule | Every 30 min |

---

Now let's actually build this thing.

---
