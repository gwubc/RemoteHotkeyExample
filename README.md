## RemoteHotkey Example

This example demonstrates the use of RemoteHotkey, which can be found here: https://github.com/gwubc/RemoteHotkey


### Getting Started
Install requirement by `pip install remotehotkey`.\
Then start the server by running `python ClientExample.py`.\
Access the server interface at http://localhost:5000/.


### Interface Overview

This project focuses not on the appearance of the UI, but on its flexibility to adapt and rearrange elements to meet specific needs.


##### Initial Page: 

The first page appears as shown in the image below:
![img.png](./img.png)

Clicking on buttons [B1, B2, B3, B4] will output "B_ clicked" to the terminal.

##### Navigation: 
Select "Next Page" to navigate to the next screen:

![img_3.png](./img_3.png)

Clicking on numbers changes the total. For example, clicking 1, 7, -5 results in the updated total shown here:
![img_4.png](./img_4.png)

The total is automatically updated after each click.

Additional Feature: 
By clicking "Print Total To Terminal Repeatedly", the current total will be printed to the terminal every second.

### Control Keyboard and Mouse
To proceed to the next page, click on "Next Page" as shown above:
![img_5.png](./img_5.png)
Click on the letter "a". This action will print `tapKeyboard a` to the terminal.\
To enable keyboard control, you need to modify `ClientExample.py`. Here's how:

add `from RemoteHotKey.Utility.ActionPerformer_Pynput import ActionPerformer_Pynput`\
replace `client.addActionManager(KeyboardAndMouseActionManager(LogToConsoleActionPerformer()))`\
with `client.addActionManager(KeyboardAndMouseActionManager(ActionPerformer_Pynput()))`



### Customization
UI Customization: Modify the user interface by editing `CustomTemplate.py`.\
Behavior Customization: Change the functionality of each button by editing `CustomTemplate.py` and `MainActionManager.py`.
