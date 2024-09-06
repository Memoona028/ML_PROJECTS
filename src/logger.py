## the purpose of this file to store all information related to exceution which will also helps us in determining errors 
## sow e can track error etc.
import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
## path to log file cwd() -> current working directory and filename would have log written too 
## log file will created in folder we will working on liek the folder src
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
##exist_ok=True: Allows the directory creation to proceed without raising an exception even if the directory already exists
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)
## checking whther it's working or not
if __name__=="__main__":
      logging.info("Checking.... %s %s", " ", "Logging has started")
