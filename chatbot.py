from flask import Flask, render_template_string, request, jsonify
import spacy

app = Flask(__name__)

nlp = spacy.load("en_core_web_sm")

qna_data = {
    "Accruals and Deferrals": [
        {"question": "What are the requirements for creating an accrual?",
         "answers": [
             "Accruals are possible from a turnover of EUR 10,000.",
             "Written documentation of our entitlement from an external party (insurer, customer).",
             "E.g., insurers offer incl. commission rate or amount & acceptance of offer by client."
         ]}
    ],
    "Definitions/ Explanations": [
        {"question": "What is the SIB spread?",
         "answers": [
             "The SIB spread is the difference between sales growth and SIB growth.",
             "The current SIB spread target is 2.",
             "E.g., with sales growth of 12%, SIB must not grow by more than 10% in order to achieve the SIB spread of 2."
         ]},
        {"question": "What is retention and how is it calculated?",
         "answers": [
             "Customer retention is calculated from the ratio of customer losses to total sales, minus non-recurring losses.",
             "Example: 1,000 revenue, 200 non-recurring lost, 150 lost; 1-(150/(1,000-200))= 81.25%"
         ]},
        {"question": "What is the health of business and how is it calculated?",
         "answers": [
             "The health of business is the ratio of recurring new business (new new & new ex) to losses."
         ]},
        {"question": "What is the rollover and how is it calculated?",
         "answers": [
             "This KPI describes what percentage of revenue, adjusted for all other effects (lost, timing, etc.), is recurring."
         ]}
    ],
    "Responsibilities": [
        {"question": "Who can I contact if I have questions about costs?",
         "answers": [
             "You can contact Oliver Gotthardt for questions about costs."
         ]},
        {"question": "Who can I contact if I have questions about revenue?",
         "answers": [
             "For regions East, Central, South & South-West, AGRC: Michael Sakschewski.",
             "For regions West & Global: Silke Furmanek.",
             "For region North: Patrick Hildebrand.",
             "For Specialties: Patrick Hildebrand."
         ]}
    ],
    "Access/ Authorization": [
        {"question": "How do I get access to the smart planning tool?",
         "answers": [
             "Submit an IT-Request at: https://aon.service-now.com/sp?id=sc_cat_item_guide&sys_id=bf8782e21bfa61507502a934604bcbef"
         ]},
        {"question": "How do I get access to Power-Bi?",
         "answers": [
             "You can contact Patrick Hildebrand for access to Power-Bi."
         ]}
    ]
}


def get_answer(user_query):
    doc = nlp(user_query.lower())
    best_match = None
    highest_similarity = 0.0
    for category, questions in qna_data.items():
        for item in questions:
            question_doc = nlp(item["question"].lower())
            similarity = doc.similarity(question_doc)
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = item
    if best_match and highest_similarity > 0.7:
        return "\n".join(best_match["answers"])
    return "Sorry, I don’t have an answer for that question."


@app.route('/')
def home():
    html_code = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FP&A Chatbot</title>
    <style>
        /* General styles for the body and chat container */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f0f4f8;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* Styling for the chat container */
.chat-container {
            max-width: 600px;
            width: 100%;
            margin: 20px;
            background-color: #ffffff;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
            padding: 20px;
            border-radius: 15px;
            display: flex;
            flex-direction: column;
            height: 80vh;
        }
/* Styling for the chat box */
.chat-box {
    flex-grow: 1;
    overflow-y: auto;
    border: 1px solid #ccc;
    padding: 15px;
    margin-bottom: 20px;
    background-color: #f9f9f9;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

/* Styling for chat messages */
.chat-box p {
    margin: 0;
    padding: 10px 15px;
    border-radius: 20px;
    max-width: 70%;
    word-wrap: break-word;
}

/* Styling for user messages */
.chat-box .user {
    align-self: flex-end;
    background-color: #007bff;
    color: white;
}

/* Styling for bot messages */
.chat-box .bot {
    align-self: flex-start;
    background-color: #e0ffe6;
    color: #333;
}

/* Styling for the input box */
.input-box {
    display: flex;
    justify-content: space-between;
}

/* Styling for the input field */
.input-box input {
    flex: 1;
    padding: 15px;
    border: 1px solid #ccc;
    border-radius: 25px;
    outline: none;
    margin-right: 10px;
    font-size: 16px;
}

/* Styling for the send button */
.input-box button {
    padding: 15px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 25px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s;
}

/* Styling for button hover effect */
.input-box button:hover {
    background-color: #0056b3;
}

/* Styles for the category buttons and container */
.category-container {
    display: flex;
    flex-wrap: wrap;
    gap: 10px; /* Space between buttons */
    margin-bottom: 20px; /* Space between buttons and chat box */
}

.category-btn {
    display: inline-block;
    padding: 5px 10px; /* Adjust padding to make buttons fit content */
    font-size: 13px; /* Adjust font size to fit content */
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 15px;
    cursor: pointer;
    transition: all 0.3s ease;
}

/* Styling for category buttons on hover */
.category-btn:hover {
    background-color: #0056b3;
    transform: scale(1.05);
}

/* Style for the fade-in animation */
.category-container.fade-in {
    display: flex;
    animation: fadeIn 0.8s ease-in-out;
}


/* Keyframes for fade-in animation */
@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

    </style>
    </head>
    <body>

    <div class="chat-container">
        <div class="chat-box" id="chat-box">
            <p class="bot">Hello! How can I assist you today?</p>
        </div>
        <div class="category-container" id="category-container">
            <button class="category-btn" onclick="showQuestions('Accruals and Deferrals')">Accruals and Deferrals</button>
            <button class="category-btn" onclick="showQuestions('Definitions/ Explanations')">Definitions/ Explanations</button>
            <button class="category-btn" onclick="showQuestions('Responsibilities')">Responsibilities</button>
            <button class="category-btn" onclick="showQuestions('Access/ Authorization')">Access/ Authorization</button>
        </div>
        <div class="input-box">
            <input type="text" id="user-input" placeholder="Ask a question...">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script>
        // Automatically show category options after the bot greeting
        document.addEventListener("DOMContentLoaded", function() {
            setTimeout(function() {
                document.getElementById('category-container').classList.add('fade-in');
            }, 1000);
        });

        function sendMessage() {
            const userInput = document.getElementById('user-input').value;
            if (!userInput) return;

            const chatBox = document.getElementById('chat-box');
            const userMessage = document.createElement('p');
            userMessage.className = 'user';
            userMessage.textContent = userInput;
            chatBox.appendChild(userMessage);
            chatBox.scrollTop = chatBox.scrollHeight;

            document.getElementById('user-input').value = '';

            fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query: userInput })
            })
            .then(response => response.json())
            .then(data => {
                const botMessage = document.createElement('p');
                botMessage.className = 'bot';
                botMessage.textContent = data.answer;
                chatBox.appendChild(botMessage);
                chatBox.scrollTop = chatBox.scrollHeight;
            });
        }

        function showQuestions(category) {
            const chatBox = document.getElementById('chat-box');
            chatBox.innerHTML += '<p class="bot">You selected the category: ' + category + '</p>';
            const questions = getQuestionsForCategory(category);
            questions.forEach(question => {
                const questionBtn = document.createElement('button');
                questionBtn.className = 'category-btn';
                questionBtn.textContent = question;
                questionBtn.onclick = () => {
                    document.getElementById('user-input').value = question;
                    sendMessage();
                };
                chatBox.appendChild(questionBtn);
            });
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        function getQuestionsForCategory(category) {
            const qnaData = {{ qna_data | tojson }};
            return qnaData[category].map(item => item.question);
        }
    </script>

    </body>
    </html>
    '''
    return render_template_string(html_code, qna_data=qna_data)


@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.json.get('query')
    answer = get_answer(user_query)
    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run(debug=True)
