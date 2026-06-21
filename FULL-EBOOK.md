# Auto-Trade Your First Stock

## A Beginner's Guide to Automated Trading with Hermes & moomoo

---

> **[IMAGE PLACEHOLDER: Book cover illustration. Title "Auto-Trade Your First Stock" in bold. Subtitle "A Beginner's Guide to Automated Trading with Hermes & moomoo". A friendly robot character holds a stock chart in one hand and a moomoo phone in the other. Background: clean gradient with subtle stock chart lines. Style: professional book cover.]**

---

### By Nidzam

**Version 1.0 | June 2026**

---

## About This Book

This book is for the absolute beginner. You do not need:
- Any computer programming knowledge
- Any stock trading experience
- Any understanding of APIs, servers, or technical jargon

You only need:
- A Windows PC
- An internet connection
- A moomoo account
- Curiosity and patience

## How to Use This Book

1. **Read Chapter 1 to Chapter 9** -- these explain the concepts. No hands-on work needed.
2. **Do Chapter 3 to Chapter 6** -- these set up your computer. Follow step by step.
3. **Do Chapter 10 to Chapter 13** -- these build your first agent. Follow every step.
4. **Read Chapter 14 to Chapter 17** -- these are for later, when you are ready to expand.
5. **Keep Appendices as reference** -- come back whenever you need a prompt or definition.

## What You Will Build

By Chapter 13, you will have:
- A working automated trading agent
- A system that checks the market every 30 minutes
- A trade log that records every buy and sell
- A dashboard to see everything at a glance

## A Final Note

This book does not promise you will get rich. No honest book can.

What this book does: it gives you the tools and knowledge to build your own automated trading system. What you do with those tools is up to you.

Start with SIMULATE. Be patient. Learn from losses. Celebrate wins. And most importantly -- keep learning.
Good luck.

---

**Version**: 1.0  
**Date**: June 2026  
**Target Audience**: Absolute beginners with zero PC knowledge

---

# TABLE OF CONTENTS

## PART 1: BEFORE YOU START
- Chapter 1: What Is Automated Trading?
- Chapter 2: The Safety Rules You Must Know First

## PART 2: SETTING UP YOUR COMPUTER
- Chapter 3: Your Computer Checklist
- Chapter 4: Installing moomoo & OpenD
- Chapter 5: Installing Hermes Agent
- Chapter 6: Connecting Hermes to moomoo

## PART 3: UNDERSTANDING THE TOOLS
- Chapter 7: How Hermes Talks to moomoo
- Chapter 8: Understanding Trading Strategies
- Chapter 9: What Is a Cron Job?

## PART 4: BUILDING YOUR FIRST TRADING AGENT
- Chapter 10: Planning Your First Agent
- Chapter 11: Creating Your First Trading Agent with Hermes
- Chapter 12: Useful Prompt Examples (Your Prompt Library)
- Chapter 13: Reading Your Results

## PART 5: LEVELING UP
- Chapter 14: Running Multiple Agents at Once
- Chapter 15: Building a Dashboard
- Chapter 16: Going from SIMULATE to LIVE
- Chapter 17: Advanced Strategies

## PART 6: TROUBLESHOOTING & MAINTENANCE
- Chapter 18: Common Problems and Fixes
- Chapter 19: Maintenance Routine
- Chapter 20: Security & Safety

## APPENDICES
- Appendix A: Glossary
- Appendix B: Keyboard Shortcuts & Commands Cheat Sheet
- Appendix C: Recommended Stocks for Beginners
- Appendix D: Template Prompts Library
- Appendix E: Where to Get Help

---
# PART 1: BEFORE YOU START

---

# Chapter 1: What Is Automated Trading (And Why Should You Care?)

---

> **[IMAGE PLACEHOLDER: A person sitting on a couch watching TV, while a robot arm buys and sells stocks on a phone screen nearby. The person is relaxed, the robot is busy. Style: friendly cartoon.]**

---

## In Plain English

Imagine you have a **robot assistant** that watches the stock market 24 hours a day. It follows rules you gave it. When the rules say "BUY", it buys. When the rules say "SELL", it sells. It never gets scared. It never gets greedy. It never gets tired.

**That is automated trading.**

You are not going to sit in front of your screen all day staring at charts. You are going to tell a computer what to do, and it will do it for you -- even while you sleep.

## The Three Players in This Book

Before we start, you need to know three things. Think of them as three people working together:

---

### Player 1: moomoo (Your Broker)

moomoo is a trading app. It is where your money lives. It is where you buy and sell stocks. Think of it as your **bank account for stocks**.

You might already have moomoo on your phone. If not, we will install it in Chapter 4.

---

### Player 2: Hermes Agent (Your AI Assistant)

Hermes is a chat app -- like WhatsApp, but for talking to a computer. You type messages to Hermes in plain English. Hermes understands you and does things for you.

Think of Hermes as your **smart friend who knows everything about computers**. You say "do this", and it does it.

---

### Player 3: moomoo OpenD (The Bridge)

OpenD is a small program that sits on your computer. It connects Hermes to moomoo. Without OpenD, Hermes cannot talk to moomoo. With OpenD, Hermes can check your balance, see stock prices, and place orders.

Think of OpenD as a **phone line between two friends**.

---

> **[IMAGE PLACEHOLDER: Three characters standing in a line. "You" on the left, "Hermes" in the middle with a speech bubble saying "I'll handle it!", and "moomoo" on the right showing a stock chart. Arrows connect them. Style: simple infographic.]**

---

## How They Work Together

Here is what happens when everything is set up:

1. **You** send a message to **Hermes**: "Buy 10 shares of NVDA if the RSI drops below 30"
2. **Hermes** asks **moomoo** (through **OpenD**): "What is the current RSI of NVDA?"
3. **moomoo** replies: "The RSI is 28"
4. **Hermes** says: "RSI is below 30. Placing order to buy 10 shares of NVDA"
5. **Hermes** tells **moomoo** to buy
6. **moomoo** executes the trade
7. **Hermes** sends you a message: "Done. Bought 10 NVDA at $142.50"

All of this happens in **seconds**.

## What This Book Will Teach You

By the end of this book, you will have:

- A working automated trading system
- A trading agent that buys and sells stocks for you
- A dashboard to see your profits and losses
- The knowledge to create more agents whenever you want

## What This Book Will NOT Do

Let me be honest:

- **This is not a money printer.** You can still lose money.
- **This is not a get-rich-quick scheme.** It takes time and learning.
- **This does not guarantee profits.** No one can guarantee that.

What this book DOES: it gives you a **tool**. Like giving someone a hammer. The hammer is useful. But the person still needs to know where to swing it.

## Who This Book Is For

You are perfect for this book if:

- You have zero computer knowledge
- You have never traded a stock before
- You use moomoo (or want to start)
- You want to learn by doing, not by reading theory

## Who This Book Is NOT For

This book is NOT for you if:

- You want guaranteed profits (nobody can offer that)
- You are looking for complex hedge fund strategies (that is a different book)
- You refuse to practice with fake money first (seriously, start with SIMULATE)

---

> **[IMAGE PLACEHOLDER: A simple flowchart box1: "You are here" -> box2: "Read this book" -> box3: "Set up your system" -> box4: "Practice with SIMULATE" -> box5: "Trade with REAL money (when ready)" with arrows between each box.]**

---

## Chapter 1 Summary

| Concept | What It Means |
|---------|---------------|
| Automated trading | A computer buys and sells stocks for you based on rules |
| moomoo | Your trading app / broker |
| Hermes Agent | Your AI assistant that does things for you |
| OpenD | The bridge that connects Hermes to moomoo |

---

Now that you know what you are getting into, let's talk about safety.

---
# Chapter 2: The Safety Rules You Must Know First

---

> **[IMAGE PLACEHOLDER: A person wearing a helmet, knee pads, and elbow pads, standing at the top of a ski slope. Text overlay: "Safety First!" Style: friendly cartoon.]**

---

## Rule #1: Start with SIMULATE (Paper Trading)

This is the most important rule in this entire book.

moomoo gives you two "environments":

| Environment | What It Means | Your Money |
|-------------|---------------|------------|
| **SIMULATE** | Practice mode. Fake money. Real stock prices. | **At ZERO risk** |
| **LIVE** | Real mode. Real stock prices. Real trades. | **At REAL risk** |

When you start, **always use SIMULATE**. You get fake money (usually $1 million virtual). You trade with real stock prices. If you lose, you lose nothing. If you win, you learn.

Think of it like a flight simulator. Pilots practice on a simulator before flying a real plane. You will practice on SIMULATE before trading real money.

**How long should you practice?** At minimum, 2-4 weeks. Some people practice for 3-6 months. The longer, the better.

---

## Rule #2: Never Use Money You Can't Afford to Lose

When you finally go LIVE (real money), only use money that you can afford to lose completely. Money for rent? Don't use it. Money for food? Don't use it. Money for your kid's education? Don't use it.

Only use **extra money** -- money that would go to entertainment or savings anyway.

---

## Rule #3: Past Performance Does Not Guarantee Future Results

Just because a stock went up yesterday does not mean it will go up tomorrow. Just because your agent made money last week does not mean it will make money this week.

The stock market is unpredictable. Accept this now. It will save you a lot of stress.

---

## Rule #4: The "Don't Panic" Rule

Here is what beginners do:

1. They set up an agent
2. The agent loses $50 in one day
3. The beginner panics and turns off the agent
4. The next day, the stock goes back up
5. The beginner misses the recovery

**Do not panic.** Stock markets go up and down every day. Your agent follows rules. Let it follow the rules. Trust the process.

---

## Rule #5: Risk Management Basics (In One Page)

Risk management means "how do I protect my money?" Here are the basics:

### Never put all your money in one stock

If you have $1,000, don't put all $1,000 into one stock. Put $200 in five different stocks. If one crashes, you still have four others.

### Set a stop-loss

A stop-loss is an automatic sell order. "If the stock drops 5%, sell it automatically." This limits your losses.

### Start small

When you go LIVE, start with small amounts. $100. $200. See how it goes. Add more only when you are comfortable.

---

> **[IMAGE PLACEHOLDER: A balance scale. Left side: "RISK" (small weight). Right side: "SAFETY" (big weight). The scale tips toward safety. Style: infographic.]**

---

## The Honest Truth

Let me tell you what will probably happen:

1. You will set up your first agent
2. It will make some money in SIMULATE
3. You will get excited
4. You will go LIVE with real money
5. The market will do something unexpected
6. You will lose some money
7. You will learn from it
8. You will try again, smarter

**This is the normal process.** Every trader goes through it. You are not failing. You are learning.

---

## Chapter 2 Summary

| Rule | What It Means |
|------|---------------|
| Start with SIMULATE | Practice with fake money first |
| Never risk rent money | Only use extra money |
| Past != future | The market is unpredictable |
| Don't panic | Trust your rules, not your emotions |
| Risk management | Diversify, set stop-losses, start small |

---

Now that you know the safety rules, let's set up your computer.

---
# PART 2: SETTING UP YOUR COMPUTER

---

# Chapter 3: Your Computer Checklist

---

> **[IMAGE PLACEHOLDER: A desk with a computer, keyboard, mouse, and a cup of coffee. Items are labeled: "Windows PC", "Internet", "moomoo account". Style: clean illustration.]**

---

## What You Need

Before we install anything, let's make sure you have everything:

### Hardware (The Physical Stuff)

| Item | What to Check | Minimum Requirement |
|------|---------------|---------------------|
| **Computer** | A Windows laptop or desktop | Windows 10 or newer |
| **Internet** | WiFi or Ethernet cable | Stable connection (not choppy) |
| **Disk Space** | Free space on your hard drive | At least 5 GB free |
| **RAM** | Your computer's memory | 4 GB minimum (8 GB better) |

### Accounts (The Login Stuff)

| Account | How to Get It | Do You Have It? |
|---------|---------------|-----------------|
| **moomoo account** | Download moomoo app and sign up | ☐ Yes / ☐ No |
| **moomoo OpenD** | Comes with moomoo (we'll enable it) | ☐ Yes / ☐ No |

---

## How to Check Your Windows Version

1. Press the **Windows key** on your keyboard (it looks like a little flag, usually near the bottom-left)
2. Type **"About"** or **"About your PC"**
3. Press **Enter**
4. Look for **"Edition"** and **"Version"**

You should see something like:
- Windows 10 Home (Version 22H2) ✅
- Windows 11 Pro (Version 23H2) ✅

If you see Windows 7 or XP... this book won't work. You need at least Windows 10.

---

## Creating Your Trading Folder

Let's create one folder where everything trading-related will live. This keeps things organized.

**Step-by-step:**

1. Double-click on **"This PC"** on your desktop
2. Double-click on your **C:** drive (your main hard drive)
3. Right-click in the empty space
4. Click **"New"** → **"Folder"**
5. Name it: **Trading**

That's it. Everything we create in this book will go inside the `C:\Trading` folder.

---

> **[IMAGE PLACEHOLDER: Screenshot-style illustration of Windows Explorer showing C:\Trading folder created. Arrow points to it with label "Your new folder goes here". Style: clean screenshot mockup.]**

---

## Chapter 3 Summary

| Requirement | Status |
|-------------|--------|
| Windows 10+ | ☐ Checked |
| Internet connection | ☐ Checked |
| 5 GB disk space | ☐ Checked |
| moomoo account | ☐ Checked |
| C:\Trading folder created | ☐ Done |

---

Ready? Let's install moomoo and OpenD.

---
# Chapter 4: Installing moomoo & OpenD

---

> **[IMAGE PLACEHOLDER: A hand clicking a "Download" button on a website. The moomoo logo is visible. Style: friendly illustration with arrows.]**

---

## Step 1: Download moomoo

1. Open your web browser (Chrome, Edge, Firefox -- any will work)
2. Go to: **https://www.moomoo.com/**
3. Click the **"Download"** button (usually at the top right or center of the page)
4. Download the **Windows desktop version** (not the mobile app)
5. Wait for the download to finish (usually takes 1-2 minutes)

---

## Step 2: Install moomoo

1. Find the downloaded file (usually in your **Downloads** folder)
   - The file name looks like: `moomoo-setup-xxx.exe`
2. **Double-click** the file
3. If Windows asks "Do you want to allow this app to make changes?" → Click **Yes**
4. Follow the installation wizard:
   - Click **Next**
   - Accept the terms (check the box, click Next)
   - Choose install location (just leave it as default)
   - Click **Install**
5. Wait for installation to finish (1-3 minutes)
6. Click **Finish**

---

## Step 3: Log Into moomoo

1. Open moomoo from your desktop (double-click the icon)
2. Log in with your account
   - If you don't have an account yet, click **Sign Up** and follow the steps
3. You should now see the moomoo main screen with stock prices and charts

---

> **[IMAGE PLACEHOLDER: The moomoo desktop app interface with labels pointing to: 1) Stock prices, 2) Charts, 3) Your portfolio, 4) Account balance. Style: annotated screenshot.]**

---

## Step 4: What Is OpenD and Why You Need It

Remember from Chapter 1: **OpenD is the bridge** between Hermes and moomoo.

Without OpenD, Hermes cannot see your account balance, cannot check stock prices, and cannot place trades. OpenD is like the **phone line** that lets Hermes call moomoo.

OpenD comes **inside** the moomoo desktop app. You just need to enable it.

---

## Step 5: Enable OpenD in moomoo

1. In the moomoo desktop app, look for **Settings** (usually a gear icon ⚙️)
2. Click on **Settings**
3. Look for **"OpenD"** or **"API Settings"** or **"Developer Access"**
4. **Turn ON** OpenD
5. Note down the **Port Number** (usually something like `18888` or similar)
6. Set a **Password** if prompted (write this down somewhere safe)

---

> **[IMAGE PLACEHOLDER: moomoo settings screen with a big green arrow pointing to the OpenD toggle switch in the "ON" position. Style: annotated screenshot.]**

---

## Step 6: Verify OpenD Is Running

1. Look at the bottom-right of your screen (the system tray, near the clock)
2. You should see a small **moomoo icon** or **OpenD icon**
3. If you see it, OpenD is running ✅
4. If you don't see it, go back to moomoo and make sure OpenD is enabled

---

## Common Installation Problems

| Problem | Solution |
|---------|----------|
| "Download failed" | Check your internet connection. Try again. |
| "Installation stuck" | Wait 5 minutes. If still stuck, restart your computer and try again. |
| "Can't find OpenD settings" | Make sure you have the latest version of moomoo. Update and try again. |
| "OpenD won't start" | Restart moomoo. Check if your firewall is blocking it. |
| "Forgot my password" | Use the "Forgot Password" link on the moomoo login screen. |

---

## Chapter 4 Summary

| Step | Status |
|------|--------|
| Downloaded moomoo | ☐ Done |
| Installed moomoo | ☐ Done |
| Logged into moomoo | ☐ Done |
| Enabled OpenD | ☐ Done |
| Verified OpenD is running | ☐ Done |

---

Now let's install Hermes Agent.

---
# Chapter 5: Installing Hermes Agent

---

> **[IMAGE PLACEHOLDER: A friendly robot character waving hello with a speech bubble saying "Hi! I'm Hermes!" Style: cartoon mascot.]**

---

## What Is Hermes Agent (One More Time)

Hermes Agent is a **chat app**. But instead of chatting with a person, you chat with an AI.

You type: "Check my moomoo account balance"

Hermes replies: "Your account balance is $1,000,000 (SIMULATE)"

That's it. It is a chat app. If you have ever used WhatsApp or Telegram, you already know how to use Hermes.

---

## Step 1: Download Hermes Agent

1. Open your web browser
2. Go to: **https://hermes-agent.nousresearch.com**
3. Look for the **Download** button
4. Download the **Windows version**
5. Wait for the download to finish

---

## Step 2: Install Hermes Agent

1. Find the downloaded file (in your **Downloads** folder)
2. **Double-click** the installer
3. If Windows asks "Do you want to allow this app to make changes?" → Click **Yes**
4. Follow the installation wizard:
   - Click **Next**
   - Accept the terms
   - Click **Install**
5. Wait for installation to finish
6. Click **Finish**

---

## Step 3: Run Hermes for the First Time

1. Open Hermes Agent from your desktop (double-click the icon)
2. You will see a **chat window** -- it looks like a messaging app
3. On the left: a list of conversations (empty for now)
4. On the right: the chat area (also empty)
5. At the bottom: a **text box** where you type messages

---

> **[IMAGE PLACEHOLDER: Hermes Agent interface with labels: 1) Conversation list (left sidebar), 2) Chat area (center), 3) Text input box (bottom), 4) Send button. Style: annotated screenshot.]**

---

## Step 4: Your First Conversation

Let's test it. In the text box at the bottom, type:

```
Hello
```

Press **Enter** or click the **Send** button.

Hermes will reply with something like:

```
Hello! I'm Hermes, your AI assistant. How can I help you today?
```

Congratulations. You just had your first conversation with your AI assistant.

---

## Step 5: Understanding the Interface

Here is what you need to know about the Hermes interface:

| Part | What It Does |
|------|-------------|
| **Left sidebar** | Shows your conversations. Each agent you create gets its own conversation. |
| **Chat area** | Where you and Hermes talk. Your messages on the right, Hermes' replies on the left. |
| **Text box** | Where you type your messages and commands. |
| **Settings** | Usually accessible from the top menu or a gear icon. |

---

## Common Installation Problems

| Problem | Solution |
|---------|----------|
| "Hermes won't open" | Restart your computer. Try opening again. |
| "Hermes is slow" | Close other programs. Hermes needs some memory to work. |
| "I can't find the download link" | Go to hermes-agent.nousresearch.com directly. |
| "Error during installation" | Make sure you have at least 2 GB of free disk space. |

---

## Chapter 5 Summary

| Step | Status |
|------|--------|
| Downloaded Hermes Agent | ☐ Done |
| Installed Hermes Agent | ☐ Done |
| Opened Hermes for the first time | ☐ Done |
| Sent my first "Hello" message | ☐ Done |

---

Now let's connect Hermes to moomoo. This is the exciting part.

---
# Chapter 6: Connecting Hermes to moomoo

---

> **[IMAGE PLACEHOLDER: Two puzzle pieces coming together. One piece has "Hermes" on it, the other has "moomoo" on it. They click together. Style: clean icon illustration.]**

---

## The Concept (Keep It Simple)

Right now, Hermes is just a chat app. It cannot see your moomoo account. It cannot check stock prices. It cannot place trades.

We need to **connect** Hermes to moomoo. The connection goes through **OpenD** (which we enabled in Chapter 4).

Think of it like plugging in a phone line. Hermes is the phone. moomoo is the other phone. OpenD is the cable connecting them.

---

## Step 1: Load the Moomoo Skill in Hermes

Hermes uses **skills** -- like apps on a phone -- to know how to talk to different services. We need to load the moomoo skill.

In Hermes, type this message:

```
load skill moomoo
```

Hermes will reply confirming that the moomoo skill is now active.

---

## Step 2: Configure the Connection

Now we need to tell Hermes how to reach OpenD (the bridge). Type:

```
configure moomoo connection
```

Hermes will ask you a few questions. Answer them based on your OpenD settings:

| Question | What to Enter | Example |
|----------|---------------|---------|
| **Host** | The address of your computer | `localhost` or `127.0.0.1` |
| **Port** | The port number you saw in Chapter 4 | `18888` |
| **Password** | The password you set in Chapter 4 | Your password here |
| **Environment** | SIMULATE or REAL | **SIMULATE** (always start here!) |

---

> **[IMAGE PLACEHOLDER: A form-style illustration with fields: Host = localhost, Port = 18888, Password = *****, Environment = SIMULATE. A button says "Connect". Style: clean UI mockup.]**

---

## Step 3: Test the Connection

Now let's see if Hermes can actually talk to moomoo. Type:

```
check moomoo balance
```

If everything is set up correctly, Hermes will reply with your account balance. In SIMULATE mode, it will show a virtual balance (like $1,000,000).

---

> **[IMAGE PLACEHOLDER: Hermes chat showing two messages. User: "check moomoo balance" -> Hermes: "Your SIMULATE account balance is $1,000,000". Style: chat screenshot mockup.]**

---

## Step 4: If It Does NOT Work

If Hermes says "Cannot connect" or "Connection failed", don't panic. Go through this checklist:

| Check | What to Do |
|-------|-----------|
| **Is moomoo open?** | Open moomoo. OpenD only works when moomoo is running. |
| **Is OpenD enabled?** | Check moomoo settings → OpenD should be ON. |
| **Is the port correct?** | Check what port OpenD uses. It might be different. |
| **Is the password correct?** | Try again carefully. Passwords are case-sensitive. |
| **Is your firewall blocking it?** | Your antivirus might block OpenD. Add moomoo as an exception. |

---

**The #1 most common mistake:** Forgetting to keep moomoo running. OpenD lives inside moomoo. If you close moomoo, OpenD stops working, and Hermes cannot connect.

---

## Step 5: What You Can Now Do

Now that Hermes is connected to moomoo, you can:

| Action | Example Prompt |
|--------|---------------|
| Check your balance | "What is my account balance?" |
| Check a stock price | "What is NVDA trading at?" |
| See your positions | "Show my current holdings" |
| Place a simulated order | "Buy 10 shares of NVDA in SIMULATE mode" |
| See your orders | "Show my open orders" |

Try each one. Get comfortable with how Hermes responds.

---

## Chapter 6 Summary

| Step | Status |
|------|--------|
| Loaded moomoo skill | Done |
| Configured connection (host, port, password) | Done |
| Tested connection with "check balance" | Done |
| Tried at least 3 example prompts | Done |

---

**Congratulations!** Your computer is now set up. The boring part is over. Now we learn how the tools work and then we build your first trading agent.

---
# PART 3: UNDERSTANDING THE TOOLS

---

# Chapter 7: How Hermes Talks to moomoo

---

> **[IMAGE PLACEHOLDER: A restaurant analogy. "You" is a customer. "Hermes" is the waiter. "moomoo" is the chef in the kitchen. Arrows: You -> Hermes ("I want NVDA") -> moomoo ("Order up!") -> Hermes -> You ("Order done!"). Style: cartoon analogy illustration.]**

---

## The Waiter Analogy

Imagine you are at a restaurant.

- **You** are the customer. You know what you want to eat.
- **The waiter** takes your order, brings it to the kitchen, and brings your food back.
- **The chef** (in the kitchen) actually cooks the food. You cannot talk to the chef directly.

In automated trading:

- **You** are the investor. You know what you want to buy.
- **Hermes** is the waiter. It takes your instructions to the market.
- **moomoo** is the chef. It actually executes the trades. You cannot talk to moomoo directly.

**OpenD** is the kitchen door. It is the opening through which the waiter passes orders to the chef.

---

## What Hermes CAN Do

| Capability | Example |
|-----------|---------|
| Check your account balance | "How much money do I have?" |
| Check stock prices | "What is AAPL trading at?" |
| See your current holdings | "What stocks do I own?" |
| Place buy orders | "Buy 5 shares of NVDA" |
| Place sell orders | "Sell 3 shares of NVDA" |
| See your trade history | "Show me my trades today" |
| Scan for opportunities | "Find stocks with unusual volume" |
| Create trading agents | "Create an agent for NVDA" |

---

## What Hermes CANNOT Do

| Limitation | Why |
|-----------|-----|
| Predict the future | Nobody can. Not even AI. |
| Guarantee profits | The market is unpredictable. |
| Trade without OpenD | OpenD is the bridge. No bridge = no trade. |
| Work when your PC is off | Hermes needs your computer running. |

---

## SIMULATE vs LIVE: The Critical Difference

This is so important it gets its own section.

When Hermes connects to moomoo, it connects to one of two "environments":

| Environment | What Happens | Risk Level |
|-------------|-------------|------------|
| **SIMULATE** | Orders go to a fake account. Real stock prices, fake money. | **ZERO risk** |
| **LIVE** | Orders go to your real account. Real stock prices, real money. | **REAL risk** |

**Always start with SIMULATE.** Always. No exceptions.

Think of SIMULATE as a video game. You play the game with real rules (real stock prices) but fake money. If you lose, nothing bad happens. If you win, you learn that your strategy works.

Only switch to LIVE when:
1. Your SIMULATE agent has been profitable for at least 1 month
2. You understand the strategy completely
3. You are ready to lose real money

---

> **[IMAGE PLACEHOLDER: Two doors side by side. Left door: green, labeled "SIMULATE - Practice Mode - No Risk". Right door: red, labeled "LIVE - Real Money - Real Risk". A person stands at the green door. Style: decision illustration.]**

---

## Chapter 7 Summary

| Concept | What It Means |
|---------|---------------|
| Hermes = waiter | Takes your instructions to moomoo |
| moomoo = chef | Actually executes trades |
| OpenD = kitchen door | The bridge between them |
| SIMULATE | Practice mode, fake money, zero risk |
| LIVE | Real mode, real money, real risk |

---

Now let's understand trading strategies.

---
# Chapter 8: Understanding Trading Strategies

---

> **[IMAGE PLACEHOLDER: A recipe book open on a table. One page says "Recipe: RSI Strategy" with ingredients like "RSI < 30 = BUY". Another page says "Recipe: EMA Crossover". Style: warm illustration.]**

---

## What Is a Trading Strategy?

A trading strategy is simply a **set of rules** that tells you:
- **When to buy** a stock
- **When to sell** a stock

That's it. It is like a recipe. A recipe tells you what ingredients to use and when to add them. A strategy tells you what signals to look for and when to act.

In this chapter, we will learn three simple strategies. These are proven, time-tested approaches that work well for beginners.

---

## Strategy #1: RSI (Buy When Cheap, Sell When Expensive)

### The Story

Imagine you are at a fruit market. Apples are normally $1 each.

One day, the seller puts apples on sale for $0.50 each. That is cheap! You buy a lot.

The next day, apples are $2 each. That is expensive! You sell what you bought.

**That is RSI in a nutshell.**

RSI stands for **Relative Strength Index**. It is a number from 0 to 100 that tells you if a stock is "cheap" or "expensive" right now.

| RSI Value | What It Means | Action |
|-----------|---------------|--------|
| Below 30 | Stock is "oversold" (cheap, like a sale) | **BUY** |
| Between 30-70 | Normal range | **WAIT** |
| Above 70 | Stock is "overbought" (expensive) | **SELL** |

---

> **[IMAGE PLACEHOLDER: A thermometer-style gauge. Bottom (blue) = "Below 30 = BUY (Cheap!)". Middle (green) = "30-70 = WAIT". Top (red) = "Above 70 = SELL (Expensive!)". Style: clean infographic gauge.]**

---

### Example

1. NVDA stock has an RSI of 25 (below 30)
2. Your agent sees this and says: "RSI is below 30. Time to buy!"
3. Agent buys 10 shares of NVDA
4. Two weeks later, RSI goes to 75 (above 70)
5. Agent says: "RSI is above 70. Time to sell!"
6. Agent sells 10 shares of NVDA
7. You profit from the difference

---

## Strategy #2: Moving Average Crossover (The Trend Follower)

### The Story

Imagine you are watching a river. Sometimes the water flows fast, sometimes slow. You want to know: is the river flowing faster or slower than usual?

A **moving average** is like the "usual speed" of a river. It smooths out the daily ups and downs to show you the overall direction.

If today's speed is faster than the usual speed, the river is speeding up. If today's speed is slower, the river is slowing down.

In stocks:
- **Today's price** = today's river speed
- **Moving average** = usual river speed

| Signal | What Happens | Action |
|--------|-------------|--------|
| Price crosses ABOVE moving average | Stock is speeding up (bullish) | **BUY** |
| Price crosses BELOW moving average | Stock is slowing down (bearish) | **SELL** |

---

> **[IMAGE PLACEHOLDER: A line chart showing a stock price line (wavy) and a moving average line (smoother). An arrow points to where the price line crosses above the average line with label "BUY signal". Another arrow points to a cross below with label "SELL signal". Style: clean chart illustration.]**

---

## Strategy #3: Bollinger Bands (Buy at the Bottom, Sell at the Top)

### The Story

Imagine a rubber band. When you stretch it, it wants to snap back. Stocks work similarly.

**Bollinger Bands** draw three lines on a chart:
- **Middle line**: The average price
- **Upper band**: The "stretched too high" line
- **Lower band**: The "stretched too low" line

| Signal | What Happens | Action |
|--------|-------------|--------|
| Price touches the LOWER band | Stock is stretched too low (cheap) | **BUY** |
| Price touches the UPPER band | Stock is stretched too high (expensive) | **SELL** |

---

> **[IMAGE PLACEHOLDER: A stock chart with three parallel bands (like a channel). Price line bounces off the lower band with a green "BUY" arrow, then later hits the upper band with a red "SELL" arrow. Style: clean chart illustration.]**

---

## Which Strategy Should You Choose?

| Strategy | Best For | Difficulty |
|----------|----------|------------|
| **RSI** | Stocks that go up and down a lot | ⭐ Easy |
| **EMA Crossover** | Stocks with clear trends | ⭐⭐ Medium |
| **Bollinger Bands** | Stocks that bounce in a range | ⭐⭐ Medium |

**My recommendation for beginners:** Start with **RSI**. It is the easiest to understand and works well for most stocks.

---

## Why Simple Is Better

You might think: "If simple strategies work, why do people create complex ones?"

The answer: **complex strategies often fail.**

Here is why:
- Complex strategies have more things that can break
- Simple strategies are easier to follow
- Simple strategies are harder to mess up
- A simple strategy you follow is better than a complex strategy you abandon

Start simple. Add complexity only when you are comfortable.

---

## Chapter 8 Summary

| Strategy | Buy Signal | Sell Signal | Difficulty |
|----------|-----------|-------------|------------|
| RSI | RSI below 30 | RSI above 70 | ⭐ Easy |
| EMA Crossover | Price crosses above average | Price crosses below average | ⭐⭐ Medium |
| Bollinger Bands | Price hits lower band | Price hits upper band | ⭐⭐ Medium |

---

Now let's learn about cron jobs -- the alarm clock for your trading robot.

---
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
| Time     | Agent   | Side | Qty | Price  | Entry | PnL
| 10:00 AM | NVDA-RSI| BUY  | 10  | $142.50| $142.50| --
| 2:30 PM  | NVDA-RSI| SELL | 10  | $145.20| $142.50| +$27.00
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

# Chapter 15: Building a Dashboard (See Everything at a Glance)

---

> **[IMAGE PLACEHOLDER: A large monitor screen showing a dashboard with cards, charts, and numbers. A person sits back and looks at it comfortably. Style: clean tech illustration.]**

---

## What Is a Dashboard?

A **dashboard** is a web page that shows you everything about your trading in one place. Think of it like the dashboard of a car -- it shows your speed, fuel, and engine status all in one view.

A trading dashboard shows you:
- Your account balance
- All your agents and their status
- Today's trades
- Profit and loss
- Charts of your performance

---

## Creating Your Dashboard

In Hermes, type:

```
Create a trading dashboard for all my agents
```

Hermes will:
1. Generate a web page (HTML file) with your trading data
2. Set it up to auto-refresh
3. Give you a URL (web address) to access it

---

> **[IMAGE PLACEHOLDER: A browser window showing the dashboard. Sections: "Account Balance", "Active Agents", "Today's PnL", "Trade Log", "Performance Chart". Style: annotated screenshot.]**

---

## What You Will See on the Dashboard

### Section 1: Account Overview
- Total account balance
- Cash available
- Total value of holdings

### Section 2: Agent Cards
- One card per agent
- Shows: stock, strategy, PnL, status (active/stopped)

### Section 3: Trade Log Table
- Recent trades with all details
- Green for profits, red for losses

### Section 4: Performance Chart
- A line graph showing your total PnL over time
- See if you are trending up or down

---

## Accessing Your Dashboard

After Hermes creates the dashboard, you can access it from:
- Your computer's browser
- Your phone's browser
- Any device connected to the internet (if you set it up that way)

Just type the URL Hermes gives you into the browser's address bar.

---

## Customizing Your Dashboard

You can change what the dashboard shows. Examples:

```
Show only US stocks on the dashboard
```

```
Add a section for KLSE stocks
```

```
Make the dashboard refresh every 60 seconds
```

```
Show my NVDA agent's trades in a separate section
```

---

## Chapter 15 Summary

| Feature | What It Does |
|---------|-------------|
| Account overview | See your total money at a glance |
| Agent cards | See each agent's status and PnL |
| Trade log | See recent trades |
| Performance chart | See your growth over time |
| Auto-refresh | Dashboard updates automatically |

---

# Chapter 16: Going from SIMULATE to LIVE (The Big Step)

---

> **[IMAGE PLACEHOLDER: A person standing at a diving board looking down at a pool. The pool has "REAL MONEY" written at the bottom. They look nervous but determined. A robot lifeguard stands nearby giving a thumbs up. Style: supportive cartoon.]**

---

## The Big Moment

You have been practicing in SIMULATE. Your agent is profitable. You understand the strategy. Now you are thinking: "Should I go LIVE?"

This chapter helps you decide.

---

## The Honest Checklist

Answer these questions honestly. You need **ALL** of them to be "Yes" before going LIVE.

| Question | Yes / No |
|----------|----------|
| Has my SIMULATE agent been profitable for at least 1 month? | ☐ |
| Do I understand exactly what the agent does and why? | ☐ |
| Am I prepared to lose real money? | ☐ |
| Am I using only "extra" money (not rent/food money)? | ☐ |
| Have I tested the agent in different market conditions? | ☐ |
| Do I have a plan for if things go wrong? | ☐ |

If you have even one "No", stay in SIMULATE longer. There is no rush.

---

## The Psychology Shift

Here is what nobody tells you: **SIMULATE and LIVE feel completely different.**

In SIMULATE:
- You lose $100 → "Oh well, it's fake money" → No emotion
- You make $100 → "Cool, fake money" → No emotion

In LIVE:
- You lose $100 → "That is MY REAL MONEY" → Panic
- You make $100 → "I am a genius!" → Overconfidence

Both panic and overconfidence lead to bad decisions. Going LIVE requires **emotional control**.

---

## How to Switch an Agent from SIMULATE to LIVE

When you are ready, in Hermes:

```
Switch my NVDA-RSI agent from SIMULATE to LIVE mode
```

Hermes will:
1. Confirm that you really want to do this
2. Change the environment setting
3. Restart the agent in LIVE mode
4. Confirm it is running

---

## The "Go LIVE" Rules

### Rule 1: Start Small

For your first LIVE trade, use a **small amount of money**. Maybe $100. Maybe $200. Not your entire account.

### Rule 2: One Agent Only

Do not switch all your agents to LIVE at once. Switch one. See how it goes. Then consider adding more.

### Rule 3: Set a Stop-Loss

A stop-loss is an automatic safety net. "If I lose 5%, sell automatically."

```
Set a 5% stop-loss on all my LIVE positions
```

### Rule 4: Monitor Closely (At First)

For the first week after going LIVE, check your agent multiple times a day. Make sure everything is working correctly.

### Rule 5: Do Not Panic

The first loss will hurt. Remember: a loss is normal. Do not turn off the agent after one bad day.

---

> **[IMAGE PLACEHOLDER: A shield with "GO LIVE RULES" written on it. Five points around it: "Start Small", "One Agent", "Stop-Loss", "Monitor", "Don't Panic". Style: shield/badge illustration.]**

---

## The "I Just Went LIVE" Monitoring Routine

For your first 2 weeks going LIVE:

| Time | What to Do |
|------|-----------|
| Morning (before market) | Check agent status. Is it running? |
| Midday | Quick check. Any trades? Any errors? |
| End of day | Review today's PnL. Write it down. |
| Weekly | Full review. Compare to SIMULATE performance. |

After 2 weeks, if everything is smooth, you can reduce monitoring to once a day.

---

## When to Go Back to SIMULATE

If any of these happen, switch back to SIMULATE immediately:

- You lose more than 10% of your LIVE capital
- The agent behaves unexpectedly
- You feel stressed or panicked
- Major market news disrupts your strategy

There is no shame in going back to SIMULATE. It is the smart move.

---

## Chapter 16 Summary

| Step | When to Do It |
|------|--------------|
| Complete the honest checklist | Before going LIVE |
| Switch one agent to LIVE | When all checklist items are "Yes" |
| Start small ($100-$200) | First LIVE trade |
| Set stop-loss | Before first trade |
| Monitor closely | First 2 weeks |
| Review weekly | Ongoing |

---

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
-----------+-------
2026-06-15 | +$27
2026-06-16 | -$15
2026-06-17 | +$42
```

---

## The Weekly Review (10 Minutes, Every Sunday)

We covered this in Chapter 13, but here is a quick reminder:

| Step | Prompt | Time |
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

```text
Show me the performance of each agent for the past 30 days
```

Look for:
- Which agents are profitable?
- Which agents are losing money?
- Which agents have been doing nothing?

### 3. Decide: Keep, Change, or Stop

For each agent, decide:

| Situation | Action |
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

| Routine | Frequency | Time |
|---------|-----------|------|
| Daily check | Every day | 2 min |
| Weekly review | Every Sunday | 10 min |
| Monthly health check | First of month | 30 min |

---

# Chapter 20: Security & Safety

---

> **[IMAGE PLACEHOLDER: A vault door with "Your Trading System" written on it. A robot guard stands next to it holding a key. A padlock icon floats above. Style: security illustration.]**

---

## Why Security Matters

Your trading system has access to:
- Your moomoo account (your money)
- Your stock positions
- Your personal information

You need to protect these from:
- Hackers
- Accidental mistakes
- Malware on your computer

---

## Rule #1: Protect Your Credentials

**Credentials** = your usernames, passwords, and API keys.

| Do This | NOT This |
|---------|----------|
| Keep passwords in a safe place | Write passwords on sticky notes |
| Use unique passwords | Use the same password everywhere |
| Share passwords with NO ONE | Share passwords "just in case" |
| Change passwords every 3 months | Keep the same password forever |

---

## Rule #2: Never Share Your API Keys

API keys are like master keys to your account. If someone has your API key, they can:
- See your account balance
- Place trades without your permission
- Withdraw money (in extreme cases)

**Never share your API key with anyone.** Not in emails. Not in chat. Not on forums. Not with "support staff" who message you first.

**Real support staff will NEVER ask for your API key.**

---

## Rule #3: The "Kill Switch"

A kill switch is a way to **stop everything immediately** if something goes wrong.

Your kill switch is simple:

```
Stop all trading agents immediately
```

Memorize this prompt. Practice typing it. If something goes wrong -- an agent is placing weird orders, your PC is acting strange, you suspect a hack -- type this immediately.

After stopping everything, you can investigate calmly.

---

## Rule #4: Back Up Your Agent Configurations

If your computer crashes or you accidentally delete something, you want to be able to restore your agents quickly.

```
Export all my agent configurations to C:\Trading\backup\
```

Do this monthly (see Chapter 19). Keep the backup on a USB drive or cloud storage.

---

## Rule #5: Keep Your Computer Safe

| Action | Why |
|--------|-----|
| Install antivirus software | Protects against malware |
| Keep Windows updated | Patches security holes |
| Don't click suspicious links | Prevents phishing attacks |
| Use a password manager | Stores passwords securely |
| Lock your PC when away | Prevents physical access |

---

> **[IMAGE PLACEHOLDER: A shield checklist with 5 items: "☐ Protect credentials", "☐ Hide API keys", "☐ Know the kill switch", "☐ Backup configs", "☐ Secure computer". All checked. Style: badge checklist illustration.]**

---

## What to Do If You Suspect Unauthorized Access

1. **Immediately:** Stop all agents
   ```
   Stop all trading agents immediately
   ```
2. **Change your moomoo password** (from the moomoo app or website)
3. **Change your OpenD password**
4. **Check your trade history** for any unauthorized trades
5. **Contact moomoo support** if you see suspicious activity
6. **Change your Hermes password** as well

---

## Chapter 20 Summary

| Rule | Action |
|------|--------|
| Protect credentials | Keep passwords safe, change regularly |
| Hide API keys | Never share with anyone |
| Know the kill switch | "Stop all trading agents immediately" |
| Backup configs | Monthly export to safe location |
| Secure your computer | Antivirus, updates, no suspicious links |

---

You have completed Part 6. You now know how to troubleshoot problems, maintain your system, and keep it secure.

---
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
