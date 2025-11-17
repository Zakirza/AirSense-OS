
# <img src="flow chat.png" height="48"> **AirSense-OS**

### **Voice + Gesture + AI Powered Operating Interface**

AirSense-OS is a next-generation human-computer interaction system that combines:

* **Touchless gesture control**
* **Voice-activated commands**
* **LLM-powered AI reasoning**
* **System automation**
* **Thread-safe audio engine**

This project brings you extremely close to **JARVIS-style interaction**:
control your computer using **your hands, your voice, and an AI brain**.

---

## 🚀 Features

### 🎤 **Voice Assistant**

* Ask time/date
* Google search
* YouTube playback
* Wikipedia queries
* Weather updates
* WhatsApp message automation
* System controls (shutdown, restart, lock)
* Memory storage (“remember that…”)
* Multi-language translation
* Screenshots
* Jokes, coin flips, dice
* **LLM fallback for any unknown question**

---

### ✋ **Gesture Virtual Mouse**

Real-time hand tracking using **MediaPipe Hands + OpenCV**:

| Gesture           | Action          |
| ----------------- | --------------- |
| Move index finger | Cursor movement |
| Index + Thumb     | Left Click      |
| Middle + Thumb    | Right Click     |
| Ring + Thumb      | Scroll          |
| Index + Middle    | Drag & Drop     |

✔ GPU-accelerated
✔ Low-latency (60 FPS)
✔ Adaptive smoothing
✔ Touchless control

---

### 🧠 **LLM Integration (AI Brain)**

Uses **OpenAI GPT-4.1 / GPT-4.1-mini** to:

* Answer complex questions
* Explain concepts
* Generate code
* Write content
* Summarize text
* Translate intelligently
* Solve reasoning tasks

Any command your assistant cannot understand is automatically routed to the LLM.

---

### 🔊 **Thread-Safe Text-to-Speech**

A dedicated queue-driven TTS worker thread prevents:

* pyttsx3 crashes
* “run loop already started” errors
* Overlapping audio

---

### 🧵 **Multithreaded Architecture**

* **Thread 1:** Voice assistant
* **Thread 2:** Text-to-speech
* **Main Thread:** Gesture tracking

Runs smoothly without blocking.

---

## 🧩 System Architecture

### Logo

(Place the logo image generated earlier as `logo.png`)

```
![AirSense-OS Logo](logo.png)
```

### Architecture Diagram

(Place the architecture image as `architecture.png`)

```
![Architecture Diagram](architecture.png)
```

---

## 🏗 Tech Stack

### Interaction

* `speech_recognition`
* `pyttsx3`
* `pyautogui`
* `mediapipe`
* `opencv-python`

### AI

* `openai` (GPT models)
* `googletrans`

### Automation

* `pywhatkit`
* `webbrowser`
* `requests`

### System

* Python 3.9+
* Threading

---

## 📦 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AirSense-OS.git
cd AirSense-OS
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add API Keys

Open main file (`main.py`):

#### 🔹 OpenAI

```python
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")
```

#### 🔹 Weather API

```python
api_key = "your_openweather_api_key"
```

---

## ▶️ Usage

### Run the system:

```bash
python main.py
```

---

## 🕹 Voice Commands You Can Use

* “What’s the time?”
* “Search for neural networks”
* “Play Alan Walker on YouTube”
* “Translate Hello to Spanish”
* “Explain quantum computing”
* “Remember that my exam is on Friday”
* “What do you remember?”
* “Shutdown the system”
* “Take a screenshot”

---

## ✋ Gesture Controls

| Gesture           | Meaning     |
| ----------------- | ----------- |
| 🖱 Index finger   | Cursor      |
| 👌 Index + Thumb  | Left Click  |
| 🤞 Middle + Thumb | Right Click |
| 👉 + 🖖           | Scroll      |
| ✌ Index + Middle  | Drag        |

---

## 🛑 Exit Program

Say:

```
stop
exit
bye
```

Or press **ESC** on the gesture window.

---

## 📁 Project Structure

```
AirSense-OS
│  main.py
│  README.md
│  requirements.txt
│
├── ai/
├── voice/
├── gesture/
└── utils/
```

---

## 🧠 Future Enhancements

* Wake-word (“Hey Nova”)
* Conversational memory
* Offline LLM support (LLaMA / Mistral / Phi-3)
* GUI dashboard
* PDF + document RAG search
* Eye-tracking integration
* Hand-gesture training via ML

---

## 🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first.

---

## 📜 License

MIT License.

---

## 🎉 Final Note

AirSense-OS represents a new way to interact with computers:
**touchless, intelligent, and immersive**.

