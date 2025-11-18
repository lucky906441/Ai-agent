import re

class EmotionAgent:
    def detect(self, text):
        t = text.lower()

        if re.search(r"\b(angry|furious|upset)\b", t):
            return "angry"

        if re.search(r"\b(sad|unhappy|disappointed)\b", t):
            return "sad"

        if re.search(r"\b(thanks|thank you|great)\b", t):
            return "positive"

        return "neutral"
