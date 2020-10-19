import os
import sys
from urllib.request import urlopen

def scrapeJson():
    print("Scrape JSON")
    return 0

def exportCSV():
    print("Export CSV")
    return 0

if __name__ == "__main__":
    print ('Argument List:', str(sys.argv))
    supportedFormats = ["JSON", "CSV"]
    if (len(sys.argv) != 4):
        print("Usage:")
        print("python3 main.py <URL> <StoreName> <Format-Type>")
        print("Format-Type: JSON/CSV")
        print("Ex: python3 main.py https://www.pizzahut.com.au/stores JSON")
    elif(sys.argv[3] not in supportedFormats):
        print("Invalid Format Type:", sys.argv[3])
    else:
        print(">>> Welcome to Web Scraper <<<")
        input_url = sys.argv[1]
        store_name = sys.argv[2]
        format_type = sys.argv[3]
        print("\tInput URL = ",input_url)
        print("\tStore Name = ",store_name)
        print("\tFormat Type = ",format_type)
        page = urlopen(sys.argv[1])
        html_bytes = page.read()
        html_code = html_bytes.decode("utf-8")
        print(html_code)