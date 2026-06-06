# </> GlobalCode 
# Glib - source: log.py logger
# 1.0.0-rc1

import os
from datetime import datetime
from colorama import Fore, Back, Style, init
import re

#LOG LEVEL PIN
#"INFO": 1,
#"WARNING": 2,
#"ERROR": 3,
#"DEBUG": 0,
#"NONE": -1

    
class LogInit:
    def __init__(self):
        self.path = "./logs/"
        self.name = "log-{date}.log"
        self.filename = None
        self.level = 1
        self.console_print = True
        self.Lmsg = "Lmsg"
        self.encoding = "utf-8"
        init()

    def filename_create(self):
        date = datetime.now().strftime("%Y-%m-%d")
        return self.name.replace("{date}", date)

    def _write_file(self, text):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        if self.filename == None:
            self.filename = self.filename_create()

        file_path = os.path.join(self.path, self.filename)

        with open(file_path, "a", encoding=self.encoding) as f:
            f.write(text + "\n")
    def statusLOG(self, status):
        col=""
        match status:
            case 0:
                return Fore.MAGENTA + "DEBUG"
            case 1:
                return Fore.GREEN + "INFO"
            case 2: 
                return Fore.YELLOW + "WARNING"
            case 3:
                return Fore.RED + "ERROR"
            case _:
                return False
    def write(self, message, status=-1):
        logstat = self.statusLOG(status)
        if not logstat or not self.statusLOG(self.level):
            return

        if status >= self.level:
            self._write_file(re.sub(r'\x1b\[[0-9;]*m', '', f"[{datetime.now().strftime('%H:%M:%S')}] [{logstat}] {self.Lmsg}: {message}"))

            if self.console_print:
                print(f"{Style.BRIGHT + self.Lmsg + Style.RESET_ALL}: [{logstat + Style.RESET_ALL}] - {message}") 
