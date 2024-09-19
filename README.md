# FP&A Chatbot

This is an **FP&A (Financial Planning & Analysis) Chatbot** built using **Flask** and **spaCy** for natural language processing. The chatbot is designed to answer specific questions related to financial planning, accruals, definitions, responsibilities, and access/authorization topics. It processes user queries and provides answers from a predefined knowledge base. Additionally, the chatbot interface includes user and bot message differentiation and a category-based question selection feature for easy navigation.

## Features

- **Natural Language Processing (NLP)**: Uses the `spaCy` library to analyze and match user queries with predefined questions.
- **Q&A Database**: The chatbot references a set of predefined questions and answers related to financial topics like accruals, definitions, and responsibilities.
- **User & Bot Messages Styling**: 
  - User messages are styled in red with white text.
  - Chatbot responses are styled in light grey with black text.
- **Category Questions**: Questions from different financial categories are displayed in red with white text for easy distinction.
- **Logo Integration**: The logo of the company is placed in the top left corner of the chat interface.
  
## Technologies Used

- **Flask**: A lightweight web framework for Python to run the chatbot backend.
- **spaCy**: A powerful NLP library for analyzing and processing the user's input.
- **HTML/CSS**: For the frontend user interface.

## How It Works

1. **User Interaction**: The user can ask questions through a text input box or select predefined categories to see related questions.
2. **Natural Language Understanding**: The chatbot uses the `spaCy` model to process the user's question and compares it with predefined questions in the Q&A database using text similarity.
3. **Response Generation**: The most relevant answer is fetched and displayed in the chat interface if the similarity score is above a set threshold.
4. **Category Selection**: Users can select specific categories of questions (like "Accruals and Deferrals" or "Definitions/Explanations") and see a list of available questions.

## How to Run the Project

### Prerequisites

- Python 3.x
- Flask
- spaCy
- `en_core_web_sm` model for spaCy

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/lailasamy/fpa_chatbot.git
   cd fpa_chatbot
