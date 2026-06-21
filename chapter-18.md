# PART 6: TROUBLESHOOTING & MAINTENANCE

---

# Chapter 18: Common Problems and Fixes

---

> **[IMAGE PLACEHOLDER: A robot mechanic with a wrench, fixing a trading robot. Sparks fly. A concerned person watches with a "Will it be okay?" expression. Style: cartoon repair scene.]**

---

## Problem #1: "Hermes Can't Connect to moomoo"

**Symptoms:** Hermes says "Connection failed" or "Cannot reach moomoo"

**Fix (in order):**

1. Is moomoo open? → Open moomoo
2. Is OpenD enabled? → Check moomoo settings → OpenD → ON
3. Is the port correct? → Check OpenD settings for the port number
4. Is the password correct? → Re-type carefully (case-sensitive)
5. Is your firewall blocking it? → Add moomoo as an exception in your antivirus
6. Restart everything: Close moomoo → Close Hermes → Open moomoo → Open Hermes

---

## Problem #2: "My Agent Stopped Running"

**Symptoms:** The agent was working yesterday but not today. No new trades.

**Fix:**

1. Check if the cron job is still active:
   ```
   Show me my cron jobs
   ```
2. If the cron job is missing, recreate it:
   ```
   Create a cron job for my NVDA-RSI agent
   ```
3. Check if Hermes is still running (it needs to be open for cron jobs to work)
4. Check if your computer went to sleep (cron jobs don't run during sleep)

---

## Problem #3: "The Dashboard Shows No Data"

**Symptoms:** You open the dashboard but it is empty.

**Fix:**

1. Make sure the agent has actually placed trades (check the trade log)
2. Refresh the dashboard:
   ```
   Refresh my trading dashboard
   ```
3. Check if the trade log file exists:
   ```
   Show me the trade log file location
   ```
4. If all else fails, recreate the dashboard:
   ```
   Recreate my trading dashboard
   ```

---

## Problem #4: "Orders Aren't Being Placed"

**Symptoms:** The agent says it wants to buy but no order appears in moomoo.

**Fix:**

1. Check if you are in SIMULATE mode (orders in SIMULATE go to the practice account, not real moomoo)
2. Check if moomoo is open
3. Check if OpenD is running (look for the icon in the system tray)
4. Check if there is enough cash (or virtual cash) in your account
5. Check if the stock is in trading hours (you cannot trade before market open or after market close)

---

> **[IMAGE PLACEHOLDER: A 5-step flowchart: "Check moomoo open? → Check OpenD? → Check port/password? → Check firewall? → Restart everything". Each step has a checkbox. Style: troubleshooting flowchart.]**

---

## Problem #5: "My PC Is Slow"

**Symptoms:** Your computer is lagging after running agents.

**Fix:**

1. Close other programs (browsers, games, etc.)
2. Check how many agents you are running (each uses some memory)
3. Stop agents you are not using:
   ```
   Stop my [AGENT_NAME] agent
   ```
4. Restart your computer once a week (this clears memory)

---

## The 5-Minute Diagnosis Checklist

When something goes wrong, go through this checklist before panicking:

| # | Check | How |
|---|-------|-----|
| 1 | Is moomoo open? | Look at your taskbar for the moomoo icon |
| 2 | Is OpenD running? | Look for the OpenD icon near your clock |
| 3 | Is Hermes open? | Look for the Hermes window |
| 4 | Is the internet working? | Try opening a website |
| 5 | Is the market open? | US market: 9:30 AM - 4:00 PM ET |

90% of problems are solved by one of these 5 checks.

---

## Chapter 18 Summary

| Problem | Most Likely Fix |
|---------|----------------|
| Can't connect | Check moomoo + OpenD are running |
| Agent stopped | Restart cron job |
| Dashboard empty | Refresh or recreate |
| No orders | Check moomoo open + OpenD running |
| PC slow | Close unused programs and agents |

---

