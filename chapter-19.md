# Chapter 19: Maintenance Routine

---

> **[IMAGE PLACEHOLDER: A person doing stretches next to a calendar. One day says "Daily Check", another says "Weekly Review", another says "Monthly Health". A robot assistant hands them a checklist. Style: routine/planning illustration.]**

---

## The Daily Check (2 Minutes)

Every day, spend 2 minutes checking your system.

### Morning (Before Market Opens)

```
Show me my running agents
```

Expected answer: List of agents with "Active" status.

If an agent is missing or shows "Stopped", restart it:

```
Start my [AGENT_NAME] agent
```

### End of Day (After Market Closes)

```
What is my PnL today?
```

Write this number down. Keep a simple log:

```
Date       | PnL
-----------+------
2026-06-15 | +$27
2026-06-16 | -$15
2026-06-17 | +$42
```

---

## The Weekly Review (10 Minutes, Every Sunday)

We covered this in Chapter 13, but here is a quick reminder:

|| Step | Prompt | Time |
|------|--------|------|
| 1 | "What is my total PnL this week?" | 1 min |
| 2 | "How many trades did I make?" | 1 min |
| 3 | "What is my win rate?" | 1 min |
| 4 | "Any unusual trades or errors?" | 2 min |
| 5 | Write notes about what you learned | 5 min |

---

## The Monthly Health Check (30 Minutes, First Weekend of Each Month)

Once a month, do a deeper review:

### 1. Update Software

- Check if moomoo has an update
- Check if Hermes has an update
- Update if available

### 2. Review Strategy Performance

Show me the performance of each agent for the past 30 days

Look for:
- Which agents are profitable?
- Which agents are losing money?
- Which agents have been doing nothing?

### 3. Decide: Keep, Change, or Stop

For each agent, decide:

|| Situation | Action |
|-----------|--------|
| Profitable for 2+ months | Keep running |
| Breaking even | Keep running, maybe adjust |
| Losing money for 2+ weeks | Stop and analyze |
| No trades for 1 month | Stop (no signals = strategy not working) |

### 4. Backup Your Configurations

```
Export all my agent configurations to a backup file
```

Save this file somewhere safe (USB drive, cloud storage, email to yourself).

---

> **[IMAGE PLACEHOLDER: A monthly calendar with tasks written on different days. "1st: Update software". "7th: Weekly review". "1st of month: Monthly health check". Style: calendar planner illustration.]**

---

## Chapter 19 Summary

|| Routine | Frequency | Time |
|---------|-----------|------|
| Daily check | Every day | 2 min |
| Weekly review | Every Sunday | 10 min |
| Monthly health check | First of month | 30 min |

---
