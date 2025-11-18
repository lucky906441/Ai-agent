# 🤖 Multi-Agent Intelligent Customer Support System (Agent Shutton)

Agent Shutton is a medium-advanced multi-agent customer support system designed to deliver fast, accurate, empathetic, and context-aware assistance.  
It uses multiple specialized agents — Intent, Emotion, Memory, and Reply — all coordinated through a central brain (Coordinator Agent) to simulate a real human support representative.

This project demonstrates how multi-agent architecture can automate enterprise-level support tasks at scale.

---

## ## Project Overview — Agent Shutton

Agent Shutton is a modular AI system built specifically for **customer support automation**.  
Instead of one single model handling everything, the system breaks the task into multiple intelligent agents:

- **Intent Agent** — Understands what the user wants  
- **Emotion Agent** — Detects emotional tone  
- **Memory Agent** — Tracks conversation history  
- **Reply Agent** — Generates context-aware empathetic answers  
- **Coordinator** — Orchestrates the full pipeline  

The goal is to provide human-level support with speed, accuracy, and emotional intelligence.

![Architecture](./thumbnail.png "Optional Title")

---

# Problem Statement

Customer support teams face several recurring issues:

- Customers wait too long for help  
- Support quality varies from agent to agent  
- No tracking of previous messages or context  
- Bots reply in robotic, emotionless ways  
- High cost of training and managing human staff  
- Difficult to scale to thousands of users  

Users expect **instant, polite, emotionally aware, context-rich responses**, which most systems cannot deliver.

Manual support is slow.  
Simple chatbots are dumb.  
Businesses need something in between:

➡️ **Fast like automation  
➡️ Smart like a human**

---

# Solution Statement

Agent Shutton solves these problems using a fully modular **multi-agent architecture**.

Each agent performs one specialized job:

# 🧠 **Intent Agent**
Detects user intent such as:
- Refund request  
- Subscription cancellation  
- Payment failure  
- Order tracking  
- Pricing queries  
- General help  

# 😐 **Emotion Agent**
Understands emotional state:
- Angry  
- Sad  
- Neutral  
- Positive  

# 📝 **Memory Agent**
Stores recent conversation history with simple summarization:
- Who said what  
- Important details  
- Weighted messages (order ID, transaction ID, etc.)

# 💬 **Reply Agent**
Generates:
- Empathy  
- Accurate support messages  
- Personalized replies  
- Context-aware responses  

# 🤖 **Coordinator Agent**
Orchestrates the entire pipeline:
1. Takes user input  
2. Sends to Intent, Emotion, Memory agents  
3. Combines results  
4. Produces final human-like response  

This design ensures:
- High accuracy  
- Emotional intelligence  
- Memory and continuity  
- Clean, modular architecture  
- Realistic support automation  

---

# Architecture
![Architecture](./flow_adk_web.png "Optional Title")


---

# Essential Tools and Utilities

Your project uses the following components:

# 🔧 **Technologies**
- Python 3  
- Dataclasses  
- Regex-based parsing  
- JSON utilities  
- Lightweight, dependency-free code  

# 🔧 **Agents**
- `IntentAgent`  
- `EmotionAgent`  
- `MemoryAgent`  
- `ReplyAgent`  
- `Coordinator`  

# 🔧 Optional Expansion Tools
- FastAPI REST wrapper  
- ADK Web Mode integration  
- Logging utilities  
- Vector memory (future)  

---

# ### Value Statement

Agent Shutton provides:

- ⚡ Lightning-fast automated support  
- ❤️ Emotion-aware responses  
- 🧠 Smart intent understanding  
- 🧵 Context-maintaining memory  
- 📈 Enterprise-ready scalability  
- 💰 Reduced operational cost  
- 🤝 Consistent and polite support tone  

This system offers a real-world solution that lifts support quality and reduces cost while maintaining human-like interaction.

If I had more time, future upgrades would include:
- ML-based intent classification  
- Long-term vector memory  
- RAG-based knowledge lookup  
- Multi-language customer support  
- A unified analytics dashboard  

---

# Installation

Tested on Python 3.11+

========================================================================================


- `{
  "intent": "payment_issue",
  "emotion": "angry",
  "reply": "I'm sorry you're facing this. Please send your transaction ID. (Context: user:...)"
}
`              

# Running the Agent in ADK Web Mode
- `adk web `


# This will:

- `Launch browser interface`
- `Show agent graph`
- `Show reasoning traces`
- `Allow live chat testing`

# Project Structure

![Architecture](./Structure.png "Optional Title")

# Workflow
 The complete Agent Shutton flow:
**1.** **User sends a message**
**2.** **Coordinator** receives message
**3.** Passes to:
- `  IntentAgent`
- `  EmotionAgent`
- `  MemoryAgent`

**4.** Agents return:
   - `Detected intent`
   - `Emotional tone`
   - `Context summary`

**5.** **ReplyAgent** generates final answer
**6.** **Coordinator** sends reply back
**7.** Memory updates conversation history
**8.** Conversation continues smoothly with context and emotion-awareness
