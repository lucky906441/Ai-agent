class IntentAgent:
    def detect(self, text):
        t = text.lower()

        rules = {
            "refund": ["refund", "money back"],
            "cancel_subscription": ["cancel", "unsubscribe"],
            "order_tracking": ["track", "order status", "where is my order"],
            "payment_issue": ["payment failed", "transaction failed", "payment"],
            "pricing_query": ["price", "cost"],
        }

        for intent, keys in rules.items():
            if any(k in t for k in keys):
                return intent, 0.9

        return "general_query", 0.5
