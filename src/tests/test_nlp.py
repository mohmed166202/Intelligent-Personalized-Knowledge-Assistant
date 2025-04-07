import unittest
from components.nlp.tokenizer import Tokenizer
from components.nlp.embeddings import Embeddings
from components.nlp.intent_recognition import IntentRecognizer

class TestNLPComponents(unittest.TestCase):

    def setUp(self):
        self.tokenizer = Tokenizer()
        self.embeddings = Embeddings()
        self.intent_recognizer = IntentRecognizer()

    def test_tokenization(self):
        text = "Hello, how can I help you?"
        tokens = self.tokenizer.tokenize(text)
        self.assertIsInstance(tokens, list)
        self.assertGreater(len(tokens), 0)

    def test_embeddings(self):
        text_chunk = "This is a test sentence."
        embedding = self.embeddings.generate_embedding(text_chunk)
        self.assertIsInstance(embedding, list)
        self.assertEqual(len(embedding), self.embeddings.embedding_size)

    def test_intent_recognition(self):
        text = "Book a flight to New York"
        intent = self.intent_recognizer.predict_intent(text)
        self.assertIsInstance(intent, str)
        self.assertIn(intent, self.intent_recognizer.available_intents)

if __name__ == '__main__':
    unittest.main()