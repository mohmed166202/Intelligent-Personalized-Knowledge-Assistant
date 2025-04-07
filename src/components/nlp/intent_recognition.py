class IntentRecognizer:
    def __init__(self, model):
        self.model = model
        self.intents = {}

    def train(self, training_data):
        # Code to train the model on the training data
        pass

    def predict(self, input_text):
        # Code to predict the intent of the input text
        pass

    def add_intent(self, intent_name, examples):
        # Code to add a new intent with examples
        pass

    def get_intents(self):
        return self.intents.keys()