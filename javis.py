import speech_recognition as sr
import pyttsx3

def speak_text(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

r = sr.Recognizer()

def record_text():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 =r.listen(source2)
                my_text = r.recognize_google(audio2)

                return my_text

        except sr.RequestError as e:
            print(f"Could not request result; {e}")
        except sr.UnknownValueError as e:
            print("Unknown error occurred")

def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write('\n')
    f.close()

while(True):
    text = record_text()
    output_text(text)
    speak_text(text)

    print("Text wrote")