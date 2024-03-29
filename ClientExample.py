import logging
import os
import subprocess
import time

from RemoteHotKey.ClientManager import ClientManager

from MainActionManager import MainActionManager
from KeyboardAndMouseActionManager import KeyboardAndMouseActionManager
from LogToConsoleActionPerformer import LogToConsoleActionPerformer
from CustomTemplate import createTemplate
from RemoteHotKey.Utility.ActionPerformer_Pynput import ActionPerformer_Pynput

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler("log.log")])

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# subprocess.Popen(f"{ROOT_DIR}/frp/frpc.exe -c ./frp/frpc.ini")

client = ClientManager()
client.setUITemplate(createTemplate())

client.addActionManager(MainActionManager())
client.addActionManager(KeyboardAndMouseActionManager(LogToConsoleActionPerformer()))

client.start()
while 1:
    time.sleep(10)