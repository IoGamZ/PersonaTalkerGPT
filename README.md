<h1>PersonalTalkerGPT</h1>

A lightweight Python-based AI chatbot built using Groq's API and the Llama 3.1 8B Instant model. This project explores how to interact with Large Language Models (LLMs) through API integration while experimenting with response generation, temperature settings, custom AI personalities, and conversational memory.

This project focuses on understanding the fundamentals of working with existing AI models rather than training a language model from scratch.

Furthermore, this project started off from CMKL AiCE warp camp 2026, under one of their courses provided. However this project is a advance of what I've learnt during the courses with alterations and improvements. Taking inspiration and learning off of the course.

<h2>Highlights</h2>

Groq API Integration – Connects to Groq's API to access and interact with hosted language models.

Llama 3.1 8B Instant – Uses Meta's Llama 3.1 8B Instant model for generating AI responses.

Interactive Chatbot – Allows users to enter questions and receive AI-generated responses directly through the terminal.

Temperature Experimentation – Explores how temperature settings influence response randomness, creativity, and consistency.

Custom AI Personality – Implements system prompts to give the chatbot a predefined personality and response style.

Conversational Memory – Maintains conversation history by storing previous user messages and AI responses.

Model Flexibility – Allows the model and AI provider to be changed through configuration.

<h2>Overview</h2>

PersonalTalkerGPT is an experimental AI chatbot designed to explore the fundamentals of interacting with Large Language Models through Python.

Instead of implementing or training a Transformer architecture from scratch, this project uses an externally hosted language model through Groq's API.

The project is divided into several experiments, each demonstrating a different aspect of LLM interaction:

1. Basic AI interaction through API requests.
2. Experimenting with temperature settings to understand response randomness.
3. Creating a custom AI personality using system prompts.
4. Implementing conversational memory to maintain context across multiple messages.

Through these experiments, the project demonstrates how relatively simple Python code can be used to build and customise an interactive AI chatbot.

<h2>Architecture</h2>

The project consists of the following components:

Groq API Client – Establishes a connection to Groq's hosted AI inference service using an API key.

Model Configuration – Defines which language model is used to generate responses. The current implementation uses llama-3.1-8b-instant.

Basic Query Function – Sends a user's question to the model and retrieves its generated response through the chat completions API.

Temperature Configuration – Controls the randomness of generated responses. Higher values generally produce more varied outputs, while lower values encourage more predictable responses.

System Prompt – Defines the chatbot's personality and behaviour through system-level instructions.

Conversational Memory – Stores previous messages in a conversation history list, allowing the model to reference earlier interactions when generating subsequent responses.

<h2>Configuration</h2>

The current implementation uses the following configuration:

<h3>Parameter</h3>

Value

<h3>AI Provider</h3>

Groq

<h3>Model</h3>

Llama 3.1 8B Instant

<h3>API Interface</h3>

Groq Chat Completions

<h3>Programming Language</h3>

Python

<h3>Response Temperature Experiment</h3>

1.0

<h3>Default Personality</h3>

Nerd

<h3>Conversation Memory</h3>

Enabled in chat loop

<h3>User Interface</h3>

Command Line / Terminal

These values can be adjusted in the source code to experiment with different model configurations and chatbot behaviours.

<h2>Temperature Experimentation</h2>

The project includes an experiment using a temperature value of 1.0.

Temperature influences the randomness of generated responses:

- Low Temperature (0.0–0.3) – Generally produces more predictable and consistent responses.
- Medium Temperature (0.4–0.8) – Allows more variation while often maintaining coherence.
- High Temperature (around 1.0) – Encourages more varied and creative responses, although outputs may become less predictable.

<h2>Requirements</h2>

Python 3.9+

Groq Python SDK

Groq API Key

<h2>Installation</h2>

<h3>1. Clone the repository</h3>

git clone https://github.com/IoGamZ/PersonalTalkerGPT.git
cd PersonalTalkerGPT

<h3>2. Install dependencies</h3>

pip install groq requests schedule

The current implementation directly imports groq. The additional requests and schedule packages were included in the initial installation setup but are not directly used in the provided script.

<h3>3. Configure API Key</h3>

Open PT_GPT.py and locate:

GROQ_API_KEY = "INPUT VALID API KEY HERE"

Replace the placeholder with your own valid Groq API key.

<h3>4. Run the program</h3>

python PT_GPT.py

The program will execute several demonstrations:

1. Ask the user for a query and generate an AI response.
2. Generate a response using an experimental temperature setting.
3. Demonstrate a chatbot with a predefined personality.
4. Start a conversational loop that retains previous messages.

Type quit or exit to end the conversational loop.

<h2>Conversational Memory</h2>

One of the main experiments in this project is conversational memory.

The implementation uses a Python list to store the conversation history:

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

Whenever the user sends a message, it is appended to the list. The AI-generated response is then appended as well.

The conversation history is sent to Groq with each subsequent request.

This allows the model to reference previous messages and maintain conversational context.

It is important to note that this is context retention through conversation history, not permanent memory. The history exists only while the program is running.

<h2>Credits</h2>

Groq – Provides the API infrastructure used to access and run the language model.

Meta AI – Developer of the Llama 3.1 model used in this project.

CMKL University - Offering the course to study about creating our own NanoGPT

<h3>Author</h3>

IoGamZ

GitHub: @IoGamZ
