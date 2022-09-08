
from udea_reservation_automation.bot import Bot
import time

def main():
    bot=Bot() #create a new bot
    bot.search_on_youtube("Risas de bebe remix")
    time.sleep(10)
    bot.go_to_video()#search  for videos on  youtube
    time.sleep(20)
    bot.close() #close the bot


if __name__ == "__main__":
    main()


