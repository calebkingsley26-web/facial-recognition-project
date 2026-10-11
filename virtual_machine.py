import datetime
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import webbrowser
import wikipedia
import yfinance as yf

# Initialize pyttsx3 engine once globally
engine = pyttsx3.init()

# Optional: Adjust voice rate and volume
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)  # Change index (0 or 1) for different voice options
#engine.setProperty('rate', 170)             # Speed of speech


def speak(message):
    """Speaks the provided string message."""
    print(f"Assistant: {message}")
    engine.say(message)
    engine.runAndWait()


def transform_audio_into_speech():
    """Listens to the microphone and returns recognized speech as text."""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        # Adjust for ambient background noise
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("\nListening...")

        audio = r.listen(source)

        try:
            request = r.recognize_google(audio, language="en-gb")
            print(f"You said: '{request}'")
            return request.lower()

        except sr.UnknownValueError:
            return "none"
        except sr.RequestError:
            speak("Network error with the speech recognition service.")
            return "none"
        except Exception as e:
            return "none"


def initial_greetings():
    """Greets the user based on the current time of day."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        greeting = "Good morning, Kingsley!"
    elif 12 <= hour < 18:
        greeting = "Good afternoon, Kingsley!"
    else:
        greeting = "Good evening, Kingsley!"

    speak(f"{greeting} How can I help you today?")


def process_request():
    """Main loop handling voice commands."""
    initial_greetings()

    go_on = True

    while go_on:
        my_request = transform_audio_into_speech()

        if my_request == "none":
            continue

        # 1. Open Websites
        if "open youtube" in my_request:
            speak("Sure. Let me open YouTube for you, Kingsley.")
            webbrowser.open("https://www.youtube.com")

        elif "open browser" in my_request or "open google" in my_request:
            speak("Of course, opening Google for you!")
            webbrowser.open("https://www.google.com")

        # 2. Play Music/Videos via YouTube
        elif "play" in my_request:
            song = my_request.replace("play", "").strip()
            speak(f"Playing {song} on YouTube.")
            pywhatkit.playonyt(song)

        # 3. Tell the Time & Date
        elif "time" in my_request:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {now}.")

        elif "date" in my_request or "day" in my_request:
            today = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"Today is {today}.")

        # 4. Wikipedia Search
        elif "wikipedia" in my_request or "search for" in my_request:
            speak("Searching Wikipedia...")
            query = my_request.replace("wikipedia", "").replace("search for", "").strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia:")
                speak(results)
            except wikipedia.exceptions.DisambiguationError:
                speak("There were multiple results for that search. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("I couldn't find any information on that topic.")

        # 5. Tell Jokes
        elif "joke" in my_request:
            joke = pyjokes.get_joke()
            speak(joke)

        # 6. Stock Price Checker
        elif "stock" in my_request or "price of" in my_request:
            speak("Which stock symbol would you like to check? For example, AAPL for Apple or TSLA for Tesla.")
            symbol = transform_audio_into_speech().upper().strip()
            if symbol != "NONE":
                try:
                    ticker = yf.Ticker(symbol)
                    price = ticker.history(period="1d")['Close'].iloc[-1]
                    speak(f"The current closing price for {symbol} is ${price:.2f}.")
                except Exception:
                    speak(f"Sorry, I couldn't fetch the stock information for {symbol}.")

        # 7. Goodbye / Exit Commands
        elif any(word in my_request for word in ["stop", "exit", "bye", "goodbye", "quit"]):
            speak("Goodbye Kingsley! Have a wonderful day.")
            go_on = False

        else:
            speak("I didn't quite catch that command. Could you repeat it?")


if __name__ == "__main__":
    process_request()