import unittest
from components.chatbot.response_generator import ResponseGenerator
from components.chatbot.context_manager import ContextManager
from components.chatbot.dialogue_manager import DialogueManager

class TestResponseGenerator(unittest.TestCase):
    def setUp(self):
        self.response_generator = ResponseGenerator()
    
    def test_generate_response(self):
        user_input = "Hello, how can I help you?"
        context = {}
        response = self.response_generator.generate_response(user_input, context)
        self.assertIsInstance(response, str)

class TestContextManager(unittest.TestCase):
    def setUp(self):
        self.context_manager = ContextManager()
    
    def test_update_context(self):
        context = {}
        new_info = {"user_name": "Alice"}
        updated_context = self.context_manager.update_context(context, new_info)
        self.assertIn("user_name", updated_context)

    def test_retrieve_context(self):
        context = {"user_name": "Alice"}
        user_name = self.context_manager.retrieve_context(context, "user_name")
        self.assertEqual(user_name, "Alice")

class TestDialogueManager(unittest.TestCase):
    def setUp(self):
        self.dialogue_manager = DialogueManager()
    
    def test_manage_dialogue_state(self):
        initial_state = "greeting"
        next_state = self.dialogue_manager.manage_dialogue_state(initial_state, "user_response")
        self.assertNotEqual(initial_state, next_state)

if __name__ == '__main__':
    unittest.main()