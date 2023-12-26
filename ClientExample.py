import logging
import os
import subprocess
import time

from RemoteHotKey.ClientManager import ClientManager

from MainActionManager import MainActionManager
from LogToConsoleActionPerformer import LogToConsoleActionPerformer
from CustomTemplate import createTemplate


logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler("log.log")])

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# subprocess.Popen(f"{ROOT_DIR}/frp/frpc.exe -c ./frp/frpc.ini")

client = ClientManager()
client.setUITemplate(createTemplate())

client.addActionManager(MainActionManager(LogToConsoleActionPerformer()))

client.start()
while 1:
    time.sleep(10)