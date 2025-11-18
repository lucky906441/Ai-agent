from coordinator import Coordinator
import json

bot = Coordinator()

tests = [
    "My payment failed and I'm angry!",
    "I want to cancel my subscription.",
    "Where is my order?",
    "Thanks for your help!",
]

for t in tests:
    print("USER:", t)
    print(json.dumps(bot.handle(t), indent=2))
    print("-" * 40)
