#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import matplotlib.pyplot as plt

chrome_100=[16.382361888885498, 11.331283807754517, 13.347985982894897, 10.653717041015625, 11.157796144485474, 20.079227209091187, 13.963016271591187, 12.541457891464233, 10.571033000946045, 10.904627799987793]
chrome_1=[120.58294796943665, 105.18527007102966, 116.8076741695404, 116.55678105354309, 102.66485691070557, 103.45651888847351, 111.83461594581604, 126.93886685371399, 135.3503668308258, 110.0745301246643]

tor_100=[57.39015984535217, 77.35663533210754, 91.06214714050293, 81.32533192634583, 83.01243209838867, 74.83794093132019, 80.68482613563538, 77.6638879776001, 65.9957549571991, 31.050397157669067]
tor_1=[332.3687870502472, 364.4225821495056, 596.9191191196442, 623.0427620410919, 369.031662940979, 393.0034749507904, 762.1211729049683, 811.2630667686462, 811.336767911911, 811.043604850769]

vpn_100=[13.284361839294434, 14.710711002349854, 14.115035772323608, 14.309076309204102, 17.971068859100342, 16.953383922576904, 15.620851993560791, 14.861648082733154, 13.447646856307983, 14.895258903503418]
vpn_1=[125.81482887268066, 113.42315173149109, 124.88232398033142, 153.28872799873352, 130.41537618637085, 126.64594793319702, 134.54498386383057, 143.65814089775085, 146.2625708580017, 133.99819421768188]

f1 = plt.figure(1)
plt.title("Chrome/Tor/Germany VPN Download Speed Histogram, 100MB")
plt.hist(np.sort(chrome_100), alpha=0.5, label='Chrome', color='red')
plt.hist(np.sort(tor_100), alpha=0.5, label='Tor', color='orange')
plt.hist(np.sort(vpn_100), alpha=0.5, label='VPN', color='blue')

plt.legend()
plt.xlabel("Time (s)")
f1.show()

f2 = plt.figure(2)
plt.title("Chrome/Tor/Germany VPN Download Speed Histogram, 1GB")
plt.hist(np.sort(chrome_1), alpha=0.5, label='Chrome', color='red')
plt.hist(np.sort(tor_1), alpha=0.5, label='Tor', color='orange')
plt.hist(np.sort(vpn_1), alpha=0.5, label='VPN', color='blue')

plt.legend()
plt.xlabel("Time (s)")
f2.show()

f3 = plt.figure(3)
plt.title("Germany VPN/Tor Download Speed Histogram, 100MB")
plt.hist(np.sort(vpn_100), alpha=0.5, label='VPN', color='orange')
plt.hist(np.sort(tor_100), alpha=0.5, label='Tor', color='purple')
plt.legend()
plt.xlabel("Time (s)")
f3.show()

f4 = plt.figure(4)
plt.title("Germany VPN/Tor Download Time Histogram, 1GB")
plt.hist(np.sort(vpn_1), alpha=0.5, label='VPN', color='orange')
plt.hist(np.sort(tor_1), alpha=0.5, label='Tor', color='purple')
plt.legend()
plt.xlabel("Time (s)")
f4.show()

print("TOR 100MB percentile:",np.percentile(tor_100, 95))
print("TOR 100MB mean:", np.mean(tor_100))
print("TOR 100MB median:", np.median(tor_100))

print("TOR 1GB percentile:",np.percentile(tor_1, 95))
print("TOR 1GB mean:", np.mean(tor_1))
print("TOR 1GB median:", np.median(tor_1))

print("VPN 100MB percentile:",np.percentile(vpn_100, 95))
print("VPN 100MB mean:", np.mean(vpn_100))
print("VPN 100MB median:", np.median(vpn_100))

print("VPN 1GB percentile:",np.percentile(vpn_1, 95))
print("VPN 1GB mean:", np.mean(vpn_1))
print("VPN 1GB median:", np.median(vpn_1))

print("Chrome 100MB percentile:",np.percentile(chrome_100, 95))
print("Chrome 100MB mean:", np.mean(chrome_100))
print("Chrome 100MB median:", np.median(chrome_100))

print("Chrome 1GB percentile:",np.percentile(chrome_1, 95))
print("Chrome 1GB mean:", np.mean(chrome_1))
print("Chrome 1GB median:", np.median(chrome_1))


# In[14]:


t_chrome_1 = calculate_throughputs_1(chrome_1)
t_tor_1 = calculate_throughputs_1(tor_1)
t_vpn_1 = calculate_throughputs_1(vpn_1)

f5 = plt.figure(5)
plt.title("Germany VPN/Tor/Chrome Througput Histogram, 1GB")
plt.hist(np.sort(t_vpn_1), alpha=0.5, label='VPN', color='red')
plt.hist(np.sort(t_tor_1), alpha=0.5, label='Tor', color='orange')
plt.hist(np.sort(t_chrome_1), alpha=0.5, label='Chrome', color='blue')

plt.legend()
plt.xlabel("MBps")
f5.show()


t_chrome_100 = calculate_throughputs_100(chrome_100)
t_tor_100 = calculate_throughputs_100(tor_100)
t_vpn_100 = calculate_throughputs_100(vpn_100)

f6 = plt.figure(6)
plt.title("Germany VPN/Tor/Chrome Througput Histogram, 100MB")
plt.hist(np.sort(t_vpn_100), alpha=0.5, label='VPN', color='red')
plt.hist(np.sort(t_tor_100), alpha=0.5, label='Tor', color='orange')
plt.hist(np.sort(t_chrome_100), alpha=0.5, label='Chrome', color='blue')

plt.legend()
plt.xlabel("MBps")
f6.show()




# In[18]:



print("TOR 100MB percentile:",np.percentile(t_tor_100, 95))
print("TOR 100MB mean:", np.mean(t_tor_100))
print("TOR 100MB median:", np.median(t_tor_100))

print("TOR 1GB percentile:",np.percentile(t_tor_1, 95))
print("TOR 1GB mean:", np.mean(t_tor_1))
print("TOR 1GB median:", np.median(t_tor_1))

print("VPN 100MB percentile:",np.percentile(t_vpn_100, 95))
print("VPN 100MB mean:", np.mean(t_vpn_100))
print("VPN 100MB median:", np.median(t_vpn_100))

print("VPN 1GB percentile:",np.percentile(t_vpn_1, 95))
print("VPN 1GB mean:", np.mean(t_vpn_1))
print("VPN 1GB median:", np.median(t_vpn_1))

print("Chrome 100MB percentile:",np.percentile(t_chrome_100, 95))
print("Chrome 100MB mean:", np.mean(t_chrome_100))
print("Chrome 100MB median:", np.median(t_chrome_100))

print("Chrome 1GB percentile:",np.percentile(t_chrome_1, 95))
print("Chrome 1GB mean:", np.mean(t_chrome_1))
print("Chrome 1GB median:", np.median(t_chrome_1))


# In[19]:


def calculate_throughputs_1(time_seconds):
    file_size_bits = 8 * 1_000_000_000 # 1GB 
    throughputs = [file_size_bits / (time * 1_000_000) for time in time_seconds]
    return throughputs


# In[20]:


def calculate_throughputs_100(time_seconds):
    file_size_bits = 100 * 8 * 1_000_000  # 100 MB
    throughputs = [file_size_bits / (time * 1_000_000) for time in time_seconds]
    return throughputs


# In[21]:


import time
import numpy as np
import os
import requests
import csv
import matplotlib.pyplot as plt
from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

NUM_SAMPLES = 10
NUM_FILES = 2
RETRY_COUNT = 3
RETRY_DELAY = 5
DOWNLOAD_DELAY = 10

Metrics = namedtuple('Metrics', 'file_name, file_size, avg_download_speed, download_times')

def hetzner_speed_test():
    driver = chrome_setup()
    url = "https://ash-speed.hetzner.com/"
    driver.get(url)

    download_elements = driver.find_elements(By.CSS_SELECTOR, "a")
    download_links = [elem.get_attribute('href') for elem in download_elements if elem.get_attribute('href').endswith(".bin")]
    download_links = download_links[:NUM_FILES]

    metrics_list = []

    for link in download_links:
        file_name = link.split('/')[-1]
        download_times = []

        print(f"Testing file: {file_name}")

        for sample in range(NUM_SAMPLES):
            success = False
            for attempt in range(RETRY_COUNT):
                try:
                    print(f"Sample {sample + 1}, Attempt {attempt + 1}: Downloading {file_name}...")

                    with requests.Session() as session:
                        session.headers.update({"User-Agent": "Mozilla/5.0"})
                        start_time = time.time()
                        response = session.get(link, stream=True, timeout=30)  
                        total_size = int(response.headers.get('content-length', 0))

                        with open(f"temp_{file_name}", 'wb') as temp_file:
                            for chunk in response.iter_content(chunk_size=1024):
                                temp_file.write(chunk)
                        end_time = time.time()

                        elapsed_time = end_time - start_time
                        download_times.append(elapsed_time)

                        os.remove(f"temp_{file_name}")
                        success = True
                        break
                except requests.exceptions.RequestException as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(RETRY_DELAY)

            if not success:
                print(f"Failed to download {file_name} after {RETRY_COUNT} attempts.")
                download_times.append(0)
                
        time.sleep(DOWNLOAD_DELAY)

        avg_speed = np.mean([(total_size / time) / (1024 * 1024) for time in download_times if time > 0])
        metrics = Metrics(file_name, total_size / (1024 * 1024) if total_size else 0, avg_speed, download_times) 
        metrics_list.append(metrics)

    write_data_to_file("hetzner_speed_test", metrics_list)
    plot_throughput_histogram(metrics_list)
    teardown(driver)

def write_data_to_file(name, metrics_list):
    with open(f"{name}_HVPNresults.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["File Name", "File Size (MB)", "Avg Download Speed (MB/s)", "Download Times (s)"])
        for metrics in metrics_list:
            writer.writerow([metrics.file_name, metrics.file_size, metrics.avg_download_speed, metrics.download_times])
    print(f"Results saved to {name}_HVPNresults.csv")


def chrome_setup():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-cache")
    service = Service(executable_path="drivers/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def teardown(driver):
    driver.quit()


# In[22]:


import time
import numpy as np
import os
import requests
import csv
import matplotlib.pyplot as plt
from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Constants
NUM_SAMPLES = 10
NUM_FILES = 2
RETRY_COUNT = 3
RETRY_DELAY = 5
DOWNLOAD_DELAY = 10

Metrics = namedtuple('Metrics', 'file_name, file_size, avg_download_speed, download_times')

def hetzner_speed_test_tor():
    driver = tor_setup()

    url = "https://ash-speed.hetzner.com/"
    driver.get(url)

    download_elements = driver.find_elements(By.CSS_SELECTOR, "a")
    download_links = [elem.get_attribute('href') for elem in download_elements if elem.get_attribute('href').endswith(".bin")]
    download_links = download_links[:NUM_FILES]

    metrics_list = []

    for link in download_links:
        file_name = link.split('/')[-1]
        download_times = []

        print(f"Testing file: {file_name}")

        for sample in range(NUM_SAMPLES):
            success = False
            for attempt in range(RETRY_COUNT):
                try:
                    print(f"Sample {sample + 1}, Attempt {attempt + 1}: Downloading {file_name}...")

                    proxies = {
                        'http': 'socks5h://127.0.0.1:9150',
                        'https': 'socks5h://127.0.0.1:9150',
                    }
                    with requests.Session() as session:
                        session.proxies.update(proxies)
                        session.headers.update({"User-Agent": "Mozilla/5.0"})
                        start_time = time.time()
                        response = session.get(link, stream=True, timeout=30)
                        total_size = int(response.headers.get('content-length', 0))

                        with open(f"temp_{file_name}", 'wb') as temp_file:
                            for chunk in response.iter_content(chunk_size=1024):
                                temp_file.write(chunk)
                        end_time = time.time()

                        elapsed_time = end_time - start_time
                        download_times.append(elapsed_time)

                        os.remove(f"temp_{file_name}")
                        success = True
                        break
                except requests.exceptions.RequestException as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(RETRY_DELAY)

            if not success:
                print(f"Failed to download {file_name} after {RETRY_COUNT} attempts.")
                download_times.append(0)

        time.sleep(DOWNLOAD_DELAY)

        avg_speed = np.mean([(total_size / time) / (1024 * 1024) for time in download_times if time > 0])
        metrics = Metrics(file_name, total_size / (1024 * 1024), avg_speed, download_times)
        metrics_list.append(metrics)

    write_data_to_file("tor_speed_test_results", metrics_list)
    plot_throughput_histogram(metrics_list)
    teardown(driver)

def write_data_to_file(name, metrics_list):
    with open(f"{name}.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["File Name", "File Size (MB)", "Avg Download Speed (MB/s)", "Download Times (s)"])
        for metrics in metrics_list:
            writer.writerow([metrics.file_name, metrics.file_size, metrics.avg_download_speed, metrics.download_times])
    print(f"Results saved to {name}.csv")

def tor_setup():
    tor_binary_path_driver = '/Applications/Tor Browser.app/Contents/MacOS/firefox'
    geckodriver_path = 'drivers/geckodriver'

    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.socks", "127.0.0.1")
    profile.set_preference("network.proxy.socks_port", 9150)
    profile.set_preference("network.proxy.socks_remote_dns", True)
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("network.cookie.cookieBehavior", 2)

    options = Options()
    options.profile = profile
    options.binary_location = tor_binary_path_driver
    options.headless = True

    return webdriver.Firefox(executable_path=geckodriver_path, options=options)

def teardown(driver):
    driver.quit()


# In[ ]:




