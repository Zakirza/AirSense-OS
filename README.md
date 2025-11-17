
---

# **ZeroTouch AI – Touchless Gesture + Voice Interaction System**

**ZeroTouch AI** is an advanced human-computer interaction system that allows users to operate a computer **without touching any hardware**.
It combines **AI-powered gesture recognition**, **voice assistant automation**, and **multi-threaded processing** to deliver a seamless, hygienic, and futuristic way to interact with a PC.

---

# 🚀 **Features**

## ✋ **Gesture Control (via MediaPipe + OpenCV)**

| Gesture                             | Operation                              |
| ----------------------------------- | -------------------------------------- |
| Index Finger Movement               | Move Mouse Cursor                      |
| Index + Thumb Touch                 | Left Click                             |
| Middle + Thumb Touch                | Right Click                            |
| Index + Middle Close                | Click & Drag                           |
| Ring + Thumb Touch                  | Scroll Up / Down                       |
| Thumb + Index + Middle + Ring Touch | Emergency Stop (Disables both modules) |
| Press Q / ESC                       | Stop gesture module manually           |

---

## 🎙 **Voice Assistant (SpeechRecognition + pyttsx3)**

| Command Category       | Examples                            |
| ---------------------- | ----------------------------------- |
| **Time & Date**        | “What’s the time?”                  |
| **Open Websites**      | “Open YouTube”, “Search for AI”     |
| **YouTube Playback**   | “Play Kesariya on YouTube”          |
| **WhatsApp Messaging** | “Send WhatsApp message”             |
| **Screenshot**         | “Take a screenshot”                 |
| **Weather**            | “What’s the weather in Mumbai?”     |
| **Jokes / Fun**        | “Tell me a joke”                    |
| **Randomizer**         | “Flip a coin”, “Roll a die”         |
| **Memory Notes**       | “Remember that I have a meeting”    |
| **Recall Notes**       | “What do you remember?”             |
| **System Control**     | Shutdown / Restart / Lock Screen    |
| **Module Toggle**      | “Disable gestures”, “Disable voice” |
| **Exit**               | “Stop”, “Exit”, “Bye”               |

---

# 🔁 **Parallel Multithreading**

Both gesture and voice modules run **simultaneously** using Python’s threading module:

* Gesture Thread → Tracks hand & executes cursor/scroll actions
* Voice Thread → Processes speech commands non-stop
* Shared State → Thread-safe enabling/disabling of modules

---

# 🧠 **System Architecture**

```
                   ┌────────────────────────┐
                   │      ZeroTouch AI       │
                   └────────────┬───────────┘
                                │
                ┌───────────────┴────────────────┐
                │                                │
      ┌─────────▼──────────┐           ┌─────────▼──────────┐
      │  Gesture Module    │           │   Voice Module     │
      │ (MediaPipe + CV2)  │           │ (Speech + TTS)     │
      └───────┬────────────┘           └─────────┬──────────┘
              │                                    │
              │                                    │
      ┌───────▼────────────┐             ┌─────────▼──────────┐
      │ Hand Landmarks     │             │ Command Processing │
      │ Finger Distance Calc│            │ (Wikipedia, YT, OS)│
      └───────┬────────────┘             └─────────┬──────────┘
              │                                    │
              └──────────┬────────────┬────────────┘
                         │            │
                ┌────────▼────────────▼─────────┐
                │       Shared State (Lock)     │
                │   gesture_enabled / voice_enabled  │
                └────────────────────────────────────┘
```

---

# 🛠 **Tech Stack**

* **Python**
* **MediaPipe Hands** (gesture tracking)
* **OpenCV**
* **PyAutoGUI** (mouse & scroll control)
* **SpeechRecognition** (Google Web Speech API)
* **pyttsx3** (text-to-speech)
* **Wikipedia API**
* **pywhatkit** (YouTube/WhatsApp automation)
* **Multithreading**
* **Shared-State Synchronization** (thread lock)

---

# 📂 **Project Structure**

```
ZeroTouch-AI/
│── main.py
│── gesture_module.py
│── voice_module.py
│── shared_state.py
│── requirements.txt
│── assistant_notes.json (auto-created)
│── README.md
```

---

# 🧩 **How to Run**

### 1. Install requirements

```
pip install -r requirements.txt
```

### 2. Start the system

```
python main.py
```

### 3. Allow microphone & camera access.

### 4. Use gestures or voice commands.

---
