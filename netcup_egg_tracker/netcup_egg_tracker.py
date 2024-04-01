import requests
import json
import time
import os
from datetime import datetime

refs = [
    "/vserver/vserver_images.php",
    "/vserver/vps.php",
    "/vserver/",
    "/vserver/root-server-erweiterungen.php",
    "/",
    "/hosting",
    "/bestellen/domainangebote.php",
    "/bestellen/softwareangebote.php"
    "/ssl-zertifikate/",
    "/ueber-netcup/",
    "/ueber-netcup/hardware-infrastruktur.php",
    "/ueber-netcup/ddos-schutz-filter.php",
    "/ueber-netcup/auszeichnungen.php",
    "/ueber-netcup/zertifizierungen.php",
    "/ueber-netcup/partner.php",
    "/groupware/",
    "/professional/",
    "/professional/dedizierte-server/",
    "/professional/managed-server/",
    "/professional/colocation/",
    "/professional/softwareentwicklung/",
    
]

def get_price_formatted(price):
    return price.replace(",", ".").replace("&euro;", "EUR").replace(" ", "")

def main():
    while True:
        current_year = datetime.now().year  # Aktuelles Jahr abrufen
        folder_path = f"eggs_{current_year}"  # Ordnername mit aktuellem Jahr erstellen
        
        for r in refs:
            try:
                resp = requests.post("https://www.netcup.de/api/eggs", data={"requrl": r})
                egg = json.loads(resp.text)["eggs"][0]
                price = get_price_formatted(egg["price"])
                name = f"{price}Euro_{egg['id']}__{egg['title']}.json"
                name = name.replace("/", "_").replace("|", "_").replace("\\", "_").replace(":", "_").replace("*", "_").replace("?", "_").replace('"', "_").replace("<", "_").replace(">", "_")
                
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                
                egg['original_url'] = f"https://www.netcup.de/bestellen/produkt.php?produkt={egg['product_id']}&ref=230003&hiddenkey={egg['product_key']}"
                egg['found_url'] = f"https://www.netcup.de{r}"  # Hinzufügen der gefundenen URL
                egg['found_unix_time'] = int(time.time())  # Hinzufügen der Unix-Zeit
                with open(os.path.join(folder_path, name), "w") as file:
                    json.dump(egg, file, indent=4)
                
                print(f"{'-' * 10}")
                print(f"{egg['title']}")
                print(f"{price}")
                print(f"{egg['original_url']}")
                print(f"{egg['found_url']}")  # Ausgabe der gefundenen URL
                print(f"Found Unix Time: {egg['found_unix_time']}")  # Ausgabe der gefundenen Unix-Zeit
                print(f"{'-' * 10}")
            except Exception as e:
                pass
        
        print(f"\n\n Time Sleep - {2*60}")
        time.sleep(2 * 60)

if __name__ == "__main__":
    main()
