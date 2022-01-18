import subprocess
import os
import schedule
import time

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    print(output)
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    
    return last_line.lower().startswith(process_name.lower())

def tryrun():
    if process_exists("ownCloud.exe")==True:
        print("Owncloud Running")
    else:
        print("OwnCloud Not Running")
        
        os.startfile("C:\\Program Files (x86)\\ownCloud\\ownCloud.exe")
    

schedule.every().day.at("11:22").do(process_exists,"ownCloud.exe")
schedule.every().day.at("11:23").do(tryrun)

while True:
    schedule.run_pending()
    time.sleep(1)
