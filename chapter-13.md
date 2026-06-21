# Chapter 13: Reading Your Results

---

> **[IMAGE PLACEHOLDER: A person looking at a stock chart on a screen with a confused expression. A helpful robot points at the screen with a speech bubble saying "Let me explain!". Style: friendly cartoon.]**

---

## Understanding the Trade Log

Your agent records every trade in a **trade log**. This is a table that shows everything that happened. Let me teach you how to read it.

---

## The Trade Log Columns

Here is a sample trade log:

```
| # | Time     | Agent    | Status | Qty | Price   | Entry   | PnL    |
|---|----------|----------|--------|-----|---------|---------|--------|
| 1 | 10:00 AM | NVDA-RSI | BUY    | 10  | $142.50 | $142.50 | --     |
| 2 | 2:30 PM  | NVDA-RSI | SELL   | 10  | $145.20 | $142.50 | +$27.00|
| 3 | 11:00 AM | NVDA-RSI | BUY    | 10  | $143.00 | $143.00 | --     |
| 4 | 3:15 PM  | NVDA-RSI | SELL   | 10  | $141.50 | $143.00 | -$15.00|
```

Here is what each column means:

| Column | What It Means | Example |
|--------|---------------|---------|
| **#** | Trade number (just counting) | 1, 2, 3, 4... |
| **Time** | When the trade happened | 10:00 AM |
| **Agent** | Which agent made the trade | NVDA-RSI |
| **Status** | BUY or SELL | BUY |
| **Qty** | How many shares | 10 shares |
| **Price** | Price per share | $142.50 |
| **Entry** | Your original buy price | $142.50 |
| **PnL** | Profit or Loss on this trade | +$27.00 |

---

## How to Read a Trade Pair

Trades come in pairs: a **BUY** followed by a **SELL**.

```
BUY  10 shares at $142.50  (You spent $1,425.00)
SELL 10 shares at $145.20  (You received $1,452.00)
-------------------------------------------
Profit: $27.00
```

The PnL column shows the result of each pair. When you see `--`, it means the trade is still open (waiting for a sell).

---

> **[IMAGE PLACEHOLDER: Two hands exchanging money. Left hand gives $1,425 (labeled "BUY"). Right hand gives back $1,452 (labeled "SELL"). In the middle: "+$27 PROFIT" in green. Style: simple money illustration.]**

---

## Understanding PnL (Profit and Loss)

PnL is how much money you made or lost on a trade.

| PnL Value | What It Means | Emotion |
|-----------|---------------|---------|
| **+$27.00** | You made $27 | 😊 Happy |
| **-$15.00** | You lost $15 | 😐 It happens |
| **$0.00** | Break even | 😐 No big deal |
| **+$500.00** | Big win | 🎉 Exciting |
| **-$200.00** | Big loss | 😟 Learn from it |

**Important:** One loss does not mean you failed. Even the best traders lose on individual trades. The goal is to make more on your winners than you lose on your losers.

---

## The Weekly Review (10 Minutes Every Sunday)

Every Sunday, spend 10 minutes reviewing your agent's performance. Here is your checklist:

### Step 1: Check Total PnL

```
What is my total PnL this week?
```

Write down the number. Is it positive (good) or negative (needs attention)?

---

### Step 2: Count Your Trades

```
How many trades did my agents make this week?
```

If you had fewer than 5 trades, that is normal. Your agent only trades when the signal is right.

---

### Step 3: Check Win Rate

```
What is my win rate this week?
```

Win rate = (number of winning trades) / (total trades) x 100

| Win Rate | What It Means |
|----------|---------------|
| Above 60% | Excellent -- your strategy is working |
| 50-60% | Good -- acceptable for RSI strategy |
| 40-50% | Normal -- some strategies have lower win rates |
| Below 40% | Needs attention -- review your strategy |

---

### Step 4: Note Any Big Moves

Did any stock make a sudden big move? Was there news? Write a note about it. This helps you learn.

---

> **[IMAGE PLACEHOLDER: A weekly planner page with Sunday highlighted. Checkboxes: "☐ Check PnL", "☐ Count trades", "☐ Win rate", "☐ Note big moves". A coffee cup sits nearby. Style: cozy planning illustration.]**

---

## When to Celebrate vs When to Worry

| Situation | What to Do |
|-----------|-----------|
| Agent made $50 in a week | 🎉 Celebrate! Your system works. |
| Agent lost $50 in a week | 😐 Normal. Losses happen. Keep going. |
| Agent lost $500 in a week | 😟 Review. Maybe the market changed. |
| Agent made $500 in a week | 🎉 Great! But don't get cocky. |
| Agent did nothing for a week | 😐 Normal. No signals = no trades. |

---

## Chapter 13 Summary

| Concept | What It Means |
|---------|---------------|
| Trade log | A table showing every buy and sell |
| PnL | Profit (+) or Loss (-) on a trade |
| Open trade | Bought but not yet sold (shows `--`) |
| Closed trade | Bought and sold (shows PnL) |
| Win rate | Percentage of winning trades |
| Weekly review | 10-minute Sunday check-up |

---

You now have a working trading agent and you know how to read its results. Let's level up!

---
