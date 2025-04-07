from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from components.nlp.tokenizer import Tokenizer
from components.nlp.embeddings import Embeddings
from components.nlp.intent_recognition import IntentRecognizer
from components.chatbot.response_generator import ResponseGenerator
from components.chatbot.context_manager import ContextManager
from components.chatbot.dialogue_manager import DialogueManager
from components.knowledge_base.retriever import Retriever
from components.knowledge_base.updater import Updater
from components.knowledge_base.query_processor import QueryProcessor
from config.settings import DATABASE_URL, API_KEY

app = FastAPI()

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
tokenizer = Tokenizer()
embeddings = Embeddings()
intent_recognizer = IntentRecognizer()
response_generator = ResponseGenerator()
context_manager = ContextManager()
dialogue_manager = DialogueManager()
retriever = Retriever()
updater = Updater()
query_processor = QueryProcessor()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Intelligent Personalized Knowledge Assistant"}

# Additional routes can be defined here for handling user queries, intents, and responses.