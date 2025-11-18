from agents.memory_agent import MemoryAgent
from agents.intent_agent import IntentAgent
from agents.emotion_agent import EmotionAgent
from agents.reply_agent import ReplyAgent

class Coordinator:
    def __init__(self):
        self.memory = MemoryAgent()
        self.intent = IntentAgent()
        self.emotion = EmotionAgent()
        self.reply = ReplyAgent()

    def handle(self, text):
        self.memory.store("user", text, weight=2)

        intent, confidence = self.intent.detect(text)
        emotion = self.emotion.detect(text)
        context = self.memory.context()

        reply = self.reply.compose(intent, emotion, context)
        self.memory.store("bot", reply)

        return {
            "intent": intent,
            "confidence": confidence,
            "emotion": emotion,
            "reply": reply,
            "context": context
        }

    # backward-compatible older method
    def ask(self, text):
        r = self.handle(text)
        urgency = "high" if r["confidence"] >= 0.9 else "medium"
        return {"intent": r["intent"], "urgency": urgency, "reply": r["reply"]}
