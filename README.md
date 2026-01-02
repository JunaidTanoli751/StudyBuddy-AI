# StudyBuddy-AI
# 📘 StudyBuddy AI

An interactive **AI-powered study tutor** that explains concepts, conducts **real-time quizzes**, checks answers, and **tracks user scores** — built using **OpenAI Agent SDK**, **Gemini API**, and **Chainlit**.

---

## 🚀 Features

✅ Friendly AI Tutor (StudyBuddy AI)

✅ Explain concepts in **simple language** with examples

✅ Interactive **quiz mode** (one question at a time)

✅ Automatic **answer checking** (Correct / Incorrect)

✅ **Score tracking** during quizzes

✅ Topic-based quizzes (Python, Math, CS, etc.)

✅ Real-time chat UI using **Chainlit**

---

## 🧠 How Quiz Mode Works

1. User starts a quiz using:

   ```
   start quiz <topic>
   ```

   Example:

   ```
   start quiz python loops
   ```

2. StudyBuddy AI:

   * Asks **one question at a time**
   * Waits for user answer
   * Checks correctness
   * Updates score automatically

3. User can:

   * Check score using:

     ```
     /score
     ```
   * End quiz using:

     ```
     /end quiz
     ```

---

## 🛠 Tech Stack

* **Python 3.10+**
* **OpenAI Agent SDK**
* **Gemini API (via OpenAI-compatible endpoint)**
* **Chainlit** (Chat UI)
* **python-dotenv** (Environment variables)
* **uv** (Fast Python package manager)

---

## 📂 Project Structure

```
StudyBuddy-AI/
│
├── app.py                # Main Chainlit app
├── .env                  # API keys (not committed)
├── pyproject.toml        # Dependencies (uv)
├── README.md             # Project documentation
└── .venv/                # Virtual environment
```

---

## 🔑 Environment Setup

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

⚠️ Never commit `.env` to GitHub.

---

## 📦 Installation (Using uv)

```bash
uv init
uv add chainlit python-dotenv agents
```

Activate environment (Windows):

```bash
.venv\Scripts\activate
```

---

## ▶️ Run the App

```bash
uv run chainlit run app.py -w
```

Then open the browser link shown in terminal.

---

## 💡 Example Commands

```text
Explain Python decorators
start quiz data structures
/score
/end quiz
```

---

## 🎯 Use Cases

* Students learning programming or CS
* Beginners preparing for exams
* Interactive self-study tool
* AI tutor demo for portfolios

---

## 🧑‍💻 Author

**Junaid Tanoli**
BSCS | AI & Data Science Learner

GitHub: [https://github.com/JunaidTanoli751](https://github.com/JunaidTanoli751)

---

## ⭐ Future Improvements

* Difficulty levels (Easy / Medium / Hard)
* Timed quizzes
* Multiple-choice questions
* Persistent score history
* User authentication

---

## 📜 License

This project is for **learning and portfolio purposes**.

---

✨ *If you like this project, don’t forget to star the repo!*
