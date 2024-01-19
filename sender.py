import pywifi
import time

def find_wifi_interface():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Assuming there is at least one WiFi interface
    return iface

def scan_and_connect(iface, ssid, password):
    iface.scan()
    time.sleep(2)
    scan_results = iface.scan_results()

    target_network = None
    for result in scan_results:
        if result.ssid == ssid:
            target_network = result
            break

    if target_network is not None:
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password

        iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(profile)
        iface.connect(tmp_profile)
        time.sleep(5)  # Wait for the connection to be established

        if iface.status() == const.IFACE_CONNECTED:
            print(f"Connected to {ssid}")
        else:
            print("Connection failed")
    else:
        print(f"Network {ssid} not found")

def send_receive_message():
    # Implement your send/receive logic here
    print("Sending and receiving messages")

if __name__ == "__main__":
    wifi_iface = find_wifi_interface()

    # Replace 'YourNetworkSSID' and 'YourNetworkPassword' with your actual Wi-Fi credentials
    network_ssid = 'Orange-ali abo ahmed 2'
    network_password = '78200316122005'

    scan_and_connect(wifi_iface, network_ssid, network_password)

    # Once connected, you can implement your send/receive logic
    send_receive_message()