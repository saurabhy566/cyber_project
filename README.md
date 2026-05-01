# Automated Linux MAC Address Changer

A lightweight Python script that automates the process of randomizing a network interface's MAC address at regular intervals. This project was developed as a hands-on exercise in Linux system automation, networking concepts (Layer 2), and basic Python scripting.

## 🚀 Features
* **Fully Automated:** Continuously changes the MAC address every 5 seconds without manual intervention.
* **System Integration:** Utilizes Python's `subprocess` module to interface directly with Linux command-line utilities.
* **Graceful Termination:** Includes `try/except` error handling to catch `KeyboardInterrupt` (Ctrl+C), allowing the user to cleanly stop the script with a status message.

## 🛠️ Prerequisites
Before running this script, ensure your Linux environment has the following installed:
1. **Python 3.x**
2. **Macchanger utility:** The script relies on the `macchanger` package.
   To install it on Debian/Ubuntu-based systems, run:
   ```bash
   sudo apt-get update
   sudo apt-get install macchanger
