import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os
import random
import requests
import pyjokes
import pyautogui
from googletrans import Translator
import cv2
import mediapipe as mp
import numpy as np
import time
import threading
from queue import Queue

# --------- LLM (OpenAI) -------------
from openai import OpenAI

# ================== GLOBAL FLAGS ==================
running = True
notes = []

# ================== TTS ENGINE + QUEUE ==================
engine = pyttsx3.init()
engine.setProperty('rate', 175)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

speech_queue = Queue()

def tts_worker():
    """Dedicated TTS thread, avoids pyttsx3 crashes."""
    while True:
        text = speech_queue.get()
        if text is None:  # shutdown signal
            break
        print(f"\n🤖 Assistant: {text}")
        engine.say(text)
        engine.runAndWait()

tts_thread = threading.Thread(target=tts_worker, daemon=True)
tts_thread.start()


def speak(text):
    speech_queue.put(text)


# ================== LLM FUNCTION ==================
def ask_llm(prompt: str) -> str:
    """
    Send user text to LLM (OpenAI GPT model) and return response text.
    """
    try:
        client = OpenAI(api_key="YOUR_OPENAI_API_KEY")  # TODO: put your key here

        response = client.chat.completions.create(
            model="gpt-4.1-mini",  # you can change to gpt-4.1 or others
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant integrated into a voice and gesture control system. Reply concisely."},
                {"role": "user", "content": prompt}
            ]
        )

        # For new-style responses, message content may be in .message.content
        answer = response.choices[0].message.content
        return answer

    except Exception as e:
        print("LLM error:", e)
        return "There was an error while contacting the AI service."


# ================== VOICE INPUT ==================
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"🗣 You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
    except sr.RequestError:
        speak("There was a problem with the speech service.")
    return ""


# ================== WEATHER ==================
def get_weather(city):
    api_key = 'your_openweather_api_key'  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    data = requests.get(url).json()
    if data.get("main"):
        speak(f"The weather in {city} is {data['weather'][0]['description']} with {data['main']['temp']}°C")
    else:
        speak("City not found.")


# ================== TRANSLATION ==================
def translate_text(text, dest_language='hi'):
    translator = Translator()
    result = translator.translate(text, dest=dest_language)
    return result.text


# ================== COMMAND HANDLER ==================
def handle_command(command):
    global notes, running

    if 'time' in command:
        speak(datetime.datetime.now().strftime("It is %I:%M %p"))

    elif 'date' in command:
        speak(datetime.datetime.now().strftime("Today is %A, %B %d, %Y"))

    elif 'wikipedia' in command:
        topic = command.replace("wikipedia", "").strip()
        if not topic:
            speak("What should I search on Wikipedia?")
            return True
        try:
            summary = wikipedia.summary(topic, sentences=2)
            speak(summary)
        except wikipedia.exceptions.DisambiguationError:
            speak("The topic is too broad. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("I couldn't find anything on Wikipedia.")
        except Exception:
            speak("Something went wrong while searching Wikipedia.")

    elif 'youtube' in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif 'google' in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif 'search for' in command:
        query = command.replace("search for", "").strip()
        if query:
            speak(f"Searching for {query}")
            pywhatkit.search(query)
        else:
            speak("What should I search?")

    elif 'play' in command:
        song = command.replace("play", "").strip()
        if song:
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)
        else:
            speak("Please tell me the song name.")

    elif 'weather' in command:
        speak("Which city?")
        city = listen()
        if city:
            get_weather(city)
        else:
            speak("I didn't get the city name.")

    elif 'joke' in command:
        speak(pyjokes.get_joke())

    elif 'flip a coin' in command:
        speak("Heads" if random.choice([True, False]) else "Tails")

    elif 'dice' in command or 'roll a die' in command:
        speak(f"You rolled a {random.randint(1,6)}")

    elif 'screenshot' in command:
        file = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        pyautogui.screenshot(file)
        speak("Screenshot taken.")

    elif 'remember that' in command:
        speak("What should I remember?")
        note = listen()
        if note:
            notes.append(note)
            speak("I will remember that.")
        else:
            speak("I didn't hear anything to remember.")

    elif 'what do you remember' in command:
        if notes:
            speak("You asked me to remember: " + "; ".join(notes))
        else:
            speak("You haven't asked me to remember anything yet.")

    elif 'shutdown' in command:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")

    elif 'restart' in command:
        speak("Restarting the system.")
        os.system("shutdown /r /t 1")

    elif 'lock screen' in command:
        speak("Locking the screen.")
        os.system("rundll32.exe user32.dll,LockWorkStation")

    elif 'translate' in command:
        speak("What text should I translate?")
        phrase = listen()
        if not phrase:
            speak("I didn't catch the text to translate.")
            return True

        speak("Which language?")
        language = listen()
        if not language:
            speak("I didn't hear the language.")
            return True

        lang_codes = {
            'hindi':'hi','spanish':'es','french':'fr','german':'de',
            'tamil':'ta','telugu':'te','arabic':'ar','russian':'ru','english':'en'
        }

        code = lang_codes.get(language.lower())
        if code:
            translated = translate_text(phrase, code)
            speak(f"The translation in {language} is: {translated}")
        else:
            speak("Language not supported.")

    # ====== LLM Trigger (Direct) ======
    elif 'ai' in command or 'assistant' in command or 'explain' in command:
        speak("Let me think...")
        answer = ask_llm(command)
        speak(answer)

    # ====== GLOBAL EXIT ======
    elif any(x in command for x in ["stop", "exit", "bye", "quit"]):
        speak("Goodbye! Closing everything.")
        running = False
        return False

    # ====== FALLBACK TO LLM FOR ANY UNKNOWN COMMAND ======
    else:
        # Instead of “I did not understand”, send to LLM
        speak("I'll try to answer that.")
        answer = ask_llm(command)
        speak(answer)

    return True


# ================== VOICE ASSISTANT THREAD ==================
def run_assistant():
    speak("Voice assistant is online.")
    active = True
    while running and active:
        cmd = listen()
        if not running:
            break
        if cmd:
            active = handle_command(cmd)
    print("🛑 Voice assistant stopped.")


# ================== GESTURE VIRTUAL MOUSE ==================
def run_virtual_mouse():
    global running

    pyautogui.FAILSAFE = False
    cv2.setUseOptimized(True)
    cv2.ocl.setUseOpenCL(True)

    WIDTH, HEIGHT = 640, 480

    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    cap.set(3, WIDTH)
    cap.set(4, HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, 60)

    screen_w, screen_h = pyautogui.size()
    frame_margin = 100

    prev_x = prev_y = 0
    curr_x = curr_y = 0

    drag_active = False
    click_gap = 0.6
    last_left = last_right = last_scroll = 0

    def dist(a, b):
        return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5

    speak("Gesture virtual mouse is online.")

    with mp_hands.Hands(
        max_num_hands=1,
        model_complexity=0,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    ) as hands:

        skip = False

        while running:
            ret, frame = cap.read()
            if not ret:
                break

            skip = not skip
            if skip:
                continue

            frame = cv2.flip(frame, 1)
            h, w, _ = frame.shape
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            cv2.rectangle(frame, (frame_margin, frame_margin),
                          (w-frame_margin, h-frame_margin), (0,255,0), 2)

            if result.multi_hand_landmarks:
                for hand in result.multi_hand_landmarks:
                    lm = hand.landmark
                    index = lm[8]
                    middle = lm[12]
                    ring = lm[16]
                    thumb = lm[4]

                    # cursor control
                    x_raw = int(index.x * w)
                    y_raw = int(index.y * h)

                    x_c = np.clip(x_raw, frame_margin, w-frame_margin)
                    y_c = np.clip(y_raw, frame_margin, h-frame_margin)

                    nx = (x_c - frame_margin) / (w-2*frame_margin)
                    ny = (y_c - frame_margin) / (h-2*frame_margin)

                    target_x = nx * screen_w
                    target_y = ny * screen_h

                    curr_x = prev_x + (target_x - prev_x)*0.35
                    curr_y = prev_y + (target_y - prev_y)*0.35

                    pyautogui.moveTo(curr_x, curr_y)
                    prev_x, prev_y = curr_x, curr_y

                    now = time.time()

                    # left click
                    if dist(index, thumb) < 0.05 and now - last_left > click_gap:
                        pyautogui.click()
                        last_left = now

                    # right click
                    elif dist(middle, thumb) < 0.05 and now - last_right > click_gap:
                        pyautogui.rightClick()
                        last_right = now

                    # scroll
                    elif dist(ring, thumb) < 0.06 and now - last_scroll > 0.2:
                        pyautogui.scroll(50 if ring.y < thumb.y else -50)
                        last_scroll = now

                    # drag
                    elif dist(index, middle) < 0.045:
                        if not drag_active:
                            pyautogui.mouseDown()
                            drag_active = True
                    else:
                        if drag_active:
                            pyautogui.mouseUp()
                            drag_active = False

                    mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            cv2.imshow("Ultra Fast Virtual Mouse", frame)

            if cv2.waitKey(1) & 0xFF == 27:
                running = False
                break

    cap.release()
    cv2.destroyAllWindows()
    print("🛑 Gesture control stopped.")


# ================== MAIN ==================
if __name__ == "__main__":
    # start voice assistant thread
    voice_thread = threading.Thread(target=run_assistant, daemon=True)
    voice_thread.start()

    # run gesture mouse in main thread
    run_virtual_mouse()

    # stop TTS gracefully
    speech_queue.put(None)
    tts_thread.join()

    print("✅ Program ended.")
