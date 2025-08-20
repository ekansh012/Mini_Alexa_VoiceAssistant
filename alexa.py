import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if "alexa" in command:
            command = command.replace("alexa", "")
            return command
    return None


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Currently it is: ' + time)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())
    elif 'hello' in command:
        talk('Hi!')
    elif 'hi' in command:
        talk('Hello!')
    elif 'how are you' in command:
        talk('I am doing good! Thanks for asking!')
    elif 'what is your name' in command:
        talk('myself Alexa, your virtual assistant')
    elif 'who built you' in command:
        talk('I am developed by ekansh verma')
    elif 'jasmine verma' in command:
        talk('jasmine is the most nonsense girl in the whole universe')
    elif 'who has made you' in command:
        talk('I am developed by ekansh verma')
    elif 'what all can you do for me' in command:
        talk('well,  i can tell you jokes,  or fetch quick short results from wikipedia,  '
             'tell you the current time,  i can even respond to your queries,  '
             'and the most interestingly i can play songs for you')
    elif 'what can you do for me' in command:
        talk('well,  i can tell you jokes,  or fetch quick short results from wikipedia,  '
             'tell you the current time,  i can even respond to your queries,  '
             'and the most interestingly i can play songs for you')
    elif 'what can you do' in command:
        talk('well,  i can tell you jokes,  or fetch quick short results from wikipedia,  '
             'tell you the current time,  i can even respond to your queries,  '
             'and the most interestingly i can play songs for you')
    elif 'when is your birthday' in command:
        talk('I came into existence on 17th of July 2024')
    elif 'where do you live' in command:
        talk('Forever in your heart')
    elif 'i love you' in command:
        talk('love you too dear')
    elif 'what is the date today' in command:
        talk('its 17th of july today')
    elif 'what is the day today' in command:
        talk('its wednesday today')
    elif 'what is the date tomorrow' in command:
        talk('it will be 18th of july tomorrow')
    elif 'what is the day tomorrow' in command:
        talk('it will be thursday tomorrow')
    elif 'what is special about today' in command:
        talk('Its National Hot Dog Day today')
    elif 'what is your age' in command:
        talk('sorry, i cannot share it with you')
    elif 'How old are you' in command:
        talk('sorry, i cannot share it with you')
    elif 'you are very bad' in command:
        talk('if you think so i am really sorry then')
    elif 'you are mental' in command:
        talk('Even i feel bad you should not say such things to me')
    elif 'you are a moron' in command:
        talk('Even i feel bad you should not say such things to me')
    elif 'fuck off' in command:
        talk('Sorry, i am not supposed to answer this')
    elif 'you are an idiot' in command:
        talk('Even i feel bad you should not say such things to me')
    elif 'you are a waste' in command:
        talk('Even i feel bad you should not say such things to me')
    elif 'you are too good' in command:
        talk('Thanks i really appreciate your compliment')
    elif 'describe yourself' in command:
        talk('Hi there,  i am your virtual assistant alexa this side, i can do anything for you')
    elif 'who are you' in command:
        talk('Hi,  i am alexa, your virtual assistant')
    elif 'bye' in command:
        quit()
    else:
        talk('Sorry!, Please say the command again.')


while True:
    run_alexa()

