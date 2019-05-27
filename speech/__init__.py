import pyttsx3


def number_name(num):
    if num == 1:
        return 'first'
    elif num == 2:
        return 'second'
    elif num == 3:
        return 'third'
    return num


def symbol_name(symbol):
    if symbol == 'x':
        return 'cross'
    elif symbol == 'o':
        return 'circle'
    return 'empty'


class Speech:
    def __init__(self, women=False):
        self.engine = pyttsx3.init()
        self.women = women

    def say(self, text):
        if self.women:
            self.engine.setProperty('voice', 'english+f1')
        else:
            self.engine.setProperty('voice', 'english+m1')
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()