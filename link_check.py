import pandas as pd
import requests

# Reading links from the Excel file
def read_links_from_excel(file_path):
    df = pd.read_excel(file_path, engine='openpyxl')
    return df['links'].tolist()  

# Checking link validity
def check_link(link):
    try:
        response = requests.head(link, timeout=5)  # Using HEAD request instead of GET to be faster
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        return False

# Main function
def main():
    links = read_links_from_excel("path_to_your_excel_file") 
    valid_links = []
    invalid_links = []
    for link in links:
        if check_link(link):
            valid_links.append(link)
        else:
            invalid_links.append(link)
    
    print("Valid links:", valid_links)
    print("Invalid links:", invalid_links)

if __name__ == "__main__":
    main()
