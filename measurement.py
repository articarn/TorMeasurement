import time
import numpy
from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ExpectedConditions
from selenium.webdriver.support.wait import WebDriverWait

numpy.set_printoptions(suppress=True)
Metrics = namedtuple('Metrics', 'startup_time, dns_time, tcp_time, tls_time, wait_time, receive_time, process_time, loading_time, blocked_time, duration, throughput, transferSize')
NUM_METRICS = 12 # number of fields in the Metrics tuple
BROWSER = "Chrome"
USE_VPN = True
VPN_LOC = "DE"
num_samples = 10

def test_npr():
    # First dimension: links accessed - NPR home page and the first ten articles (11)
    # Second dimension: metrics
    # Third dimension: samples
    data = numpy.zeros(shape=(11, NUM_METRICS, num_samples))
    locations = list()

    for sample in range(num_samples):
        match BROWSER:
            case "Tor":
                driver = tor_setup()
                locations.append(get_tor_exit_node_location(driver))
            case "Firefox":
                driver = firefox_setup()
            case "Chrome":
                driver = chrome_setup()

        # Navigate to NPR home page
        calc_timing_metrics("https://text.npr.org/", driver, data, 0, sample)

        # Retrieve article links from home page
        articles = driver.find_elements(By.CLASS_NAME, "topic-title")
        article_links = [article.get_attribute('href') for article in articles]

        # Retreive/record metrics for first ten links
        for i in range(10):
            calc_timing_metrics(article_links[i], driver, data, i+1, sample) # +1 because of home page
        teardown(driver)
    write_data_to_file("npr", data, locations)

def test_nos():
    data = numpy.zeros(shape=(11, NUM_METRICS, num_samples))
    locations = list()

    for sample in range(num_samples):
        match BROWSER:
            case "Tor":
                driver = tor_setup()
                locations.append(get_tor_exit_node_location(driver))
            case "Firefox":
                driver = firefox_setup()
            case "Chrome":
                driver = chrome_setup()

        # Navigate to NOS home page
        calc_timing_metrics("https://noslite.nl/", driver, data, 0, sample)

        # Retrieve article links from home page
        articles = driver.find_elements(By.CSS_SELECTOR, "a")
        article_links = [article.get_attribute('href') for article in articles]

        # Retreive/record metrics for first ten links
        for i in range(10):
            calc_timing_metrics(article_links[i], driver, data, i+1, sample) # +1 because of home page
        teardown(driver)
    write_data_to_file("nos", data, locations)

def test_cnn():
    data = numpy.zeros(shape=(11, NUM_METRICS, num_samples))
    locations = list()

    for sample in range(num_samples):
        match BROWSER:
            case "Tor":
                driver = tor_setup()
                locations.append(get_tor_exit_node_location(driver))
            case "Firefox":
                driver = firefox_setup()
            case "Chrome":
                driver = chrome_setup()

        # Navigate to CNN home page
        calc_timing_metrics("https://lite.cnn.com/", driver, data, 0, sample)

        # Retrieve article links from home page
        articles = driver.find_elements(By.CSS_SELECTOR, "a")
        article_links = [article.get_attribute('href') for article in articles]

        # Retreive/record metrics for first ten links
        for i in range(10):
            calc_timing_metrics(article_links[i], driver, data, i+1, sample) # +1 because of home page
        teardown(driver)
    write_data_to_file("cnn", data, locations)

def test_cern():
    data = numpy.zeros(shape=(12, NUM_METRICS, num_samples))
    locations = list()

    for sample in range(num_samples):
        match BROWSER:
            case "Tor":
                driver = tor_setup()
                locations.append(get_tor_exit_node_location(driver))
            case "Firefox":
                driver = firefox_setup()
            case "Chrome":
                driver = chrome_setup()

        # Metrics for CERN landing page
        calc_timing_metrics("https://info.cern.ch/", driver, data, 0, sample)

        # Metrics for WWW Project page
        calc_timing_metrics("https://info.cern.ch/hypertext/WWW/TheProject.html", driver, data, 0, sample)

        # Retrieve hyperlink addresses on WWW Project page
        link_elems = driver.find_elements(By.CSS_SELECTOR, "a")
        links = [link_elem.get_attribute('href') for link_elem in link_elems]
        
        # Retreive/record metrics for first ten links
        for i in range(10):
            calc_timing_metrics(links[i], driver, data, i+2, sample) # +2 because of landing/www pages
        teardown(driver)
    write_data_to_file("cern", data, locations)

def test_manpage():
    data = numpy.zeros(shape=(11, NUM_METRICS, num_samples))
    locations = list()

    for sample in range(num_samples):
        match BROWSER:
            case "Tor":
                driver = tor_setup()
                locations.append(get_tor_exit_node_location(driver))
            case "Firefox":
                driver = firefox_setup()
            case "Chrome":
                driver = chrome_setup()
        
        # Metrics for man page ToC
        calc_timing_metrics("https://manpages.bsd.lv/toc.html", driver, data, 0, sample)

        # Retrieve hyperlink addresses from ToC
        link_elems = driver.find_elements(By.CSS_SELECTOR, "a")
        links = [link_elem.get_attribute('href') for link_elem in link_elems]

        # Retreive/record metrics for first ten links
        for i in range(10):
            calc_timing_metrics(links[i], driver, data, i+1, sample) # +1 because of ToC page
        teardown(driver)
    write_data_to_file("manpage", data, locations)

def test_rfc():
    data = numpy.zeros(shape=(11, NUM_METRICS, num_samples))
    locations = list()

    for sample in range(num_samples):
        match BROWSER:
            case "Tor":
                driver = tor_setup()
                locations.append(get_tor_exit_node_location(driver))
            case "Firefox":
                driver = firefox_setup()
            case "Chrome":
                driver = chrome_setup()
        
        # Metrics for first 100 RFCs (ascending)
        calc_timing_metrics("https://www.rfc-editor.org/rfc-index-100a.html", driver, data, 0, sample)

        # Metrics for all RFCs (ascending)
        asc_all_link = driver.find_element(By.LINK_TEXT, "Show All").get_attribute('href')
        calc_timing_metrics(asc_all_link, driver, data, 1, sample)

        # Metrics for first 100 RFCs (descending)
        calc_timing_metrics("https://www.rfc-editor.org/rfc-index-100d.html", driver, data, 2, sample)

        # Metrics for all RFCs (descending)
        desc_all_link = driver.find_element(By.LINK_TEXT, "Show All").get_attribute('href')
        calc_timing_metrics(desc_all_link, driver, data, 3, sample)

        # Metrics for all RFCs with no hyperlinks
        calc_timing_metrics("https://www.rfc-editor.org/rfc-index.txt", driver, data, 4, sample)

        # Metrics for IP RFC
        calc_timing_metrics("https://www.rfc-editor.org/rfc/rfc791.txt", driver, data, 5, sample)

        # Metrics for TCP RFC
        calc_timing_metrics("https://www.rfc-editor.org/rfc/rfc9293.txt", driver, data, 6, sample)

        # Metrics for QUIC RFC
        calc_timing_metrics("https://www.rfc-editor.org/rfc/rfc9000.txt", driver, data, 7, sample)

        # Metrics for HTTP3 RFC
        calc_timing_metrics("https://www.rfc-editor.org/rfc/rfc9114.txt", driver, data, 8, sample)

        # Metrics for TLS 1.3 RFC
        calc_timing_metrics("https://www.rfc-editor.org/rfc/rfc8446.txt", driver, data, 9, sample)

        # Metrics for CUBIC RFC
        calc_timing_metrics("https://www.rfc-editor.org/rfc/rfc8312.txt", driver, data, 10, sample)
    
        teardown(driver)
    write_data_to_file("rfc", data, locations)
        
def test_sports():
    data = numpy.zeros(shape=(11, NUM_METRICS, num_samples))
    locations = list()

    for sample in range(num_samples):
        match BROWSER:
            case "Tor":
                driver = tor_setup()
                locations.append(get_tor_exit_node_location(driver))
            case "Firefox":
                driver = firefox_setup()
            case "Chrome":
                driver = chrome_setup()

        # Metrics for sports home page
        calc_timing_metrics("https://plaintextsports.com/", driver, data, 0, sample)

        # Retrieve links for all schedules
        sched_link_elems = driver.find_elements(By.LINK_TEXT, "Schedule")
        sched_links = [elem.get_attribute('href') for elem in sched_link_elems]

        # Retrieve links for all standings
        stand_link_elems = driver.find_elements(By.LINK_TEXT, "Standings")
        stand_links = [elem.get_attribute('href') for elem in stand_link_elems]

        # Combine links into one list
        # Retreive/record metrics for first ten links
        links = sched_links + stand_links
        for i in range(10):
            calc_timing_metrics(links[i+1], driver, data, i+1, sample) # +1 because of home page
        teardown(driver)
    write_data_to_file("sports", data, locations)

def test_yarchive():
    data = numpy.zeros(shape=(12, NUM_METRICS, num_samples))
    locations = list()

    for sample in range(num_samples):
        match BROWSER:
            case "Tor":
                driver = tor_setup()
                locations.append(get_tor_exit_node_location(driver))
            case "Firefox":
                driver = firefox_setup()
            case "Chrome":
                driver = chrome_setup()

        # Metrics for yarchive home page
        calc_timing_metrics("https://yarchive.net/", driver, data, 0, sample)

        # Metrics for 'Computers' page
        comp_link = driver.find_element(By.LINK_TEXT, "Computers").get_attribute('href')
        calc_timing_metrics(comp_link, driver, data, 1, sample)

        # Retrieve hyperlink addresses on 'Computers' page
        link_elems = driver.find_elements(By.CSS_SELECTOR, "a")
        links = [link_elem.get_attribute('href') for link_elem in link_elems]
        
        # Retreive/record metrics for first ten links
        # Skip the first two links (home page and about page)
        for i in range(10):
            calc_timing_metrics(links[i+2], driver, data, i+1, sample) # +2 because of home/Computer pages
        teardown(driver)
    write_data_to_file("yarchive", data, locations)

# Calculate timing metrics and save them to the supplied data matrix
def calc_timing_metrics(link, driver, data, link_num, sample_num):
    start = time.time()
    driver.get(link)
    end = time.time()

    # Time elapsed (in ms) for driver to link
    total_time = (end - start) * 1000

    # Retrieve PerformanceNavigationTiming information from Firefox
    # NOTE: the executed script returns an array, but there should only be one entry
    perf_entry = driver.execute_script(f"return performance.getEntriesByName(\"{link}\")")[0]

    # Most of these timing metrics are calculated as described at
    # https://developer.mozilla.org/en-US/docs/Web/API/Performance_API/Resource_timing
    startup_time = perf_entry['domainLookupStart'] - perf_entry['startTime']
    dns_time = perf_entry['domainLookupEnd'] - perf_entry['domainLookupStart']
    tcp_time = perf_entry['connectEnd'] - perf_entry['connectStart']
    tls_time = perf_entry['requestStart'] - perf_entry['secureConnectionStart']
    wait_time = perf_entry['responseStart'] - perf_entry['requestStart'] # aka request time
    receive_time = perf_entry['responseEnd'] - perf_entry['responseStart']
    process_time = perf_entry['domContentLoadedEventStart'] - perf_entry['responseEnd']
    loading_time = perf_entry['loadEventEnd'] - perf_entry['domContentLoadedEventStart'] # DOMContentLoaded and load events
    blocked_time = total_time - perf_entry['duration'] # remaining time is the difference between total_time and duration
    throughput = perf_entry['transferSize'] / total_time;
    metrics = Metrics(startup_time, dns_time, tcp_time, tls_time, wait_time, receive_time, process_time, loading_time, blocked_time, perf_entry['duration'], throughput, perf_entry['transferSize'])

    # Write metrics to data matrix
    for i in range(NUM_METRICS):
        data[link_num, i, sample_num] = metrics[i]

def get_tor_exit_node_location(driver):
    driver.get("https://check.torproject.org/")
    relay_search_element = driver.find_element(By.LINK_TEXT, "Relay Search")
    relay_search_link = relay_search_element.get_attribute('href')
    driver.get(relay_search_link)
    country = (WebDriverWait(driver, 10)).until(ExpectedConditions.any_of(
        ExpectedConditions.presence_of_element_located(
            (By.ID, "tip.inline.country")
        ),
        ExpectedConditions.presence_of_element_located(
            (By.CLASS_NAME, "inline.country")
        )
    ))
    location = country.get_attribute("title") if country.get_attribute("title") else country.get_attribute("alt")
    return location

def write_data_to_file(name, data, locations):
    match BROWSER:
        case "Tor":
            numpy.save(f'{name}_tor', data)
            f = open(f'{name}_locations.txt', 'w')
            print(locations, file=f)
        case "Firefox":
            if USE_VPN:
                numpy.save(f'{name}_firefox_{VPN_LOC}', data)
            else:
                numpy.save(f'{name}_firefox', data)
        case "Chrome":
            if USE_VPN:
                numpy.save(f'{name}_chrome_{VPN_LOC}', data)
            else:
                numpy.save(f'{name}_chrome', data)

# Tor Driver Setup
def tor_setup():
    # Disable caching
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference('network.cookie.cookieBehavior', 2)

    # Open Tor Firefox instance
    options = webdriver.FirefoxOptions()
    options.profile = profile
    options.binary_location = "C:\\Tor Browser\\Browser\\firefox.exe"
    driver = webdriver.Firefox(options)

    # Find "Connect" button on Tor landing page
    connect_button = driver.find_element(By.ID, "connectButton")
    connect_button.click()
    time.sleep(2) # wait until connection is established (hard coded to wait for 2 seconds... hopefully is sufficient)

    # Navigate to example Selenium web form (not strictly necessary, but done as a baseline)
    # For some reason, calling it once does nothing in Tor...
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    return driver

# Firefox Driver Setup
def firefox_setup():
    # Disable caching
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference('network.cookie.cookieBehavior', 2)
    options = webdriver.FirefoxOptions()
    options.profile = profile

    driver = webdriver.Firefox(options)
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    return driver

# Chrome Driver Setup
def chrome_setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disk-cache-size=0")

    driver = webdriver.Chrome(options)
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    return driver

def teardown(driver):
    driver.quit()
