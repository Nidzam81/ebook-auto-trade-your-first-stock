# Chapter 7.5: Hermes Brain - Which Model to Use & How to Get Free Models

---

> **[IMAGE PLACEHOLDER: A brain illustration with "Hermes" written inside. Around it: logos of different AI models (some with "free" badges). Style: clean tech illustration.]**

---

## What Is "Hermes Brain"?

Every time you ask Hermes to do something, it needs to "think." The thinking part is done by a **Large Language Model (LLM)** -- an AI that understands your text and responds intelligently.

**Hermes Brain = the AI model that powers Hermes.**

Think of it like this:
- **Hermes** is the body (the chat interface, the tools, the memory)
- **The Model** is the brain (the intelligence that thinks and responds)

Different models have different strengths:
| Model | Strength | Cost |
|-------|----------|------|
| **GPT-4o** | Smartest, fastest | $$$ |
| **Claude Sonnet** | Great reasoning | $$ |
| **Gemini** | Good at analysis | $ |
| **Llama 3 (local)** | Free, runs on your PC | Free |
| **OpenRouter free models** | Various capabilities | Free |

---

## How to Check Your Current Model

In Hermes, type:

```
show model
```

Or check your config file at:
```
C:\Users\Nidzam\AppData\Local\hermes\config.yaml
```

You will see something like:
```yaml
model:
  default: openrouter/owl-alpha
  provider: openrouter
  model: owl-alpha
```

---

## Option 1: Free Models on OpenRouter (Easiest)

**OpenRouter** is a service that gives you access to many AI models -- including free ones.

### Step 1: Create an OpenRouter Account

1. Go to: **https://openrouter.ai**
2. Click **Sign Up** (use Google or GitHub for quick signup)
3. Once logged in, click **Keys** in the left sidebar
4. Click **Create Key**
5. Copy the API key (it looks like: `sk-or-v1-...`)

### Step 2: Add the Key to Hermes

In Hermes, type:

```
configure openrouter
```

Paste your API key when prompted.

### Step 3: Switch to a Free Model

In Hermes, type:

```
hermes config set model.model google/gemini-2.0-flash-001
```

Or for an even faster free model:

```
hermes config set model.model openrouter/auto
```

### Best Free Models on OpenRouter

| Model | Why It's Good |
|-------|---------------|
| `google/gemini-2.0-flash-001` | Fast, smart, generous free tier |
| `google/gemini-2.5-flash` | Latest Gemini, excellent reasoning |
| `meta-llama/llama-3.1-8b` | Meta's best open model |
| `openrouter/auto` | Auto-selects best available free model |

> **[IMAGE PLACEHOLDER: Screenshot of OpenRouter dashboard showing free models list with green "Free" badges. Style: annotated screenshot.]**

---

## Option 2: Run Models Locally with Ollama (100% Free, Private)

If you have a decent PC (8GB+ RAM), you can run AI models **locally** -- no internet needed, completely free, and private.

### Step 1: Install Ollama

1. Go to: **https://ollama.com**
2. Download the Windows version
3. Install it (just click Next, Next, Finish)
4. Ollama runs in the background -- you will see its icon in the system tray

### Step 2: Download a Free Model

Open a terminal and type:

```
ollama run gemma4:12b
```

This downloads the Google Gemma model (~7.6 GB). Other options:

| Model | Size | Best For |
|-------|------|----------|
| `gemma4:12b` | 7.6 GB | General purpose, coding |
| `llama3.2:latest` | 2.0 GB | Fast, good for beginners |
| `qwen2.5:latest` | 4.9 GB | Best for coding |
| `deepseek-r1:8b` | 4.9 GB | Advanced reasoning |

### Step 3: Connect Hermes to Ollama

In Hermes, configure the model:

```
hermes config set model.model ollama/gemma4:12b
```

Or for the lighter model:

```
hermes config set model.model ollama/llama3.2
```

### Step 4: Test It

In Hermes, type:

```
Say hello
```

If Ollama is running and configured correctly, the model will respond.

---

> **[IMAGE PLACEHOLDER: Diagram showing "You" -> "Hermes" -> "Ollama (on your PC)" with a shield icon around Ollama showing "Private + Free". Style: clean infographic.]**

---

## Option 3: Google Gemini (Free Tier)

Google offers a generous free tier for Gemini models.

### Step 1: Get a Google AI Key

1. Go to: **https://aistudio.google.com/apikey**
2. Sign in with your Google account
3. Click **Create API Key**
4. Copy the key

### Step 2: Configure Hermes

```
hermes config set model.provider google
hermes config set model.model google/gemini-2.0-flash-001
```

---

## Which Model Should You Choose?

| Situation | Recommended Model |
|-----------|-------------------|
| **Just starting out** | OpenRouter free tier (`openrouter/auto`) |
| **Want privacy** | Ollama with `gemma4:12b` or `llama3.2` |
| **Best quality (paid)** | GPT-4o or Claude Sonnet via OpenRouter |
| **Coding tasks** | `qwen2.5` via Ollama |
| **Low-spec PC** | `llama3.2` (2GB) via Ollama |

---

## How to Switch Models Anytime

You don't have to stick with one model. Switch anytime:

```
hermes config set model.model google/gemini-2.0-flash-001
```

Or use the interactive picker:

```
hermes model
```

This shows a list of available models. Use arrow keys to select, Enter to confirm.

---

## Important Notes

1. **Restart Hermes** after changing the model for changes to take effect
2. **Free models** may be slower during peak hours but work fine for trading tasks
3. **Local models** (Ollama) don't use internet -- great for privacy
4. **API keys** should never be shared or committed to GitHub

---

## Chapter 7.5 Summary

| Option | Cost | Privacy | Ease |
|--------|------|---------|------|
| OpenRouter free models | Free | Medium | Easiest |
| Ollama (local) | Free | Highest | Medium |
| Google Gemini free tier | Free | Medium | Easy |
| GPT-4o / Claude (paid) | $$$ | Low | Easy |

---

Now let's add backtesting to your trading strategy toolkit.

---
