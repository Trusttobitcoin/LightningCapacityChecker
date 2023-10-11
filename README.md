
# LightningCapacityChecker

A simple Python tool for Lightning Network node operators to check and analyze the total, outbound, and inbound capacities of their channels.

## Overview

LightningCapacityChecker is a Python script designed to assist operators of LND Lightning Network nodes. It fetches and displays the total, outbound, and inbound capacities of the node's channels, providing a quick overview of the node's liquidity status. Utilizing `lncli`, this tool gathers data about your open channels and presents the summarized capacities in a user-friendly format.

## Features

- **Total Channel Capacity**: Sum of the capacities of all your channels.
- **Total Outbound Capacity**: Sum of all local balances, indicating how much you can send.
- **Total Inbound Capacity**: Calculated as (Total Channel Capacity - Total Outbound Capacity), representing how much you can receive.

## Prerequisites

- Python 3.x
- LND node with `lncli` configured and accessible.

## Usage

1. Ensure your LND node and `lncli` are configured and running.
2. Clone this repository or download the `LightningCapacityChecker.py` script.
3. Run the script in your terminal:
   ```shell
   python3 LightningCapacityChecker.py
   ```
4. Review the displayed capacities.

## Notes

- Ensure `lncli` is correctly configured and accessible from the environment where the script is executed.
- If your node uses specific configurations (e.g., testnet or custom macaroon paths), you may need to modify the subprocess call within the script.
- Always exercise caution with scripts interacting with cryptocurrency nodes and consider using them in a safe and offline environment when possible.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

Use this script at your own risk. The developer is not responsible for any financial losses or discrepancies in reported data. Always verify with multiple sources and use in a secure environment.

## Acknowledgments

- The LND development team for providing `lncli` and comprehensive documentation.
