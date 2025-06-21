# app/src/scheduler.py

import time
import threading
from datetime import datetime
from src.inquiry.service import generate_llm_response  # Correct import path

def uvicron_scheduler():
    print("[UVICRON] Scheduler started.")
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == "12:00":  # Change this to your desired time
            print(f"[UVICRON] Scheduled Inquiry at {current_time}")
            try:
                query = "Hello, this is an automated inquiry."
                response = generate_llm_response(query)
                print(f"[UVICRON] Response: {response}")
            except Exception as e:
                print(f"[UVICRON Error] {e}")
        
        time.sleep(60)  # Check every 60 seconds
