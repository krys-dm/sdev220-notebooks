# my_task_module.py

import time
import random
from datetime import datetime

def task(name):
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)
    return f"{name} ended on: {datetime.now().strftime('%H:%M:%S.%f')}"
