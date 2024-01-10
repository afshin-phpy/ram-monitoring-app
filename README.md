# RAM Monitoring FastAPI Application

## Overview
This project is a FastAPI application designed to monitor and record system RAM usage. It periodically collects RAM data (total, used, and free memory) and stores this information in a SQLite database. Data collection is automated through a Python script and can be scheduled as a cron job.

## Installation

### Prerequisites
- Python 3.10+
- pip (Python package manager)

### Steps
Clone the repository and install the required packages:
```bash
git clone https://github.com/afshin-phpy/ram-monitoring-app.git
cd ram-monitoring-app
pip install -r requirements.txt
```
### Running the Application
Start the FastAPI server using:
```
uvicorn app:app --reload
```
The server will be hosted on http://127.0.0.1:8000. The --reload flag enables live reloading during development.

### Accessing RAM Data
The recorded RAM data can be viewed at the /ram_info endpoint:
```
http://127.0.0.1:8000/ram_info

```

### Cron Job Setup
To automate data collection, set up a cron job to run the script periodically:
1. Edit the crontab file:
```
crontab -e
```
2. Add the following line to execute the script every minute
```
* * * * * /usr/bin/python3 /path/to/ram_info_job.py
```

### Functionality

*   Data Collection: Automated collection and storage of total, used, and free RAM data.
*   Data Retrieval: The /ram_info API endpoint retrieves the latest RAM usage data.

### Testing
Run the unit tests to ensure the reliability of the application:

```
pytest
```

### API Reference

 * `GET /ram_info`: Retrieves the latest RAM usage data in JSON format.