# Block Data Processing

## Overview

This project processes blockchain block data to identify the largest transactions within a 24-hour period using sliding windows. It fetches block data from an API, processes it, and outputs the largest transactions both per window and overall for the last 24 hours.

## Features

- **Data Parsing**: Extracts and structures block data (block hash, timestamp, number of transactions).
- **Sliding Window Analysis**: Identifies the largest transactions within a rolling window of time (default 60-minute window, sliding every 5 minutes).
- **Overall Largest Transaction**: Finds the largest transaction within the last 24 hours.
- **Visualization**: Displays the largest transactions and saves the results as CSV files.

## Dependencies

- Python 3.x
- pandas
- requests
- matplotlib

To install dependencies, run:
```bash
pip install pandas requests matplotlib
