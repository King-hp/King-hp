import speech_recognition as sr # as use to short form in speech recognition
import webbrowser
import pyttsx3
import musicLibrary
import feedparser


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def read_latest_news():
    news_feed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
    speak("Here are the latest news headlines.")
    for i in range(3):  # Read top 3 headlines
        headline = news_feed.entries[i].title
        print(f"News {i+1}: {headline}")
        speak(headline)

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
        
    elif "open insta" in c.lower():
        webbrowser.open("http://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif c.lower().startswith("play"):
        song =c.lower().split(" ")[1]
        link =musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower() or "latest news" in c.lower() or "shamachar" in c.lower():
        read_latest_news()
    elif "nothing" in c.lower():
            speak("Sorry, I couldn't find that song.")



if __name__ == "__main__":
    speak("Initializing Jarvis.....")

    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        

        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")

                # listen the commend
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
