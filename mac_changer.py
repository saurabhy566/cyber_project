
import time
import subprocess

try:
    while True:
        subprocess.run(["sudo", "macchanger", "-r", "ens33"])
        time.sleep(5)
except KeyboardInterrupt:
    print("\n[+] MAC changer stopped by user")