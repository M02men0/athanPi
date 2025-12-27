# 🕌 athanPi 🕌

> **﴿ إِنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا ﴾**  
> *سورة النساء — الآية ١٠٣*  
>  
> **“Indeed, prayer has been prescribed for the believers at fixed times.”**
> *(Qur’an 4:103)*

## Raspberry Pi Adhan Scheduler

A lightweight *Raspberry Pi Athan* system that plays Athan and notifications at precise times using a CSV schedule and local audio files.

Designed to run *headless*, *at boot*, and reliably as a *background service*.

---

## ✨ Features

- ⏰ Plays Athan for the 5 daily prayers
- 🌅 Plays a notification sound at sunrise (beep)
- 📅 Uses a CSV schedule (monthly or yearly)
- 🔊 Outputs audio via USB DAC / sound card
- 🔁 Auto-starts on boot (systemd)
- 🛠️ Auto-restarts if it crashes
- 📜 Logs activity for debugging

---

## 🛠 Hardware Used

- Raspberry Pi Zero 2 W
- USB DAC 
- Powered speaker
- microSD card

---

## 📁 Directory Structure

```
/home/user1/athan/
├── script.py
├── schedule.csv
├── audio/
│   ├── fajr.mp3
│   ├── sunrise_beep.mp3
│   ├── zuhr.mp3
│   ├── asr.mp3
│   ├── maghrib.mp3
│   └── isha.mp3
└── logs/
    └── adhan.log
```

---

## 📊 CSV Format

```csv
date,fajr,sunrise,zuhr,asr,maghrib,isha
2025-01-01,06:10,07:39,12:13,15:04,16:47,18:12
```

- Date format: `YYYY-MM-DD`
- Time format: `HH:MM` (24-hour)
- One row per day

---

## ▶️ How It Works

1. Loads **today’s row** from the CSV  
2. Converts times into system clock events  
3. Sleeps until the next event  
4. Plays the associated audio using `mpg123`  
5. Repeats daily  

The script runs continuously and uses almost no CPU.

---

## 🔮 Planned Extensions

- 🔔 Pre-Athan alerts (e.g. 10 minutes before Maghrib)
- 🔉 Per-prayer volume control
- 🕌 Iqamah notifications
- 🧭 RTC fallback for offline operation
- 🧩 Button / LCD / Web configuration
