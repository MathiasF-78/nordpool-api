# Nordpool API Integration

## Introduction
This repository contains a Python script for integrating with the Nordpool API to retrieve day-ahead market data. The script retrieves area prices for a specified delivery area and time frame. 

### Important Note
The API should be executed no earlier than 13:30 UTC to ensure that prices are set for the following day.

## Prerequisites
Before running the script, ensure you have the following prerequisites installed:
- Python 3.x
- Requests library
- Dotenv library

## Setup
1. Clone this repository to your local machine.
2. Install the required libraries by running:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project directory with the following variables:
   ```
   password=your_password
   user_name=your_username
   api_key=your_api_key
   auth_url=authorization_url
   dayahead_url=dayahead_data_url
   host=api_host
   scope=authorization_scope
   ```
   Replace `your_password`, `your_username`, `your_api_key`, and other placeholders with your actual credentials and URLs.

## Usage
Run the script `nordpool_integration.py` to retrieve day-ahead market data. Ensure that the API is executed after 13:30 UTC for accurate results.

## Script Overview
The script performs the following steps:
1. Retrieves authentication token using OAuth 2.0.
2. Retrieves day-ahead market data for the specified delivery area and time frame.
3. Parses the response JSON to extract relevant information.

## Script Configuration
You can configure the following parameters in the script:
- `deliveryarea`: Area code for filtering content (e.g., SE3).
- `currency`: Currency code for filtering content (e.g., SEK).
- `startTime`: Start time in RFC3339 format (UTC).
- `endTime`: End time in RFC3339 format (UTC).

## Disclaimer
This script is provided for educational and informational purposes only. Use it responsibly and adhere to Nordpool's terms of service.

```
