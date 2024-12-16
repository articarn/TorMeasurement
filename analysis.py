import numpy
import re
import matplotlib.pyplot as plt

numpy.set_printoptions(suppress=True)

# Metrics
# 0: startup_time
# 1: dns_time
# 2: tcp_time
# 3: tls_time
# 4: wait_time
# 5: receive_time
# 6: process_time
# 7: loading_time
# 8: blocked_time
# 9: duration
# 10: throughput
# 11: transferSize

def print_means(data, browser):
    total_times = numpy.sort((data[:, 8] + data[:, 9]))

    print(f"{browser} Mean Startup Time: ", numpy.mean(data[:, 0]))
    # for i in range(numpy.shape(data)[0]):
    #     print(f"{browser} Mean Page {i+1} Startup Time: ", numpy.mean(data[i, 0]))
    print(f"{browser} Mean Startup Time (Exclude Page 1): ", numpy.mean(numpy.delete(data, 0, axis=0)[:, 0]))
    print("-------------------------------------------")
    print(f"{browser} Mean DNS Time: ", numpy.mean(data[:, 1]))
    print(f"{browser} Mean Page 1 DNS Time: ", numpy.mean(data[0, 1]))
    # for i in range(numpy.shape(data)[0]):
    #     print(f"{browser} Mean Page {i+1} DNS Time: ", numpy.mean(data[i, 1]))
    print(f"{browser} Mean DNS Time (Exclude Page 1): ", numpy.mean(numpy.delete(data, 0, axis=0)[:, 1]))
    print("-------------------------------------------")
    print(f"{browser} Mean TCP Time: ", numpy.mean(data[:, 2]))
    # for i in range(numpy.shape(data)[0]):
    #     print(f"{browser} Mean Page {i+1} TCP Time: ", numpy.mean(data[i, 2]))
    print(f"{browser} Mean TCP Time (Exclude Page 1): ", numpy.mean(numpy.delete(data, 0, axis=0)[:, 2]))
    print("-------------------------------------------")
    print(f"{browser} Mean TLS Time: ", numpy.mean(data[:, 3]))
    # for i in range(numpy.shape(data)[0]):
    #     print(f"{browser} Mean Page {i+1} TLS Time: ", numpy.mean(data[i, 3]))
    print(f"{browser} Mean TLS Time (Exclude Page 1): ", numpy.mean(numpy.delete(data, 0, axis=0)[:, 3]))
    print("-------------------------------------------")
    print(f"{browser} Mean Wait Time: ", numpy.mean(data[:, 4]))
    # for i in range(numpy.shape(data)[0]):
    #     print(f"{browser} Mean Page {i+1} Wait Time: ", numpy.mean(data[i, 4]))
    print(f"{browser} Mean Wait Time (Exclude Page 1): ", numpy.mean(numpy.delete(data, 0, axis=0)[:, 4]))
    print("-------------------------------------------")
    print(f"{browser} Mean Receive Time: ", numpy.mean(data[:, 5]))
    # for i in range(numpy.shape(data)[0]):
    #     print(f"{browser} Mean Page {i+1} Receive Time: ", numpy.mean(data[i, 5]))
    print(f"{browser} Mean Receive Time (Exclude Page 1): ", numpy.mean(numpy.delete(data, 0, axis=0)[:, 5]))
    print("-------------------------------------------")
    print(f"{browser} Mean Process Time: ", numpy.mean(data[:, 6]))
    # for i in range(numpy.shape(data)[0]):
    #     print(f"{browser} Mean Page {i+1} Process Time: ", numpy.mean(data[i, 6]))
    print(f"{browser} Mean Process Time (Exclude Page 1): ", numpy.mean(numpy.delete(data, 0, axis=0)[:, 6]))
    print("-------------------------------------------")
    print(f"{browser} Mean Loading Time: ", numpy.mean(data[:, 7]))
    # for i in range(numpy.shape(data)[0]):
    #     print(f"{browser} Mean Page {i+1} Loading Time: ", numpy.mean(data[i, 7]))
    print(f"{browser} Mean Loading Time (Exclude Page 1): ", numpy.mean(numpy.delete(data, 0, axis=0)[:, 7]))
    print("-------------------------------------------")
    print(f"{browser} Mean Blocked Time: ", numpy.mean(data[:, 8]))
    # for i in range(numpy.shape(data)[0]):
    #     print(f"{browser} Mean Page {i+1} Blocked Time: ", numpy.mean(data[i, 8]))
    print(f"{browser} Mean Blocked Time (Exclude Page 1): ", numpy.mean(numpy.delete(data, 0, axis=0)[:, 8]))
    print("-------------------------------------------")
    print(f"{browser} Mean Duration: ", numpy.mean(data[:, 9]))
    # for i in range(numpy.shape(data)[0]):
    #     print(f"{browser} Mean Page {i+1} Duration: ", numpy.mean(data[i, 9]))
    print(f"{browser} Mean Duration (Exclude Page 1): ", numpy.mean(numpy.delete(data, 0, axis=0)[:, 9]))
    print("-------------------------------------------")
    print(f"{browser} Mean Total Time: ", numpy.mean(total_times))
    # for i in range(numpy.shape(data)[0]):
    #     print(f"{browser} Mean Page {i+1} Total Time: ", numpy.mean(total_times[i]))
    print(f"{browser} Mean Total Time (Exclude Page 1): ", numpy.mean(numpy.delete(total_times, 0, axis=0)))
    print("-------------------------------------------")
    print(f"{browser} Mean Throughput: ", numpy.mean(data[:, 10]))
    # for i in range(numpy.shape(data)[0]):
    #     print(f"{browser} Mean Page {i+1} Throughput: ", numpy.mean(data[i, 10]))
    print(f"{browser} Mean Throughput (Exclude Page 1): ", numpy.mean(numpy.delete(data, 0, axis=0)[:, 10]))
    print("-------------------------------------------")

def print_medians(data, browser):
    total_times = numpy.sort((data[:, 8] + data[:, 9]))

    print(f"{browser} Median Startup Time: ", numpy.median(data[:, 0]))
    print(f"{browser} Median DNS Time: ", numpy.median(data[:, 1]))
    print(f"{browser} Median TCP Time: ", numpy.median(data[:, 2]))
    print(f"{browser} Median TLS Time: ", numpy.median(data[:, 3]))
    print(f"{browser} Median Wait Time: ", numpy.median(data[:, 4]))
    print(f"{browser} Median Receive Time: ", numpy.median(data[:, 5]))
    print(f"{browser} Median Process Time: ", numpy.median(data[:, 6]))
    print(f"{browser} Median Loading Time: ", numpy.median(data[:, 7]))
    print(f"{browser} Median Blocked Time: ", numpy.median(data[:, 8]))
    print(f"{browser} Median Total Time: ", numpy.median(total_times))
    print(f"{browser} Median Throughput: ", numpy.median(data[:, 10]))

def get_stats(data_file_1, data_file_2, data_file_3, data_name_1, data_name_2, data_name_3, site_name):
    d1 = numpy.load(data_file_1)
    d2 = numpy.load(data_file_2)
    d3 = numpy.load(data_file_3)
    d1_total_times = numpy.sort((d1[:, 8] + d1[:, 9]).flatten())
    d2_total_times = numpy.sort((d2[:, 8] + d2[:, 9]).flatten())
    d3_total_times = numpy.sort((d3[:, 8] + d3[:, 9]).flatten())

    # Total Time Histogram
    f1 = plt.figure(1)
    plt.title(f"{site_name} Total Time Histogram")
    plt.hist(d1_total_times, alpha=0.5, label=data_name_1, color='red')
    plt.hist(d2_total_times, alpha=0.5, label=data_name_2, color='yellow')
    plt.hist(d3_total_times, alpha=0.5, label=data_name_3, color='blue')
    plt.legend()
    plt.xlabel("Time (ms)")
    f1.show()

    # Throughput Histogram
    f2 = plt.figure(2)
    plt.title(f"{site_name} Throughput Histogram")
    plt.hist(numpy.sort((d1[:, 10]).flatten()), alpha=0.5, label=data_name_1, color='red')
    plt.hist(numpy.sort((d2[:, 10]).flatten()), alpha=0.5, label=data_name_2, color='yellow')
    plt.hist(numpy.sort((d3[:, 10]).flatten()), alpha=0.5, label=data_name_3, color='blue')
    plt.legend()
    plt.xlabel("Throughput (KB/s)")
    f2.show()

    # Total Time CDF
    f3 = plt.figure(3)
    plt.title(f"{site_name} Total Time CDF")
    y_cdf = numpy.array([i/d1_total_times.size for i in range(d1_total_times.size)])
    plt.plot(d1_total_times, y_cdf, label=data_name_1, color='red')
    plt.plot(d2_total_times, y_cdf, label=data_name_2, color='green')
    plt.plot(d3_total_times, y_cdf, label=data_name_3, color='blue')
    plt.legend()
    plt.vlines(numpy.percentile(d1_total_times, 95), 0, 0.95, color='red', linestyle='dotted')
    plt.vlines(numpy.percentile(d2_total_times, 95), 0, 0.95, color='green', linestyle='dotted')
    plt.vlines(numpy.percentile(d3_total_times, 95), 0, 0.95, color='blue', linestyle='dotted')
    plt.xlabel("Time (ms)")
    f3.show()

    # Mean Time Bar Plot
    f4, ax4 = plt.subplots()
    browsers = (data_name_1, data_name_2, data_name_3)
    weights = {
        "Startup": numpy.array([
            numpy.mean(d1[:, 0]),
            numpy.mean(d2[:, 0]),
            numpy.mean(d3[:, 0])
        ]),
        "DNS": numpy.array([
            numpy.mean(d1[:, 1]),
            numpy.mean(d2[:, 1]),
            numpy.mean(d3[:, 1])
        ]),
        "TCP": numpy.array([
            numpy.mean(d1[:, 2]),
            numpy.mean(d2[:, 2]),
            numpy.mean(d3[:, 2])
        ]),
        "TLS": numpy.array([
            numpy.mean(d1[:, 3]),
            numpy.mean(d2[:, 3]),
            numpy.mean(d3[:, 3])
        ]),
        "Wait": numpy.array([
            numpy.mean(d1[:, 4]),
            numpy.mean(d2[:, 4]),
            numpy.mean(d3[:, 4])
        ]),
        "Receive": numpy.array([
            numpy.mean(d1[:, 5]),
            numpy.mean(d2[:, 5]),
            numpy.mean(d3[:, 5])
        ]),
        "Process": numpy.array([
            numpy.mean(d1[:, 6]),
            numpy.mean(d2[:, 6]),
            numpy.mean(d3[:, 6])
        ]),
        "Loading": numpy.array([
            numpy.mean(d1[:, 7]),
            numpy.mean(d2[:, 7]),
            numpy.mean(d3[:, 7])
        ])
    }
    bottom = numpy.zeros(3)
    for boolean, weight in weights.items():
        ax4.bar(browsers, weight, width=0.5, bottom=bottom, label=boolean)
        bottom += weight
    plt.title(f"{site_name} Mean Time Breakdown")
    plt.legend()
    f4.show()

    # Mean Time Bar Plot (Exclude Page 1)
    f5, ax5 = plt.subplots()
    weights = {
        "Startup": numpy.array([
            numpy.mean(numpy.delete(d1, 0, axis=0)[:, 0]),
            numpy.mean(numpy.delete(d2, 0, axis=0)[:, 0]),
            numpy.mean(numpy.delete(d3, 0, axis=0)[:, 0])
        ]),
        "DNS": numpy.array([
            numpy.mean(numpy.delete(d1, 0, axis=0)[:, 1]),
            numpy.mean(numpy.delete(d2, 0, axis=0)[:, 1]),
            numpy.mean(numpy.delete(d3, 0, axis=0)[:, 1])
        ]),
        "TCP": numpy.array([
            numpy.mean(numpy.delete(d1, 0, axis=0)[:, 2]),
            numpy.mean(numpy.delete(d2, 0, axis=0)[:, 2]),
            numpy.mean(numpy.delete(d3, 0, axis=0)[:, 2])
        ]),
        "TLS": numpy.array([
            numpy.mean(numpy.delete(d1, 0, axis=0)[:, 3]),
            numpy.mean(numpy.delete(d2, 0, axis=0)[:, 3]),
            numpy.mean(numpy.delete(d3, 0, axis=0)[:, 3])
        ]),
        "Wait": numpy.array([
            numpy.mean(numpy.delete(d1, 0, axis=0)[:, 4]),
            numpy.mean(numpy.delete(d2, 0, axis=0)[:, 4]),
            numpy.mean(numpy.delete(d3, 0, axis=0)[:, 4])
        ]),
        "Receive": numpy.array([
            numpy.mean(numpy.delete(d1, 0, axis=0)[:, 5]),
            numpy.mean(numpy.delete(d2, 0, axis=0)[:, 5]),
            numpy.mean(numpy.delete(d3, 0, axis=0)[:, 5])
        ]),
        "Process": numpy.array([
            numpy.mean(numpy.delete(d1, 0, axis=0)[:, 6]),
            numpy.mean(numpy.delete(d2, 0, axis=0)[:, 6]),
            numpy.mean(numpy.delete(d3, 0, axis=0)[:, 6])
        ]),
        "Loading": numpy.array([
            numpy.mean(numpy.delete(d1, 0, axis=0)[:, 7]),
            numpy.mean(numpy.delete(d2, 0, axis=0)[:, 7]),
            numpy.mean(numpy.delete(d3, 0, axis=0)[:, 7])
        ])
    }
    bottom = numpy.zeros(3)
    for boolean, weight in weights.items():
        ax5.bar(browsers, weight, width=0.5, bottom=bottom, label=boolean)
        bottom += weight
    plt.title(f"{site_name} Mean Time Breakdown (Exclude Page 1)")
    plt.legend()
    f5.show()

    print(f"{site_name}\n")
    print_means(d1, data_name_1)
    print_means(d2, data_name_2)
    print_means(d3, data_name_3)
    print_medians(d1, data_name_1)
    print_medians(d2, data_name_2)
    print_medians(d3, data_name_3)
    print(f"{data_name_1} Total Time 95%: ", numpy.percentile(d1_total_times, 95))
    print(f"{data_name_2} Total Time 95%: ", numpy.percentile(d2_total_times, 95))
    print(f"{data_name_3} Total Time 95%: ", numpy.percentile(d3_total_times, 95))
    print(f"{data_name_1} Throughput 5%: ", numpy.percentile((d1[:, 10]), 5))
    print(f"{data_name_2} Throughput 5%: ", numpy.percentile((d2[:, 10]), 5))
    print(f"{data_name_3} Throughput 5%: ", numpy.percentile((d3[:, 10]), 5))
    input()
    plt.close('all')

def combine_data(browser):
    cern = numpy.load(f'cern_{browser}.npy')
    cnn = numpy.load(f'cnn_{browser}.npy')
    manpage = numpy.load(f'manpage_{browser}.npy')
    nos = numpy.load(f'nos_{browser}.npy')
    npr = numpy.load(f'npr_{browser}.npy')
    rfc = numpy.load(f'rfc_{browser}.npy')
    sports = numpy.load(f'sports_{browser}.npy')
    yarch = numpy.load(f'yarchive_{browser}.npy')
    return numpy.vstack((cern, cnn, manpage, nos, npr, rfc, sports, yarch))

def total_stats():
    data_ff = combine_data('firefox')
    data_chrome = combine_data('chrome')
    data_tor = combine_data('tor')

    ff_total_times = numpy.sort((data_ff[:, 8] + data_ff[:, 9]).flatten())
    chrome_total_times = numpy.sort((data_chrome[:, 8] + data_chrome[:, 9]).flatten())
    tor_total_times = numpy.sort((data_tor[:, 8] + data_tor[:, 9]).flatten())

    # Total Time Histogram
    f1 = plt.figure(1)
    plt.title("Total Time Histogram")
    plt.hist(ff_total_times, alpha=0.5, label="Firefox", color='red')
    plt.hist(chrome_total_times, alpha=0.5, label="Chrome", color='yellow')
    plt.hist(tor_total_times, alpha=0.5, label="Tor", color='blue')
    plt.legend()
    plt.xlabel("Time (ms)")
    f1.show()

    # Throughput Histogram
    f2 = plt.figure(2)
    plt.title("Throughput Histogram")
    plt.hist(numpy.sort((data_ff[:, 10]).flatten()), alpha=0.5, label="Firefox", color='red')
    plt.hist(numpy.sort((data_chrome[:, 10]).flatten()), alpha=0.5, label="Chrome", color='yellow')
    plt.hist(numpy.sort((data_tor[:, 10]).flatten()), alpha=0.5, label="Tor", color='blue')
    plt.legend()
    plt.xlabel("Throughput (KB/s)")
    f2.show()

    # Total Time CDF
    f3 = plt.figure(3)
    plt.title("Total Time CDF")
    y_cdf = numpy.array([i/ff_total_times.size for i in range(ff_total_times.size)])
    plt.plot(ff_total_times, y_cdf, label="Firefox", color='red')
    plt.plot(chrome_total_times, y_cdf, label="Chrome", color='green')
    plt.plot(tor_total_times, y_cdf, label="Tor", color='blue')
    plt.legend()
    plt.vlines(numpy.percentile(ff_total_times, 95), 0, 0.95, color='red', linestyle='dotted')
    plt.vlines(numpy.percentile(chrome_total_times, 95), 0, 0.95, color='green', linestyle='dotted')
    plt.vlines(numpy.percentile(tor_total_times, 95), 0, 0.95, color='blue', linestyle='dotted')
    plt.xlabel("Time (ms)")
    f3.show()

    # Mean Time Bar Plot
    f4, ax4 = plt.subplots()
    browsers = ("Firefox", "Chrome", "Tor")
    weights = {
        "Startup": numpy.array([
            numpy.mean(data_ff[:, 0]),
            numpy.mean(data_chrome[:, 0]),
            numpy.mean(data_tor[:, 0])
        ]),
        "DNS": numpy.array([
            numpy.mean(data_ff[:, 1]),
            numpy.mean(data_chrome[:, 1]),
            numpy.mean(data_tor[:, 1])
        ]),
        "TCP": numpy.array([
            numpy.mean(data_ff[:, 2]),
            numpy.mean(data_chrome[:, 2]),
            numpy.mean(data_tor[:, 2])
        ]),
        "TLS": numpy.array([
            numpy.mean(data_ff[:, 3]),
            numpy.mean(data_chrome[:, 3]),
            numpy.mean(data_tor[:, 3])
        ]),
        "Wait": numpy.array([
            numpy.mean(data_ff[:, 4]),
            numpy.mean(data_chrome[:, 4]),
            numpy.mean(data_tor[:, 4])
        ]),
        "Receive": numpy.array([
            numpy.mean(data_ff[:, 5]),
            numpy.mean(data_chrome[:, 5]),
            numpy.mean(data_tor[:, 5])
        ]),
        "Process": numpy.array([
            numpy.mean(data_ff[:, 6]),
            numpy.mean(data_chrome[:, 6]),
            numpy.mean(data_tor[:, 6])
        ]),
        "Loading": numpy.array([
            numpy.mean(data_ff[:, 7]),
            numpy.mean(data_chrome[:, 7]),
            numpy.mean(data_tor[:, 7])
        ])
    }
    bottom = numpy.zeros(3)
    for boolean, weight in weights.items():
        ax4.bar(browsers, weight, width=0.5, bottom=bottom, label=boolean)
        bottom += weight
    plt.title("Mean Time Breakdown")
    plt.legend()
    f4.show()

    print_means(data_ff, "Firefox")
    print_means(data_chrome, "Chrome")
    print_means(data_tor, "Tor")
    print_medians(data_ff, "Firefox")
    print_medians(data_chrome, "Chrome")
    print_medians(data_tor, "Tor")
    print("Firefox Total Time 95%: ", numpy.percentile(ff_total_times, 95))
    print("Chrome Total Time 95%: ", numpy.percentile(chrome_total_times, 95))
    print("Tor Total Time 95%: ", numpy.percentile(tor_total_times, 95))
    print("Firefox Throughput 5%: ", numpy.percentile((data_ff[:, 10]), 5))
    print("Chrome Throughput 5%: ", numpy.percentile((data_chrome[:, 10]), 5))
    print("Tor Throughput 5%: ", numpy.percentile((data_tor[:, 10]), 5))

    input()
    

sites = ['NPR', 'NOS', 'CNN', 'CERN', 'Manpage', 'RFC', 'Sports', 'Yarchive']
for site in sites:
    get_stats(f"{site}_firefox.npy", f"{site}_chrome.npy", f"{site}_tor.npy", 'Firefox', 'Chrome', 'Tor', site)
    get_stats(f"{site}_firefox.npy", f"{site}_firefox_DE.npy", f"{site}_tor.npy", 'Firefox', 'VPN (DE)', 'Tor', site)

total_stats()

# Count different locations
all_loc_string = ""
loc_files = ['cern_locations.txt', 'cnn_locations.txt', 'manpage_locations.txt', 'nos_locations.txt', 'npr_locations.txt', 'rfc_locations.txt', 'sports_locations.txt', 'yarchive_locations.txt']
for loc in loc_files:
    file = open(loc)
    contents = file.read()
    file.close()
    all_loc_string += contents[1:(len(contents)-2)]
    all_loc_string += ", "
print(numpy.unique(re.split(', ', all_loc_string), return_counts=True))