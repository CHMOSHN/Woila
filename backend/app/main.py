import uvicorn
import webbrowser
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

#Creating an app object
app = FastAPI()

#Checking current and static directories
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, "static")

#Host, port and address
ADDRESS = "127.0.0.1"
PORT = 1337
HOST = "http://127.0.0.1:1337"

#Checking if everything correct and mounting / if so
if os.path.exists(static_dir):
    app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

#Starting the local web server
def start() -> None:
    try:
        print(f"""
[+] Creating local server...
[+] Succesfully created local server!
[+] Address: {ADDRESS}
[+] Port: {PORT} 
              """)
        webbrowser.open(HOST)        
        uvicorn.run(app=app, host=ADDRESS, port=PORT, log_level=None)
    except Exception as e:
        print(f"Error while starting local server:\n{e}")

#Executing main function
if __name__ == '__main__':
    start()        
        