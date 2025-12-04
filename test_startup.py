import sys
import traceback

with open('startup_log.txt', 'w') as f:
    try:
        f.write("Testing app startup...\n")
        f.write("Importing app...\n")
        import app
        f.write("App imported successfully!\n")
    except Exception as e:
        f.write(f"Error: {e}\n")
        traceback.print_exc(file=f)
