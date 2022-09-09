
from udea_reservation_automation.bot import Bot
from udea_reservation_automation.bot import Bot_Meet_Room
import time

def main():

    bot=Bot_Meet_Room()
    bot.enter_page()
    time.sleep(5)
    bot.Log_in("username","password")
    time.sleep(5)
    bot.library_interfaz()
    time.sleep(5)
    bot.meet_rooms_interfaz()
    time.sleep(5)
    bot.room1()
    time.sleep(5)
    bot.ReserveRoom()
    time.sleep(30)
    bot.close()

'''

    bot=Bot() #create a new bot
    bot.search_on_youtube("Risas de bebe remix")
    time.sleep(10)
    bot.go_to_video()#search  for videos on  youtube
    time.sleep(20)
    bot.close() #close the bot
'''




    
if __name__ == "__main__":
    main()


