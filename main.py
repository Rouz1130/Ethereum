import pandas as pd
from datetime import timedelta
import matplotlib.pyplot as plt
from api_utils import fetch_block_data

window_output_csv_path = "outputs/largest_transactions_per_hour_window.csv"
overall_output_csv_path = "outputs/largest_transaction_overall.csv"

def parse_block_data(data):
    blocks = data.get("data", [])
    block_data = []

    for block in blocks:
        block_hash = block['block_hash']
        timestamp = block['consensus_time']
        n_transactions = int(block['n_transactions'])  
        
        block_data.append({
            "block_hash": block_hash,
            "timestamp": timestamp,
            "n_transactions": n_transactions
        })

    df = pd.DataFrame(block_data)
    df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True)
    
    return df

# Sliding window logic to find largest transactions within a rolling window
def find_largest_transactions_per_window(df, window_size=60, step_size=5):  
    df = df.sort_values(by='timestamp')

    end_time = df['timestamp'].max()
    start_time = end_time - timedelta(hours=24)

    print(f"Start time: {start_time}, End time: {end_time}")

    df_last_24_hours = df[(df['timestamp'] >= start_time) & (df['timestamp'] <= end_time)]
    largest_transactions_per_window = []

    current_time = start_time

    while current_time + timedelta(minutes=window_size) <= end_time:
        window_start = current_time
        window_end = current_time + timedelta(minutes=window_size)

        df_window = df_last_24_hours[(df_last_24_hours['timestamp'] >= window_start) & (df_last_24_hours['timestamp'] < window_end)]
        
        if not df_window.empty:
            largest_transaction = df_window.loc[df_window['n_transactions'].idxmax()]
            largest_transactions_per_window.append(largest_transaction)
        
        current_time += timedelta(minutes=step_size)

    largest_transactions_df = pd.DataFrame(largest_transactions_per_window)
    largest_transactions_df = largest_transactions_df.drop_duplicates()

    largest_transactions_df.to_csv(window_output_csv_path, index=False)
    
    return largest_transactions_df

def find_largest_transaction_overall(window_max_transactions):
    valid_transactions = window_max_transactions[window_max_transactions['n_transactions'] > 0]

    if not valid_transactions.empty:
        largest_transaction = valid_transactions.loc[valid_transactions['n_transactions'].idxmax()]
        largest_transaction.to_frame().T.to_csv(overall_output_csv_path, index=False)
        return largest_transaction
    else:
        print("No valid transactions found in the 24-hour period.")
        return None

def display_largest_transactions(window_max_transactions, largest_transaction_overall):
    print("\nLargest transactions for each window (last 24 hours):")
    print(window_max_transactions[['block_hash', 'timestamp', 'n_transactions']])
    
    print("\nLargest transaction overall:")
    if largest_transaction_overall is not None:
        print(largest_transaction_overall[['block_hash', 'timestamp', 'n_transactions']])
    else:
        print("No transactions found in the last 24 hours.")


if __name__ == "__main__":
    api_data = fetch_block_data()

    if api_data:
        df = parse_block_data(api_data)
        largest_transactions_per_window = find_largest_transactions_per_window(df)
        largest_transaction_overall = find_largest_transaction_overall(largest_transactions_per_window)
        display_largest_transactions(largest_transactions_per_window, largest_transaction_overall)
