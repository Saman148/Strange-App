import keyboard 
import pyautogui 
import time 

class Spammer:
    def __init__(self, language, name, timeStart, timeMessage) :
        self.lang = language
        self.name = name 
        self.timeStart = timeStart
        self.timeMessage = timeMessage

    def start(self):
        time.sleep(self.timeStart)
        f = open(f'txt/{self.lang}_insult.txt', encoding='utf-8')
        if self.lang == 'fa':
            for word in f:
                keyboard.write(f'{self.name} {word}')
                time.sleep(self.timeMessage)
                pyautogui.press('Enter')
                
        elif self.lang == 'en':
            for word in f:
                keyboard.write(f'{word} {self.name}')
                time.sleep(self.timeMessage)
                pyautogui.press('Enter')