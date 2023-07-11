import subprocess
import time

while True:
    # Run curl command
    subprocess.run(["curl", "<your_curl_command_here>"], capture_output=True, text=True)

    # Wait for 2 seconds
    time.sleep(2)
