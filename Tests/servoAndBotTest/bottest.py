# credit to https://maker.pro/raspberry-pi/projects/how-to-create-a-telegram-bot-with-a-raspberry-pi
import datetime 
import telepot   
from telepot.loop import MessageLoop   
import RPi.GPIO as GPIO   
from time import sleep    


now = datetime.datetime.now() 

servo_pin = 26          

 
GPIO.setmode(GPIO.BCM)      # We are using the BCM pin numbering
# Declaring Servo Pins as output pins
GPIO.setup(servo_pin, GPIO.OUT)     

 
# Created PWM channels at 50Hz frequency
p = GPIO.PWM(servo_pin, 50) #what is a pwm channel

 
# Initial duty cycle
p.start(0)


def handle(msg):
    chat_id = msg['chat']['id'] # Receiving the message from telegram
    command = msg['text']   # Getting text from the message

    print ('Received:')
    print(command)
    
    bot.sendMessage (chat_id, str("Hi! type /open to open"))

    # Comparing the incoming message to send a reply according to it
    if command == 'hi':
        bot.sendMessage (chat_id, str("Hi! type /open to open"))
    elif command == 'time':
        bot.sendMessage(chat_id, str("Time: ") + str(now.hour) + str(":") + str(now.minute) + str(":") + str(now.second))
    elif command == 'date':
        bot.sendMessage(chat_id, str("Date: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year))
   
    elif command == 'open' or command == 'Open':
        bot.sendMessage(chat_id, str("opening your drawer"))
        p.ChangeDutyCycle(float(11.5))
   
        # Give servo some time to move
        sleep(1)
        # Pause the servo
        p.ChangeDutyCycle(0)
    elif command == 'close' or command == 'Close':
        bot.sendMessage(chat_id, str("closing your drawer"))
        p.ChangeDutyCycle(float(2))
   
        # Give servo some time to move
        sleep(1)
        # Pause the servo
        p.ChangeDutyCycle(0)
  


bot = telepot.Bot('ENTER ACCESS TOKEN HERE')
print (bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

while 1:
    sleep(10)
