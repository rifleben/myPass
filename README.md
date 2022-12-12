# myPass

Password generator and vault to keep track of your passwords. Built with Python.

![](https://github.com/rifleben/myPass_gif/blob/main/myPass.gif)


## Summary:

The app requests users to enter their account name, username, and password. If the user wants a secure password generated, the program will offer one if clicked. Then, the program will copy that password to the user's clipboard to make pasting the secure password easier.

The program also has validation to ensure that a user is happy with the details entered and that there are no blank fields.

The program will then save, to a json file, the user details formatted in a readable way. A data.json file will be created storing the password info if the file does not exist on the user's machine (see repo for example). 

### Tools Used:
- Python Packages:
  - tkinter (GUI interface)
  - random
  - pyperclip
  - JSON
- IDE:
  - PyCharm
