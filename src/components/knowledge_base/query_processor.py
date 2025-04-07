class QueryProcessor:
    def __init__(self, retriever):
        self.retriever = retriever

    def format_query(self, user_query):
        # Implement logic to format the user query
        formatted_query = user_query.strip().lower()
        return formatted_query

    def execute_query(self, user_query):
        formatted_query = self.format_query(user_query)
        results = self.retriever.retrieve(formatted_query)
        return results

    def process_query(self, user_query):
        # Process the user query and return results
        results = self.execute_query(user_query)
        return results