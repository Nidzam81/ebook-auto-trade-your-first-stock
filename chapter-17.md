# Chapter 17: Advanced Strategies (When You're Ready)

---

> **[IMAGE PLACEHOLDER: A person climbing a staircase. Bottom step: "RSI". Middle steps: "Bollinger Bands", "EMA Crossover". Top step: "Multi-Indicator Combo". Each step is bigger than the last. Style: progression illustration.]**

---

## When to Add Complexity

Do NOT read this chapter until you have:
- At least 1 month of profitable SIMULATE trading
- A solid understanding of your chosen strategy
- Comfortable reading trade logs and PnL reports

If you check all three boxes, keep reading. If not, go back and practice more.

---

## Combining Multiple Indicators

Single-indicator strategies (like RSI alone) work well. But you can make them stronger by combining indicators.

### Example: RSI + Volume

Instead of just "buy when RSI < 30", add a volume check:

```
Buy when:
- RSI < 30 (stock is cheap)
- AND volume is 1.5x average (people are buying heavily)
```

This filters out weak signals. The stock is cheap AND people are interested. Stronger signal.

---

### Example: RSI + EMA + Bollinger Bands

```
Buy when:
- RSI < 30 (cheap)
- Price is above 20-day EMA (overall trend is up)
- Price touches lower Bollinger Band (short-term dip)
```

Three indicators must all agree before buying. Fewer trades, but higher quality.

---

> **[IMAGE PLACEHOLDER: Three traffic lights stacked vertically. All three show green. Text: "All 3 indicators agree = STRONG signal". Style: simple infographic.]**

---

## Multi-Market Trading

Once you are comfortable with US stocks, you can trade other markets:

| Market | What You Need to Know |
|--------|----------------------|
| **KLSE** (Malaysia) | Different stock codes, MYR currency, different trading hours |
| **SGX** (Singapore) | SGD currency, overlapping hours with KLSE |
| **HKEX** (Hong Kong) | HKD currency, close to US market hours |

To add a KLSE agent:

```
Create a trading agent for [STOCK_CODE] on KLSE using RSI strategy in SIMULATE mode
```

---

## Sector Rotation Basics

Different sectors perform well at different times:

| Market Condition | Sectors That Do Well |
|-----------------|---------------------|
| Economic growth | Technology, Consumer Discretionary |
| Recession | Utilities, Healthcare, Consumer Staples |
| Rising interest rates | Financials |
| Falling rates | Real Estate, Technology |

You can create agents that rotate between sectors based on market conditions. But this is advanced -- do not attempt until you have 6+ months of experience.

---

## When NOT to Add Complexity

Do NOT add complexity when:
- Your current simple strategy is already profitable
- You do not fully understand the new indicator
- You have less than 3 months of trading experience
- You are adding complexity because you are bored

**If it ain't broke, don't fix it.**

---

## Chapter 17 Summary

| Advanced Concept | What It Does |
|-----------------|-------------|
| Multi-indicator | Combine 2+ signals for stronger entries |
| Multi-market | Trade US, KLSE, SGX, HKEX |
| Sector rotation | Shift between sectors based on market conditions |
| When to add | Only after 1+ month of profitable trading |

---

