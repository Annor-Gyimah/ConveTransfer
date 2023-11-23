# from resourcepath import resource_path
# try:
#     import pywifi

#     import iface
#     import comtypes
# except ModuleNotFoundError:
#     import pywifi


# def get_wifi_ssid():
#     wifi = pywifi.PyWiFi()
#     iface = wifi.interfaces()[0]  # Assuming the first Wi-Fi interface
#     ssid = iface.scan_results()[0].ssid if iface.scan_results() else "Not connected to Wi-Fi"
#     return ssid

# if __name__ == "__main__":
#     wifi_ssid = get_wifi_ssid()
#     print(f"Wi-Fi SSID: {wifi_ssid}")

try:
    import pywifi
    import iface
    import comtypes
except ModuleNotFoundError:
    import pywifi

def get_wifi_ssid():
    try:
        wifi = pywifi.PyWiFi()
        interfaces = wifi.interfaces()

        if not interfaces:
            return "No Wi-Fi interfaces found"

        iface = interfaces[0]  # Assuming the first Wi-Fi interface
        try:
            scan_results = iface.scan_results()

            if not scan_results:
                return "No Wi-Fi networks found"

            ssid = scan_results[0].ssid
            return ssid
        except Exception as scan_error:
            return f"Error scanning for networks: {scan_error}"
    except Exception as interface_error:
        return f"Error accessing Wi-Fi interface: {interface_error}"

if __name__ == "__main__":
    try:
        wifi_ssid = get_wifi_ssid()
        print(f"Wi-Fi SSID: {wifi_ssid}")
    except Exception as e:
        print(f"An error occurred: {e}")



# import subprocess
# import platform
# import os

# def get_wifi_ssid():
#     system_platform = platform.system()
    
#     if system_platform == "Windows":
#         try:
#             result = subprocess.check_output(["netsh", "wlan", "show", "interfaces"])
#             result = result.decode("utf-8").split("\n")
#             for line in result:
#                 if "SSID" in line:
#                     ssid = line.strip().split(":")[1].strip()
#                     return ssid
#         except subprocess.CalledProcessError:
#             return "Not available on Windows"

#     elif system_platform == "Linux":
#         try:
#             result = subprocess.check_output(["iwgetid"])
#             ssid = result.decode("utf-8").split('"')[1]
#             return ssid
#         except subprocess.CalledProcessError:
#             return "Not available on Linux"

#     else:
#         return "Unsupported platform"

# if __name__ == "__main__":
#     wifi_ssid = get_wifi_ssid()
    #print(f"Connected Wi-Fi SSID: {wifi_ssid}")

