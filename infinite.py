from subprocess import run
from time import sleep

# Path and name to the script you are trying to start
file_path = "ustar_server_20240314.py" 

restart_timer = 2

def start_script():
    try:
        # Make sure 'python' command is available
        run(["python", file_path]) 
    except Exception as e:
        # Script crashed, lets restart it!
        print(f"Script crashed with error: {e}")
        handle_crash()

def handle_crash():
    sleep(restart_timer)  # Restarts the script after 2 seconds
    start_script()

start_script()