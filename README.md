# 🌠Woila

Woila is a log analysis tool written in Python that provides simple yet informative log analysis using **AI** and/or **NON AI** features.

## ✨Features

- "*Clock*" for an **automatic analysis** every day at set time.
- **AI Summary** of analyzed logs in a set period of time(turned off by default, need API key to work!)
- Attack pattern recognition
- Customizeable trigger rules
- **And much more !!!**

## 🔨Stack

- Python 3.14+
- [duckdb](https://duckdb.org/)
- [uvicorn](https://uvicorn.dev/)
- [openai](https://github.com/openai/openai-python)

## 📁Structure

```code
├───backend
│   └───app
│       ├───api
│       ├───core
│       └───services
│           └───__pycache__
├───frontend
│   └───src
│       ├───assets
│       ├───components
│       │   └───ui
│       └───features
│           ├───charts
│           ├───dashboard
│           └───log-viewer
└───test_data
```

## 👨‍💻Usage

1. Start by entering a command for web GUI

    ```bash
    ./woila.py --web
    ```

2. This will start a local webserver and open a browser inside of which will be a web interface

3. Done! You can now use this utility as you wish

## 🏭 WIP

**ATTENTION!**

This project is still **under developement**, most of the things in this README are not done yet😝!
