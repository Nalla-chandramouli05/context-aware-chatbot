class ChatBot:
    def __init__(self):
        self.context = {}

    def detect_intent(self, message):
        message = message.lower()

        greetings = ["hello", "hi", "hey", "hii", "hai"]
        order_issue = ["not delivered", "late", "delay", "missing"]
        cancel = ["cancel", "stop order"]
        refund = ["refund", "money back", "return", "when can i expect", "refund status"]
        thanks = ["thanks", "thank you", "thx"]
        status = ["status", "where is my order", "track"]

        if any(word in message for word in greetings):
            return "greeting"
        elif any(word in message for word in order_issue):
            return "order_issue"
        elif any(word in message for word in cancel):
            return "cancel_order"
        elif any(word in message for word in refund):
            return "refund"
        elif any(word in message for word in status):
            return "order_status"
        elif any(word in message for word in thanks):
            return "thanks"
        elif message.isdigit():
            return "order_id"
        else:
            return "unknown"

    def respond(self, message):
        intent = self.detect_intent(message)

        # Save context (except for some cases)
        if intent not in ["order_id", "thanks", "greeting"]:
            self.context["last_intent"] = intent

        if intent == "greeting":
            return "Hello! 😊 How can I help you today?"

        elif intent == "order_issue":
            return "I understand your concern. Please share your Order ID so I can check."

        elif intent == "cancel_order":
            return "No problem. Please provide your Order ID to proceed with cancellation."

        elif intent == "refund":
            last = self.context.get("last_intent")

            if last == "refund":
                return "Your refund is being processed and will be completed within 3-5 business days."
            else:
                return "Sure! Please provide your Order ID to initiate your refund."

        elif intent == "order_status":
            return "Please provide your Order ID to check the current status of your order."

        elif intent == "order_id":
            last = self.context.get("last_intent")

            if last == "order_issue":
                return "Thanks! Your order is on the way and will arrive soon."
            elif last == "cancel_order":
                return "Your order has been cancelled successfully."
            elif last == "refund":
                return "Your refund has been initiated and will reflect in 3-5 days."
            elif last == "order_status":
                return "Your order is currently out for delivery."
            else:
                return "Order ID received. How can I assist you further?"

        elif intent == "thanks":
            return "You're welcome! 😊 Let me know if you need anything else."

        else:
            return "I'm not sure I understood that. Could you please rephrase?"

# Run chatbot
if __name__ == "__main__":
    bot = ChatBot()
    print("Bot: Hello! Welcome to Customer Support.")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Thank you! Goodbye.")
            break

        print("Bot:", bot.respond(user_input))