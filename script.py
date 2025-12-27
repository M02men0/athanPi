#!/usr/bin/env python3

import csv
import time
import subprocess
from datetime import datetime, date, timedelta
from pathlib import Path

# --------------- Paths & configuration ---------------

BASE_DIR = Path("/home/user1/athan")
CSV_FILE = BASE_DIR / "schedule.csv"
AUDIO_DIR = BASE_DIR / "audio"
LOG_FILE = BASE_DIR / "logs" / "athan.log"

EVENT_AUDIO = {
    "fajr": "fajr.mp3",
    "sunrise": "sunrise_beep.mp3",
    "zuhr": "zuhr.mp3",
    "asr": "asr.mp3",
    "maghrib": "maghrib.mp3",
    "isha": "isha.mp3",
}

EVENT_ORDER = [
    "fajr",
    "sunrise",
    "zuhr",
    "asr",
    "maghrib",
    "isha",
]

# --------------- Utility functions ---------------

def log(message: str):
    LOG_FILE.parent.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {message}\n")

def play_event(event_type: str):
    audio_file = AUDIO_DIR / EVENT_AUDIO[event_type]
    log(f"Playing {event_type}")
    subprocess.run(
        ["mpg123", str(audio_file)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )

# --------------- Schedule loading ---------------

def load_today_schedule():
    today = date.today().isoformat()
    events = []

    with open(CSV_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["date"] == today:
                for event in EVENT_ORDER:
                    event_time = datetime.strptime(
                        f"{row['date']} {row[event]}",
                        "%Y-%m-%d %H:%M"
                    )
                    events.append({
                        "type": event,
                        "time": event_time
                    })
                break

    return sorted(events, key=lambda e: e["time"])

# --------------- Main scheduler loop ---------------

def main():
    log("Athan scheduler started")

    while True:
        events = load_today_schedule()

        if not events:
            log("No schedule found for today; sleeping until midnight")
            tomorrow = datetime.combine(
                date.today() + timedelta(days=1),
                datetime.min.time()
            )
            time.sleep((tomorrow - datetime.now()).total_seconds())
            continue

        for event in events:
            now = datetime.now()

            if event["time"] <= now:
                continue

            sleep_seconds = (event["time"] - now).total_seconds()
            log(f"Next event: {event['type']} in {int(sleep_seconds)} seconds")
            time.sleep(sleep_seconds)

            play_event(event["type"])

        # After last event, wait until next day
        tomorrow = datetime.combine(
            date.today() + timedelta(days=1),
            datetime.min.time()
        )
        time.sleep((tomorrow - datetime.now()).total_seconds())

# --------------- Entry point ---------------

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log(f"Fatal error: {e}")
        raise
