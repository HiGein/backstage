from datetime import datetime
import platform
import os
import sys

dt = datetime.now()
dt_formatted = dt.strftime("%d.%m.%Y %H:%M:%S")

data={'Current date (default format)' : dt,
      'Current date dd.mm.yyyy hh:mm:ss' : dt_formatted,
      'Operating system name' : platform.system(),
      'Platform system name' : os.name,
      'System platform name' : sys.platform,
      'Platform release' : platform.release(),
      'Platform version' : platform.version(),
      'Platform details' : platform.platform()
     }

try:
    with open("/usr/local/bin/data.txt", "w") as file:
        for key, value in data.items():
            file.write('%-40s--- %s\n' % (key, value))
except FileNotFoundError:
    print("Not able to create 'data.txt' file")
