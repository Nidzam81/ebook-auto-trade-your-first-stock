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

|| Capability | Example |
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

|| Limitation | Why |
|-----------|-----|
| Predict the future | Nobody can. Not even AI. |
| Guarantee profits | The market is unpredictable. |
| Trade without OpenD | OpenD is the bridge. No bridge = no trade. |
| Work when your PC is off | Hermes needs your computer running. |

---

## SIMULATE vs LIVE: The Critical Difference

This is so important it gets its own section.

When Hermes connects to moomoo, it connects to one of two "environments":

|| Environment | What Happens | Risk Level |
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

|| Concept | What It Means |
|---------|---------------|
| Hermes = waiter | Takes your instructions to moomoo |
| moomoo = chef | Actually executes trades |
| OpenD = kitchen door | The bridge between them |
| SIMULATE | Practice mode, fake money, zero risk |
| LIVE | Real mode, real money, real risk |

---

Now let's understand trading strategies.

---