"""Full Doku on: https://github.com/NapoII/netcup_egg_tracker"
-----------------------------------------------
Dieses Python-Skript ruft Produktinformationen von www.netcup.de ab und speichert sie in Textdateien. Der Dateiname enthält den Preis und die Produktinformationen. Automatische Aktualisierung alle 10 Minuten.
------------------------------------------------
"""

import requests
import json
import time
import os

refs = [
    "/vserver/vserver_images.php",
    "/vserver/vps.php",
    "/vserver/",
    "/vserver/root-server-erweiterungen.php",
    "/",
    "/hosting",
    "/bestellen/domainangebote.php",
    "/ssl-zertifikate/",
    "/ueber-netcup/",
    "/ueber-netcup/hardware-infrastruktur.php",
    "/ueber-netcup/ddos-schutz-filter.php",
    "/ueber-netcup/auszeichnungen.php"
]

def get_price_formatted(price):
    # Formatieren Sie den Preis, damit er in den Dateinamen eingefügt werden kann
    return price.replace(",", ".").replace("&euro;", "EUR").replace(" ", "")

def main():
    while True:
        for r in refs:
            try:
                resp = requests.post("https://www.netcup.de/api/eggs", data={"requrl": r})
                egg = json.loads(resp.text)["eggs"][0]
                print(egg)
                price = get_price_formatted(egg["price"])
                name = f"{price}Euro_{egg['id']}__{egg['title']}.txt"
                name = name.replace("/", "_").replace("|", "_").replace("\\", "_").replace(":", "_").replace("*", "_").replace("?", "_").replace('"', "_").replace("<", "_").replace(">", "_")
                with open(name, "w") as file:
                    file.write(f"https://www.netcup.de/bestellen/produkt.php?produkt={egg['product_id']}&hiddenkey={egg['product_key']}\n{json.dumps(egg)}\n{r}")
            except Exception as e:
                print(f"Error: {e}")
        print(f"\n\n Time Sleep - {10*60}")
        time.sleep(2 * 60)

if __name__ == "__main__":
    main()
