import requests
from colorama import init, Fore

class CHAT:
    __TOKEN = ""
    __CHATID = ""
    __ANSWER = ""

    def __init__(self):
        with open("TOKEN.dat") as f1:
            self.__TOKEN = str(f1.readline())
            print(Fore.GREEN + "Find 'ALT+TAB Tb' in Telegram and send em a random message")
            input("Press Enter when done...")


    def getID(self):
        url = f"https://api.telegram.org/bot{self.__TOKEN}/getUpdates"
        self.__ANSWER = str(requests.get(url).json())
        print(self.__ANSWER)
        self.__parseAnswer()
        self.__writeId()

    def __parseAnswer(self):
        index = self.__ANSWER.find("'id':")
        if index > 0:
            index += 6
            while (self.__ANSWER[index] != ","):
                self.__CHATID += self.__ANSWER[index]
                index += 1
            print("\nLast message chat id is "+ Fore.YELLOW + self.__CHATID)


    def __writeId(self):
        f2 = open("USER_ID.txt","w+")
        f2.write(self.__CHATID)
        f2.close()



if __name__ == "__main__":
    init()
    p = CHAT()
    p.getID()






