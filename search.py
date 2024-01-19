import pywifi
from pywifi import const

def scan_wifi_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Assuming there is at least one WiFi interface

    iface.scan()
    scan_results = iface.scan_results()

    for result in scan_results:
        print("SSID: {}".format(result.ssid))
        print("BSSID: {}".format(result.bssid))
        print("Signal Strength: {} dBm".format(result.signal))
        
        # Check if 'channel' is present in the attributes
        if hasattr(result, 'channel'):
            print("Channel: {}".format(result.channel))
        else:
            print("Channel information not available.")
        
        print("Security: {}".format(result.akm[0]))
        print("-----------------------")

# Scan and display detailed information about available WiFi networks
scan_wifi_networks()