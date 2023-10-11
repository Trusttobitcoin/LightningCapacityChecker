import subprocess
import json

def get_lightning_channels():
    """
    Execute `lncli listchannels` and return the output as a Python dictionary.
    """
    try:
        # Execute the `lncli listchannels` command and get the output as a JSON string
        output = subprocess.check_output(["lncli", "listchannels"], text=True)
        # Convert the JSON string to a Python dictionary
        channels = json.loads(output)
        return channels
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {str(e)}")
        return None
    except json.JSONDecodeError as e:
        print(f"Unable to parse output as JSON: {str(e)}")
        return None

def calculate_capacities(channels):
    """
    Calculate the total outbound and inbound capacities from the provided channels information.
    """
    total_capacity = 0
    total_outbound_capacity = 0
    
    # Check if 'channels' key exists in channels and it is not empty
    if 'channels' in channels and channels['channels']:
        # Iterate through each channel
        for channel in channels["channels"]:
            # Add the channel's total capacity and local balance (outbound capacity)
            total_capacity += int(channel["capacity"])
            total_outbound_capacity += int(channel["local_balance"])
    else:
        print("No channels found.")
    
    # Inbound capacity is total capacity minus outbound capacity
    total_inbound_capacity = total_capacity - total_outbound_capacity
    
    return total_outbound_capacity, total_inbound_capacity, total_capacity

def main():
    # Get the channels information
    channels = get_lightning_channels()
    
    # Check if channels were retrieved successfully
    if channels is not None:
        # Calculate the total outbound, inbound, and total capacities
        total_outbound_capacity, total_inbound_capacity, total_capacity = calculate_capacities(channels)
        
        # Convert satoshis to bitcoins for a more human-friendly display
        total_outbound_capacity_btc = total_outbound_capacity / 10**8
        total_inbound_capacity_btc = total_inbound_capacity / 10**8
        total_capacity_btc = total_capacity / 10**8
        
        print(f"Total Channel Capacity: {total_capacity_btc:.8f} BTC")
        print(f"Total Outbound Capacity: {total_outbound_capacity_btc:.8f} BTC")
        print(f"Total Inbound Capacity: {total_inbound_capacity_btc:.8f} BTC")
    else:
        print("Failed to retrieve channel information.")

if __name__ == "__main__":
    main()
