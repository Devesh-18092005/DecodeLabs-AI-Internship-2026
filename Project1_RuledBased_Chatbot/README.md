# 🤖 DecoBot — Rule-Based AI Chatbot

### Project 1 | Decode Labs AI Internship | Batch 2026

> *"Before you build systems that learn on their own, you must master the art of teaching a machine through explicit if-else instructions."*
> — Decode Labs Industrial Training Kit

---

## 📌 Project Overview

**DecoBot** is a Rule-Based AI Chatbot built as **Project 1** of the Decode Labs AI Internship (Batch 2026).

This project demonstrates the **Logic Engine** — the foundation of intelligent systems.
Instead of deep learning, it uses **Control Flow + Dictionary-based intent matching + Keyword Matching** to simulate human conversation with deterministic, traceable responses.

| Field        | Details                         |
| ------------ | ------------------------------- |
| **Intern**   | Devesh Marathe                  |
| **Track**    | Artificial Intelligence (AI)    |
| **Company**  | Decode Labs (`decodelabs.tech`) |
| **Mode**     | Remote / Virtual                |
| **Language** | Python 3.x                      |

---

## 🏗️ Architecture — The IPO Model

```text
INPUT  →  PROCESS  →  OUTPUT
  │           │           │
Sanitize   Intent     Response
(lower +   Matching   Generation
 strip)    + Keywords  (Formatted)
```

### Phase 1 — Input & Sanitization

```python
clean_input = raw_input.lower().strip()
```

Normalises `HeLLo`, `HELLO`, `  hello  ` → all map to the **same response**.

### Phase 2 — Intent Matching

Uses a **Python Dictionary** for fast exact-match lookup, followed by multi-word and single-word keyword matching.

```python
if clean_input in RESPONSES:
    return RESPONSES[clean_input]
```

For natural multi-word inputs, `KEYWORD_MAP` searches for known phrases:

```python
for phrase, key in sorted(KEYWORD_MAP.items(), key=lambda x: -len(x[0])):
    if phrase in clean_input:
        return RESPONSES.get(key, FALLBACK)
```

### Phase 3 — The Heartbeat (Infinite Loop)

```python
while True:
    raw_input_text = input("You: ").strip()

    if not raw_input_text:
        continue

    clean = sanitize(raw_input_text)

    if clean in EXIT_COMMANDS:
        break

    reply = get_response(raw_input_text)
    print(f"\nDecoBot: {reply}\n")
```

---

## ✅ Project 1 — Logic Skeleton Checklist

| Requirement         | Status | Implementation                            |
| ------------------- | ------ | ----------------------------------------- |
| **INPUT LOOP**      | ✅      | `while True` continuous cycle             |
| **SANITIZATION**    | ✅      | `.lower().strip()`                        |
| **KNOWLEDGE BASE**  | ✅      | `RESPONSES` dictionary with 30+ responses |
| **INTENT MATCHING** | ✅      | Exact + multi-word + single-word matching |
| **KEYWORD MAP**     | ✅      | `KEYWORD_MAP` for phrase-based matching   |
| **FALLBACK**        | ✅      | Default response for unknown inputs       |
| **EXIT STRATEGY**   | ✅      | `exit`, `quit`, `bye`, `goodbye`, `q`     |
| **ERROR HANDLING**  | ✅      | Graceful `KeyboardInterrupt` handling     |

---

## 💬 Supported Intents (30+)

| Category       | Example Inputs                                                             |
| -------------- | -------------------------------------------------------------------------- |
| 🗣️ Greetings  | `hello`, `hi`, `hey`, `good morning`, `good evening`, `good afternoon`     |
| 🤖 Identity    | `who are you`, `what are you`, `your name`                                 |
| 🧠 AI & Tech   | `what is ai`, `machine learning`, `deep learning`, `python`, `chatbot`     |
| 🏢 Decode Labs | `what is decode labs`, `internship`, `about decode labs`                   |
| 😂 Fun/Jokes   | `joke`, `tell me a joke`, `another joke`, `are you human`, `are you smart` |
| ❤️ Feelings    | `how are you`, `i am sad`, `i am bored`, `i am fine`                       |
| 🙏 Gratitude   | `thank you`, `thanks`, `great`, `nice`                                     |
| ℹ️ Help        | `help`, `topics`, `what can you do`                                        |
| 🚪 Exit        | `exit`, `quit`, `bye`, `goodbye`, `q`                                      |

---

## 🚀 How to Run

### Requirements

* Python 3.6 or above
* No external libraries required (pure Python!)

### Run the Chatbot

```bash
git clone https://github.com/DeveshAi/DecoBot-Rule-Based-Chatbot.git
cd DecoBot-Rule-Based-Chatbot
python chatbot.py
```

---

## 📂 Project Structure

```text
project1_chatbot/
│
├── chatbot.py          # Main chatbot — all logic lives here
├── README.md           # Project documentation
└── screenshots/        # Demo screenshots
```

---

## 🔬 Key Concepts Demonstrated

| Concept                   | Where Used                                       |
| ------------------------- | ------------------------------------------------ |
| **Dictionary (Hash Map)** | `RESPONSES` — fast exact intent lookup           |
| **Input Sanitization**    | `sanitize()` function                            |
| **Intent Matching**       | `match_intent()` function                        |
| **Multi-word Matching**   | `KEYWORD_MAP` longest-match scan                 |
| **Single-word Matching**  | Word-by-word fallback scan                       |
| **Infinite Loop**         | `while True` in `run_chatbot()`                  |
| **Exit Strategy**         | `EXIT_COMMANDS` set + `break`                    |
| **Fallback Logic**        | `FALLBACK` constant                              |
| **Modular Functions**     | `sanitize()`, `match_intent()`, `get_response()` |
| **Exception Handling**    | `KeyboardInterrupt`                              |

---

## 📊 Why Dictionary over If-Elif Ladder?

| Approach        | Complexity       | Maintainability | Scalability             |
| --------------- | ---------------- | --------------- | ----------------------- |
| `if-elif`       | O(n)             | ❌ High Debt    | ❌ Difficult to maintain |
| **Dict Lookup** | **O(1) average** | **✅ Clean**    | **✅ Easy to extend**    |

The `RESPONSES` dictionary provides fast exact-match lookup, while `KEYWORD_MAP` adds support for multi-word phrases and more flexible user input.

---

## 📸 Screenshots

> *See `/screenshots` folder in this repo.*

---

## 🎓 Learning Outcomes

* ✅ Built a continuous, interactive loop-based chatbot
* ✅ Applied dictionary-based intent resolution
* ✅ Implemented input sanitization using `.lower().strip()`
* ✅ Implemented multi-word keyword matching
* ✅ Added fallback handling for unknown inputs
* ✅ Implemented multiple exit commands
* ✅ Added graceful `Ctrl+C` shutdown
* ✅ Practiced modular Python function design
* ✅ Understood the fundamentals of rule-based conversational AI

---

*Project 1 of 4 — Rule-Based AI Chatbot | Decode Labs AI Internship 2026*