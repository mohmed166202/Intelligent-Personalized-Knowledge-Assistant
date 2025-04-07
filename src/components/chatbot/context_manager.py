class ContextManager:
    def __init__(self):
        self.context = {}

    def update_context(self, user_id, key, value):
        if user_id not in self.context:
            self.context[user_id] = {}
        self.context[user_id][key] = value

    def get_context(self, user_id):
        return self.context.get(user_id, {})

    def clear_context(self, user_id):
        if user_id in self.context:
            del self.context[user_id]