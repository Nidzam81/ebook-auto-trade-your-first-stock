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

|| Question | What to Enter | Example |
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

|| Check | What to Do |
|-------|-----------|
| **Is moomoo open?** | Open moomoo. OpenD only works when moomoo is running. |
| **Is OpenD enabled?** | Check moomoo settings → OpenD should be ON. |
| **Is the port correct?** | Check what port OpenD uses. It might be different. |
| **Is the password correct?** | Try again carefully. Passwords are case-sensitive. |
| **Is your firewall blocking it?** | Your antivirus might block OpenD. Add moomoo as an exception. |

**The #1 most common mistake:** Forgetting to keep moomoo running. OpenD lives inside moomoo. If you close moomoo, OpenD stops working, and Hermes cannot connect.

---

## Step 5: What You Can Now Do

Now that Hermes is connected to moomoo, you can:

|| Action | Example Prompt |
|--------|---------------|
| Check your balance | "What is my account balance?" |
| Check a stock price | "What is NVDA trading at?" |
| See your positions | "Show my current holdings" |
| Place a simulated order | "Buy 10 shares of NVDA in SIMULATE mode" |
| See your orders | "Show my open orders" |

Try each one. Get comfortable with how Hermes responds.

---

## Chapter 6 Summary

|| Step | Status |
||------|--------|
|| Loaded moomoo skill | Done |
|| Configured connection (host, port, password) | Done |
|| Tested connection with "check balance" | Done |
|| Tried at least 3 example prompts | Done |

**Congratulations!** Your computer is now set up. The boring part is over. Now we learn how the tools work and then we build your first trading agent.

---