# 🤖 PG-AGI – AI-Powered Hiring Assistant

Welcome to **PG-AGI**, a Streamlit-based AI chatbot built for "TalentScout," a fictional recruitment agency focused on tech placements. PG-AGI acts as an intelligent Hiring Assistant, screening candidates by gathering essential details and generating relevant technical questions based on the declared tech stack.

---

## 📘 Project Overview

PG-AGI uses **Google's gemini-1.5-flash-latest model** with Langchain, offering:

* Smart candidate interaction
* Sentiment analysis
* Language translation support
* Context-aware chat history
* Automatic chat log saving

This tool demonstrates effective **prompt engineering**, **LLM integration**, and **interactive UI development** with **Streamlit**.

---

## 🎯 Features & Capabilities

### ✅ Core Functionality

* **Greeting**: Welcomes the candidate and introduces its role.
* **Information Gathering**:

  * Full Name
  * Email Address
  * Phone Number
  * Years of Experience
  * Desired Position(s)
  * Current Location
  * Tech Stack
* **Tech Stack Declaration**: Prompts user to specify technologies they know.
* **Dynamic Question Generation**:

  * Generates 3–5 technical questions per candidate based on stack.
  * E.g., Python + Django → questions on both.
* **Context Retention**: Maintains chat history and flow.
* **Sentiment Analysis**: Uses `TextBlob` to assess tone (positive, neutral, negative).
* **Multilingual Support**: Translates non-English inputs via `deep-translator`.
* **Conversation Exit**: Recognizes exit keywords and gracefully ends chat.
* **History Saving**: Saves each conversation to a timestamped `.txt` file.

---

## 🧱 Architecture & Stack

| Layer       | Technology                                      |
| ----------- | ------------------------------------------------|
| UI          | Streamlit                                       |
| LLM Backend |gemini-1.5-flash-latest,Langchain & Google GenAI |
| Translation | deep-translator                                 |
| Sentiment   | TextBlob                                        |
| Deployment  | Localhost / Render Cloud                        |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pg-agi-hiring-assistant.git
cd pg-agi-hiring-assistant
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/Mac
.venv\Scripts\activate   # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. API Key Setup

Create a file named `google_api_key.txt` in the root directory and paste your Google Generative AI API key inside.

---

## 🚀 Running the App

```bash
streamlit run app.py
```

---

## 🧠 Prompt Design Strategy

The system prompt defines the assistant's role and task breakdown. It ensures structured information gathering followed by stack-aware technical questioning.

**System Prompt Example:**

```
You are TalentScout, a professional hiring assistant for a tech recruitment agency...
```

Prompts are dynamically generated based on user input and appended to a `ChatPromptTemplate` using Langchain.

---

## 💬 Example Interaction Flow

1. Chatbot greets the user.
2. Collects profile details (name, experience, tech stack, etc).
3. Generates tailored questions (e.g., Python, React, etc).
4. Applies sentiment analysis on each input.
5. Translates input if not in English.
6. Ends the chat gracefully when the user types "exit".
7. Saves chat log.

---

## 📁 File Structure

```
.
├── app.py                  # Main chatbot application
├── google_api_key.txt      # API key (not committed)
├── requirements.txt        # Python dependencies
├── README.md               # Documentation
└── chat_history_*.txt      # Saved conversation logs
```

---

## 📚 Requirements File

```txt
streamlit==1.35.0
langchain-core==0.1.44
langchain-google-genai==0.0.8
textblob==0.18.0
deep-translator==1.11.4
```

---

## ⚠️ Known Limitations

* **API Quota**: Free-tier limits from Gemini API (\~50 requests/day). 
* **SystemMessage Error**: Handled using `convert_system_message_to_human=True` in production deployments.

---

## 🧩 Challenges & Solutions

| Challenge                            | Solution                                    |
| ------------------------------------ | ------------------------------------------- |
| Gemini system messages not supported | Used `convert_system_message_to_human=True` |
| Free tier quota exceeded             | Shown 429 error with link to quota info     |
| Unexpected input or language         | Translated using `deep-translator`          |


---

## 🌐 Deployment Notes

* Deployed locally and tested.
* Bonus: Hosted on [Render](https://pg-agi-chatbot.onrender.com) .
* Compatible with Streamlit Cloud.

---

## 🎥 Demo / Presentation

* [Loom Video Demo](#) *(Optional link)*
* Or attach `.mp4` walk-through in GitHub repo

---


**M A**

---

PG-AGI combines AI power with practical hiring needs. It's modular, multilingual, and highly customizable. A great starting point for AI-driven recruitment automation.
