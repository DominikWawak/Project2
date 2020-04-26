# Project Name: Slidy

#### Student Name: *Dominik Wawak*   Student ID: *20089042*

# Contents:  
The project graphics are in the Documents folder  
The pictures of the project are in the images and Pictures folder.  
The website is in the root directory because of github pages hosting.  
The Tests folder contains multiple folders:  
* ButtonServoLock is the first try on the project using flask and a website to operate a servo motor
* servoAndBotTest test just the servo motor operated by a telegram bot.
* weightSensor contains tests I used on a load cell.  
Everything is also explained in the website linked below.
## Description:

Smart drawer that keeps track of the items you, have put in ,and taken out. The interaction with the drawer will be communicated to the user via a telegram bot. 
The drawer will also unlock with the use of messaging the telegram bot and keep count of your items.

## Tools, Technologies and Equipment:

* Communication  
The user and the drawer communicate through telegram chat bot created with the help of botFather on telegram.

* Weight/Force sensors  
The weight sensor used is SEN0160 with analog-to-digital converter.
It keeps track of the items in the drawer.
When an item is placed in the drawer knows its weight and increases the items count. When the user takes out the item the drawer also reports to the user.
The data will be reported to the user via the chat bot.

* Drawer lock  
A servo motor is used to open and close the drawer with th help of messaging the chat bot.

* Pulling everything together  
A raspberry pi handles the communication for this project aswell as gathering the data.



## Hardware, programming languages etc.

* Telegram chat bot api to handle the information and communicate with the user.
* SEN0160 weight sensor to controll the interaction with the drawer.
* A servo motor for the lock mechanism.
* Python used to program these devices.

## Finished Product
![](https://github.com/DominikWawak/Project2/blob/master/Presentation/Website_and_Tutorial/images/final.jpg)


# [Project Graphics](https://dominikwawak.github.io/Project2/)
 
# [Project Website](https://dominikwawak.github.io/Project2/index.html)
