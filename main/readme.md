# Google Chrome Automation

A simple Python script that automates opening Google Chrome and performing a search for a specified song using GUI automation.

## Requirements

- Python 3.x
- `pyautogui` library

## Installation

1. Install Python from [python.org](https://www.python.org/).
2. Install the required library:
   ```
   pip install pyautogui
   ```

## Usage

Run the script from the command line:

```
python google_chrome_automation.py
```

The script will:
1. Open Google Chrome (assuming it's installed and accessible via Windows search).
2. Open a new tab.
3. Perform a search for the hardcoded song "montagem noche".
4. Click on the first result (coordinates are hardcoded and may need adjustment for your screen resolution).

**Note:** This script uses hardcoded mouse coordinates and may not work correctly on different screen resolutions or setups. Adjust the coordinates in the script if necessary.

## Disclaimer

This script uses GUI automation which can be unreliable and may interfere with other applications. Use at your own risk. Ensure that Google Chrome is not already running or adjust the script accordingly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
