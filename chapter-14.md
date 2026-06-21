# PART 5: LEVELING UP

---

# Chapter 14: Running Multiple Agents at Once

---

> **[IMAGE PLACEHOLDER: Three robots standing in a line, each holding a different stock ticker: NVDA, AAPL, TSLA. They are wearing different colored hats. Style: fun cartoon.]**

---

## Why More Agents?

One agent is great. But what if you want to trade multiple stocks? Or use different strategies?

You can run **multiple agents at once**. Each agent trades independently, following its own rules.

Example setup:

| Agent | Stock | Strategy | Market |
|-------|-------|----------|--------|
| NVDA-RSI | NVDA | RSI | US |
| AAPL-BB | AAPL | Bollinger Bands | US |
| TSLA-EMA | TSLA | EMA Crossover | US |

---

## How Many Agents Should You Run?

| Experience Level | Recommended Agents |
|-----------------|-------------------|
| Beginner (first month) | 1 agent |
| Intermediate (1-3 months) | 2-3 agents |
| Advanced (3+ months) | 4-5 agents |
| Expert (6+ months) | 6+ agents |

**Do not start with 5 agents.** Start with 1. Add one more only when you are comfortable with the first.

---

## Making Sure Agents Don't Conflict

Agents can sometimes conflict. For example:
- Agent A wants to BUY NVDA
- Agent B wants to SELL NVDA

To avoid conflicts:
1. **Give each agent different stocks** (easiest solution)
2. **Give each agent a different strategy** on the same stock (advanced)
3. **Set a total budget** so agents don't over-spend

---

## Checking All Your Agents

```
Show me all my running agents and their PnL
```

Hermes will show a summary:

```
| Agent    | Stock | PnL Today | Total PnL | Status |
|----------|-------|-----------|-----------|--------|
| NVDA-RSI | NVDA  | +$27.00   | +$340.00  | Active |
| AAPL-BB  | AAPL  | -$12.00   | +$85.00   | Active |
| TSLA-EMA | TSLA  | +$0.00    | -$45.00   | Active |
```

---

## Chapter 14 Summary

| Tip | What It Means |
|-----|---------------|
| Start with 1 agent | Do not overcomplicate |
| Different stocks per agent | Avoid conflicts |
| Check status regularly | Know what each agent is doing |
| Add slowly | One new agent at a time |

---

