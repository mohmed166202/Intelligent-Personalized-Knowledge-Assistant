class ResponseGenerator:
    def __init__(self, llm_api):
        self.llm_api = llm_api

    def generate_response(self, user_input, context):
        prompt = self.create_prompt(user_input, context)
        response = self.llm_api.get_response(prompt)
        return response

    def create_prompt(self, user_input, context):
        return f"User: {user_input}\nContext: {context}\nAssistant:"