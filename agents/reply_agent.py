class ReplyAgent:
    def compose(self, intent, emotion, context):

        empathy = {
            "angry": "I'm sorry you're facing this. ",
            "sad": "I understand this is disappointing. ",
            "positive": "Great! Happy to help! ",
            "neutral": ""
        }[emotion]

        templates = {
            "refund": "I can help with your refund. Please provide your order ID.",
            "cancel_subscription": "I can cancel your subscription. What's your email?",
            "order_tracking": "Please share your order number.",
            "payment_issue": "Please send your transaction ID for verification.",
            "pricing_query": "Pricing depends on the plan. Which plan are you interested in?",
            "general_query": "Could you explain a bit more?",
        }

        core = templates.get(intent, "I didn’t fully understand that.")

        return empathy + core + f" (Context: {context})"
