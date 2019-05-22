#!/usr/bin/python
import os
import sys
def checkfile(filename):
    command = "echo 'seek 95 1' | mplayer -slave -msglevel all=4 -benchmark -vo null -nosound \"" + filename + "\" 2>&1"
    output = os.popen(command).read()
    if output.lower().find('error') == -1:
        return True
    else:
        return False
if __name__ == "__main__":
    for filename in sys.argv[1:]:
        if checkfile(filename):
            print('OK|' + filename)
        else:
            print('ERROR|' + filename)
            os.remove(filename)
