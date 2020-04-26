
# credit to https://maker.pro/raspberry-pi/projects/how-to-create-a-telegram-bot-with-a-raspberry-pi
import datetime 
import telepot   
from telepot.loop import MessageLoop   
import RPi.GPIO as GPIO   
from time import sleep  
import time  
import env



now = datetime.datetime.now() 

servo_pin = 26        

DT =27
SCK=17




sample=0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)      # We are using the BCM pin numbering
# Declaring Servo Pins as output pins
GPIO.setup(servo_pin, GPIO.OUT)  
GPIO.setup(SCK, GPIO.OUT)   

 
# Created PWM channels at 50Hz frequency
p = GPIO.PWM(servo_pin, 50) #what is a pwm channel

 
# Initial duty cycle
p.start(0)
#weight part

def show_weight():
    count= readCount()
    w=0
  
    w=(count-sample)/106
    actualw =( (w -80933)/20)+8 #calibration
    
    
    
    
    print actualw,"g"
   
    return actualw


def readCount():
  i=0
  Count=0
  #print Count
  time.sleep(0.5)
  GPIO.setup(DT, GPIO.OUT)
  GPIO.output(DT,1)
  GPIO.output(SCK,0)
  GPIO.setup(DT, GPIO.IN)

  while GPIO.input(DT) == 1:
      i=0
  for i in range(24):
        GPIO.output(SCK,1)
        Count=Count<<1

        GPIO.output(SCK,0)
        #time.sleep(0.001)
        if GPIO.input(DT) == 0: 
            Count=Count+1
            #print Count
        
  GPIO.output(SCK,1)
  Count=Count^0x800000
  #time.sleep(1)
  GPIO.output(SCK,0)
  return Count 

itemadded = False
previous = show_weight()
current = previous
delta = 5

def handle(msg):
    chat_id = msg['chat']['id'] # Receiving the message from telegram
    command = msg['text']   # Getting text from the message

    print ('Received:')
    print(command)

  
   
    bot.sendMessage (chat_id, str("Hi! the commands you can use are: time, date, open, close and tell me weight"))
    
    
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
    elif command == 'tell me weight' or command == 'Tell me weight':
        bot.sendMessage(chat_id, str(show_weight()))
    
    

    
        
   
bot = telepot.Bot(env.access_token)

print(bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')



    

noitems=0

count = 0
while 1:
    show_weight()
    current = show_weight()
    difference = previous - current
    if abs(difference)>delta:
        count=count + 1  #increment count
        time.sleep(8)
        if (count == 3): #if 3 successive readings in excess of delta
            if(current>previous):
                print("item added")
                noitems=noitems+1
                bot.sendMessage(env.chat_id, str("Item has been added current weight = " + str(current - 4)+ "g , " + "number of items = "+ str(noitems)))
            elif(current<previous):
                noitems=noitems-1
                print("item removed")
                bot.sendMessage(env.chat_id, str("Item has been removed current weight = " + str(current-4) + "g , "+ "number of items = "+ str(noitems)))
            previous = current
            count=0 
    else:
        count=0 #reset count to 0
  
  
sleep(10)
