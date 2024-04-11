import requests
import json
import time
import os
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)

# ... rest of your code ...

def sanitize_filename(filename):
    return filename.replace("/", "_").replace("|", "_").replace("\\", "_").replace(":", "_").replace("*", "_").replace("?", "_").replace('"', "_").replace("<", "_").replace(">", "_")

def main():
    # ... rest of your code ...

    while True:
        
        for r in refs:

            try:
                # ... rest of your code ...

                file_name = sanitize_filename(f"{price}_{egg['id']}.json")
                sub_folder = sanitize_filename(f"{egg['title']}").replace(" ","_")  # Unterordner für angebotstyp erstellen
                
                # ... rest of your code ...

                logging.info(f"{'-' * 10}")
                logging.info(f"{egg['title']}")
                logging.info(f"{price}")
                logging.info(f"{egg['original_url']}")
                logging.info(f"{egg['found_url']}")  # Ausgabe der gefundenen URL
                logging.info(f"Found Unix Time: {egg['found_unix_time']}")  # Ausgabe der gefundenen Unix-Zeit
                logging.info(f"{'-' * 10}")
            
            except requests.exceptions.RequestException as e:
                logging.error(f"Request failed: {e}")
                continue
            except json.JSONDecodeError as e:
                logging.error(f"Failed to decode JSON: {e}")
                continue
            except Exception as e:
                logging.error(f"An unexpected error occurred: {e}")
                continue
        
        logging.info(f"\n\n Time Sleep - {2*60}")
        time.sleep(2 * 60)

if __name__ == "__main__":
    main()
