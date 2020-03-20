# Project Name: Slidy

#### Student Name: *Dominik Wawak*   Student ID: *20089042*

## Description:

Smart drawer that keeps track of the items you, have put in ,and taken out. The interaction with the drawer will be communicated to the user via a telegram bot. 
The drawer will also unlock with the use of messaging the telegram bot.

## Tools, Technologies and Equipment:

* Communication  
The user and the drawer will communicate through telegram chat bot created with the help of botFather on telegram.

* Weight/Force sensors  
The weight sensor used is SEN0160 with analog-to-digital converter.
It will be used to keep track of the items in the drawer.
When an item is placed in the drawer will know its weight and store it. When the user takes out the item the drawer will know by the weight what item it was.
The data will be reported to the user via the chat bot.

* Drawer lock  
A servo motor is used to open and close the drawer with th help of messaging the chat bot.

* Pulling everything together  
A raspberry pi will be the device that will handle the communication for this project aswell as gathering the data.



## Hardware, programming languages etc.

* Telegram chat bot api to handle the information and communicate with the user.
* SEN0160 weight sensor to controll the interaction with the drawer.
* A servo motor for the lock mechanism.
* Python used to program these devices.

### The Project so far:
![](/Pictures/slidy1)


# [Project Graphics](https://dominikwawak.github.io/Project2/)
 
# [Project Repository](https://dominikwawak.github.io/Project2/)
