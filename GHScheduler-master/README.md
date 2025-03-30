# 24/7 Flexible Schedule Manager

A web application for managing caregiver schedules with specific shift requirements.

## Features

- Four shift types: A (6am-2pm), B (2pm-10pm), C (10pm-6am), G (12pm-8pm)
- 8 caregivers working 40 hours per week
- Calendar view for schedule visualization
- Individual caregiver schedule view
- Automatic schedule generation following specific rules

## Requirements

- Python 3.8+
- Flask
- Flask-SQLAlchemy
- python-dateutil

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:
   ```bash
   python app.py
   ```

2. Generate the initial schedule:
   ```bash
   python schedule_generator.py
   ```

3. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Views

1. Home Page (`/`): Overview of shift types and general information
2. Calendar View (`/calendar`): Monthly view of all shifts
3. Caregiver View (`/caregivers`): Individual schedules for each caregiver

## Schedule Rules

- A Shift (6am-2pm): 2 caregivers per day
- B Shift (2pm-10pm): 2 caregivers per day (except Saturdays)
- C Shift (10pm-6am): 1 caregiver per day
- G Shift (12pm-8pm): 1 caregiver per day
- Each caregiver works 40 hours per week (5 days, 8 hours per day)
- Total of 8 caregivers in the system 