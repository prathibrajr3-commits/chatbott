# 🤖 Chatbot

A modern AI chatbot web application built using:

* Python
* Django
* Google Gemini AI API
* HTML
* CSS
* Bootstrap

This project allows users to chat with Google's Gemini AI model through a modern web interface.

---

# 🚀 Features

✅ AI-powered chatbot
✅ Modern futuristic UI
✅ Responsive design
✅ User & AI chat bubbles
✅ Gemini AI integration
✅ Django backend
✅ Real-time AI responses
✅ Beginner-friendly project

---

# 🛠 Technologies Used

| Technology | Purpose                |
| ---------- | ---------------------- |
| Python     | Backend programming    |
| Django     | Web framework          |
| Gemini API | AI response generation |
| HTML       | Page structure         |
| CSS        | Styling                |
| Bootstrap  | Responsive UI          |

---

# 📂 Project Structure

```text
chatbot/
│
├── chatbot/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── ai_app/
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── templates/
│   └── index.html
│
├── manage.py
└── requirements.txt
```

---

# ⚙️ Installation

## 1. Clone Project

```bash
git clone <your-github-repo>
```

---

## 2. Create Virtual Environment

```bash
python -m venv env
```

---

## 3. Activate Environment

### Windows

```bash
env\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install django
pip install google-generativeai
```

---

# 🔑 Gemini API Setup

## Step 1

Create Gemini API key from:

[https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

---

## Step 2

Add API key in:

```python
settings.py
```

```python
GEMINI_API_KEY = "YOUR_API_KEY"
```

---

# ▶️ Run Project

```bash
python manage.py runserver
```

Open browser:

```text
http://127.0.0.1:8000
```

---

# 🧠 How It Works

```text
User Message
      ↓
Django Backend
      ↓
Gemini API
      ↓
AI Generates Response
      ↓
Response Displayed on Website
```

---

# 💻 views.py Example

```python
from django.shortcuts import render
from django.conf import settings
import google.generativeai as genai

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def home(request):

    answer = ""

    if request.method == "POST":

        user_message = request.POST.get("message")

        try:
            response = model.generate_content(user_message)
            answer = response.text

        except Exception as e:
            answer = str(e)

    return render(request, "index.html", {"answer": answer})
```

---

# 🎨 UI Features

* Glassmorphism design
* Dark theme
* Responsive layout
* Chat-style message bubbles
* Smooth animations
* Mobile-friendly interface

---

# 📸 Future Improvements

You can upgrade this project with:

* User authentication
* Chat history database
* Voice assistant
* AI image generation
* Streaming responses
* Dark/light mode toggle
* Multiple AI models
* File upload support

---

# 📚 Learning Outcomes

By building this project, you learn:

* Django basics
* API integration
* AI chatbot development
* Frontend + backend connection
* Prompt handling
* Modern UI design
* Real-world AI application workflow

---

# 🌟 Project Use Cases

* AI assistant
* Customer support bot
* Personal chatbot
* Portfolio project
* AI SaaS starter project
* Learning Django AI integration

---

# 👨‍💻 Author

Developed by Prathib

---

# ⭐ Conclusion

This Django Gemini AI Chatbot is a beginner-friendly AI web application that demonstrates how modern AI can be integrated into web development using Django and Gemini API.

It is a great starting point for building advanced AI SaaS products and intelligent web applications.
