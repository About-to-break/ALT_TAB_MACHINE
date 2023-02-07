import requests
import random

class Telesend:
    def __init__(self):
            #Токен
            try:
                self.__TOKEN = open("Plugins/Telegram/TOKEN.dat").readline()
            except FileNotFoundError:
                print("TELEGERAM_PLUGIN: cannot locate TOKEN file")
                self.__flag = False
            #Chat
            try:
                self.__CHAT_ID = open("Plugins/Telegram/USER_ID.txt").readline()
            except FileNotFoundError:
                self.__flag = False
                print("TELEGERAM_PLUGIN: cannot locate USER_ID file\n Run ID.bat to create it!")
            #Фразы
            try:
                aliases_file = open("Plugins/Telegram/Aliases.txt")
                for quip in aliases_file:
                    self.__QUIPS.append(quip)
            except FileNotFoundError:
                self.__flag = False
                print("TELEGERAM_PLUGIN: cannot locate QUIPS file")


    def statusSignalizer(self):
        return self.__flag

    def __takeQuip(self):
        return random.choice(self.__QUIPS)

    def __sendMessage(self):
        message = self.__takeQuip()
        url = f"https://api.telegram.org/bot{self.__TOKEN}/sendMessage?chat_id={self.__CHAT_ID}&text={message}"
        requests.get(url).json()  # this sends the message

    def action(self):
        self.__sendMessage()
    __flag = True
    __TOKEN = ""
    __CHAT_ID = ""
    __QUIPS = []
