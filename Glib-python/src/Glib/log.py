# </> GlobalCode 
# Glib - source: log.py logger
# 1.0.0-release 

import os #TODO: заменить на свой модуль для работы с фс
from datetime import datetime
from colorama import Fore, Style, init
import re

#ALL LOG TYPES
#"INFO": 1,
#"WARNING": 2,
#"ERROR": 3,
#"DEBUG": 0,
#"NONE": -1
    
class LogInit:
    def __init__(self):
        self.dir = "./logs/" #путь сохранения логов
        self.filemask = "log-{date}.log" #маска файла
        self.filename = None #имя файла
        self.level = 1 #уровень фильтрации логов
        self.console_output = True #вывод в консоль
        self.write_file = True #запись лога в файл
        self.whoami = "Lmsg" #префикс логов "Lmsg: [{log type}] - msg"
        self.encoding = "utf-8" #вайбкодер не поймёт
        init()

    def filename_create(self):
        date = datetime.now().strftime("%Y-%m-%d")
        return self.filemask.replace("{date}", date)

    def _write_file(self, text, path, filename, encoding):
        try:
            if not os.path.exists(path):
                os.makedirs(path)

            if filename is None:
                self.filename = self.filename_create()
                filename = self.filename

            file_path = os.path.join(path, filename)

            with open(file_path, "a", encoding=encoding) as f:
                f.write(text + "\n")
        except Exception as e:
            self.write_file = False
            self._Lsystem_error(f"{e}", 3, "log.py-ERROR.log")
            exit(3)


    def VCTIT(self, CodeType): # Validity check and translation into text
        match CodeType:
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
        return False

    def Lprint(self, message, CodeType=0): # Log print
        LogTypeName = self.VCTIT(CodeType)

        if (not LogTypeName) or (not self.VCTIT(self.level)):
            if CodeType != -1 or self.level != -1:
                self._Lsystem_error(f"CodeType({CodeType}) or level({self.level}) - Not supported type", 2, "log.py-ERROR.log")
            return

        if (CodeType >= self.level) and (self.console_output):
            print(f"{Style.RESET_ALL}{Style.BRIGHT + self.whoami + Style.RESET_ALL}: [{LogTypeName + Style.RESET_ALL}] - {message}{Style.RESET_ALL}") 

        if self.write_file:
            self._write_file(re.sub(r'\x1b\[[0-9;]*m', '', f"[{datetime.now().strftime('%H:%M:%S')}] [{LogTypeName}] {self.whoami}: {message}"), self.dir, self.filename, self.encoding)

    def _Lsystem_error(self, msg, CodeType, fileN):
        path = "./Glib_E/"
        print(f"{Style.RESET_ALL}{Style.BRIGHT}Glibs-LOG{Style.RESET_ALL}: [{self.VCTIT(CodeType) + Style.RESET_ALL}] - {msg}{Style.RESET_ALL}")
        if self.write_file:
            self._write_file(re.sub(r'\x1b\[[0-9;]*m', '', f"[{datetime.now().strftime('%H:%M:%S')}] [{self.VCTIT(CodeType)}] Glibs-LOG: {msg}"), path, fileN, "utf-8")


def main_help():
    print("""log.py - удобное логирование
Пример использования:

from Glib.log import LogInit
from colorama import Fore #можно без этого импорта если не устанавливать цвет префикса в ручную 

logger = LogInit()
logger.level = 0

logger.Lprint(f"Уровень фильтрации равен {logger.level}", 0)
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 1)
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 2)
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 3)
logger.level = 1
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 0)
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 1)
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 2)
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 3)
logger.level = 2
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 0)
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 1)
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 2)
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 3)
logger.level = 3
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 0)
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 1)
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 2)
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 3)
logger.whoami=Fore.CYAN + "test"
logger.level = 0
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 0)
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 1)
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 2)
logger.Lprint(f"Уровень фильтрации равен {logger.level}", 3)

атрибуты:

dir - путь до деректории логирования (по умолчанию: "./logs/")
filemask - маска имени файла (по умолчанию: "log-{date}.log")
filename - имя конечного файла 
level - уровень фильтрации логов в консоль (по умолчанию: 1 (INFO))
console_output - разрешить вывод в консоль (по умолчанию: True)
write_file Разрешить запись логов в файл (по умолчанию: True)
whoami = Имя процесса(префикс) от которого пришёл лог (по умолчанию: "Lmsg")
encoding = кодировка выходного файла (по умолчанию: "utf-8")""")

if __name__ == "__main__":
    main_help()
