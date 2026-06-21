# Chapter 9: What Is a Cron Job? (Your Trading Robot's Alarm Clock)

---

> **[IMAGE PLACEHOLDER: An alarm clock ringing, with a small robot hand reaching out to press a button labeled "CHECK MARKET". The clock shows "Every 30 min". Style: cartoon.]**

---

## The Problem

Your trading agent needs to check the market regularly. But:
- You cannot watch the market 24/7
- You need to sleep, eat, live your life
- Stocks move even when you are not looking

So how does your agent check the market without you?

---

## The Solution: A Cron Job

A **cron job** is an **alarm clock for your computer**.

You set it up once. Then, at regular intervals (every 30 minutes, every hour, etc.), it automatically wakes up your agent and says: "Hey, check the market now!"

You do not need to be there. You do not need to click anything. The cron job does it for you.

---

## How It Works (Step by Step)

1. **You set up a cron job** that says: "Every 30 minutes, check NVDA's RSI"
2. **The cron job starts running** in the background
3. **30 minutes pass...**
4. The cron job wakes up and asks Hermes: "What is NVDA's RSI?"
5. Hermes checks moomoo: "NVDA RSI is 28"
6. Hermes says: "RSI is below 30. Buying!"
7. The trade is placed
8. The cron job goes back to sleep
9. **30 minutes later, it happens again**

---

> **[IMAGE PLACEHOLDER: A timeline showing 30-minute intervals. At each interval, a small icon of an eye opening (checking) and closing (sleeping). Labels: "00:00 - Check", "00:30 - Check", "01:00 - Check", "01:30 - Check". Style: timeline infographic.]**

---

## Common Cron Job Schedules

| Schedule | What It Means | Good For |
|----------|---------------|----------|
| Every 30 minutes | Checks twice an hour | Active trading (US market hours) |
| Every hour | Checks once an hour | Less active monitoring |
| Every 2 hours | Checks every 2 hours | Long-term strategies |
| Daily at 9:30 AM | Checks once at market open | End-of-day decisions |

**For beginners:** Start with **every 30 minutes** during market hours (9:30 AM - 4:00 PM Eastern Time for US market).

---

## Setting Up a Cron Job Through Hermes

Setting up a cron job is easy. You just tell Hermes what you want in plain English.

In Hermes, type something like:

```
Create a cron job that checks NVDA RSI every 30 minutes during US market hours
```

Hermes will:
1. Create the cron job for you
2. Set the schedule (every 30 minutes)
3. Set the task (check NVDA RSI)
4. Confirm that it is running

That is it. You do not need to write any code. Hermes handles everything.

---

## Cron Jobs Are Patient

Here is the beautiful thing about cron jobs: they do not get bored.

Imagine checking the market every 30 minutes, 13 times a day, for 30 days straight. That is 390 checks. You would go crazy doing that manually.

A cron job does it without complaining. Every. Single. Time.

---

## Chapter 9 Summary

| Concept | What It Means |
|---------|---------------|
| Cron job | An alarm clock for your computer |
| Schedule | How often the cron job runs (e.g., every 30 min) |
| Task | What the cron job does (e.g., check RSI) |
| Background | Runs silently while you do other things |

---

Now you understand the tools. Let's build your first trading agent!

---
