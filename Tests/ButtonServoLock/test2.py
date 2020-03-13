from flask import Flask, render_template, request   
import RPi.GPIO as GPIO    
from time import sleep      
import socket


port= 5005

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80)) #only opening a socket not sending data
    return s.getsockname()[0]
    
    
print(get_ip_address() , port) # will print to a screen in future

servo_pin = 26          

 
GPIO.setmode(GPIO.BCM)      # We are using the BCM pin numbering
# Declaring Servo Pins as output pins
GPIO.setup(servo_pin, GPIO.OUT)     

 
# Created PWM channels at 50Hz frequency
p = GPIO.PWM(servo_pin, 50) #what is a pwm channel

 
# Initial duty cycle
p.start(0)

 
# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)
# Enable debug mode
app.config['DEBUG'] = True
 
# Store HTML code
TPL = "index.html"
 
# which URL should call the associated function.
@app.route("/")
def home():
    return render_template (TPL)
 
@app.route("/test", methods=["POST"])
def test():
    # Get slider Values
    slider1 = request.form["button"]
    
    # Change duty cycle
    p.ChangeDutyCycle(float(slider1))
   
    # Give servo some time to move
    sleep(1)
    # Pause the servo
    p.ChangeDutyCycle(0)
   
    return render_template (TPL)
 
# Run the app on the local development server
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5005)
  
