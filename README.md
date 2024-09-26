Got it! I'll include **everything** (installation, usage, and functionality) in the **README**.

Here's the **full README** with all the details:

```md
# Block Data Analyzer 🧑‍💻📊

## Overview

This project analyzes Ethereum blockchain data by fetching it from a public API. The main script parses the block data, then processes it to find the largest transactions within a sliding window of 24 hours. It outputs results both for each window and the overall largest transaction.

## Features

- **Fetch Ethereum Block Data:** Retrieve blockchain data from the CoinMetrics API.
- **Parse and Analyze Block Data:** Identify and display the largest transactions in a sliding window.
- **CSV Outputs:** Save the largest transactions for each window and the overall largest transaction in CSV files.
- **Visualization:** Optionally display largest transactions in the terminal.

## Project Structure

```bash
.
├── main.py                   # Main script to fetch, process, and display block data
├── api_utils.py              # Utility functions to interact with the API
├── outputs/                  # Directory for CSV outputs
│   ├── largest_transactions_per_hour_window.csv    # Transactions for each window
│   └── largest_transaction_overall.csv             # Largest overall transaction
└── data/
    └── response.json         # Cached API response data
```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/block-data-analyzer.git
    ```

2. Navigate into the project directory:
    ```bash
    cd block-data-analyzer
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
   Ensure you have the following packages installed:
   - `pandas`
   - `requests`
   - `matplotlib`
   
4. Create the necessary output directories:
    ```bash
    mkdir outputs
    mkdir data
    ```

## Usage

1. **Fetch and Process Block Data**:
    Run the main script to fetch the latest Ethereum block data and process it:
    ```bash
    python main.py
    ```

2. **CSV Outputs**:
    - The largest transactions for each hour window are saved to `outputs/largest_transactions_per_hour_window.csv`.
    - The overall largest transaction is saved to `outputs/largest_transaction_overall.csv`.

3. **Display Output**:
    The largest transactions for each window and the overall largest transaction are printed to the console.

## Functionality

### `main.py`

- **`parse_block_data(data)`**: Converts raw block data from the API into a `pandas` DataFrame.
- **`find_largest_transactions_per_window(df, window_size=60, step_size=5)`**: Identifies the largest transactions within a sliding window (default 60-minute windows, 5-minute steps).
- **`find_largest_transaction_overall(window_max_transactions)`**: Finds the largest transaction among all the windows.
- **`display_largest_transactions(window_max_transactions, largest_transaction_overall)`**: Displays the largest transactions in the terminal.

### `api_utils.py`

- **`fetch_block_data()`**: Fetches Ethereum block data from the CoinMetrics API and saves the response to `data/response.json`.

## Example Output

Example output displayed in the console:
```
Largest transactions for each window (last 24 hours):
block_hash     timestamp           n_transactions
...
...

Largest transaction overall:
block_hash     timestamp           n_transactions
...
```

## Configuration

- **API Configuration**: The API base URL and parameters can be modified in `api_utils.py`.
- **Window Configuration**: The window size and step size can be modified in the `find_largest_transactions_per_window` function inside `main.py`.

## License

This project is licensed under the MIT License.
