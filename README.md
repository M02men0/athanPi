# 🕌 athanPi 🕌
## Raspberry Pi Adhan Scheduler

> **﴿ إِنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا ﴾**  
> *سورة النساء — الآية ١٠٣*  
>  
> **“Indeed, prayer has been prescribed for the believers at fixed times.”**
> *(Qur’an 4:103)*


/* discription */ 

---

## ✨ Features

- ⏰ Plays Adhan at exact prayer times (CSV-based)
- 🌅 Sunrise notification sound (beep)
- 🔊 USB DAC / external speaker support
- 🔁 Runs at boot & restarts on crash (systemd)
- 🧠 Simple, extensible Python design
- 🌐 Uses internet time (RTC-ready later)

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

## 🔄 Startup & Reliability

- Managed by **systemd**
- Starts automatically at boot
- Restarts automatically if it crashes
- Logs activity to a file for debugging

---

## 🚀 Planned Enhancements

- 🔔 Pre-Adhan alerts (e.g. 10 minutes before Maghrib)
- 🔉 Per-prayer volume control
- 🕌 Iqamah notifications
- 🧭 RTC fallback for offline operation
- 🧩 Button / LCD / Web configuration
