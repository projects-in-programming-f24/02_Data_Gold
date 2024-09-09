import requests
from bs4 import BeautifulSoup
import random

def scape_the_facts(url, num_facts=5):
    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"failed to get the webpage: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        
        facts_list = soup.find_all('p', class_="list")

        # use regex to strip the <p> tags (e.g., just show the content)
        facts = [item.text.strip() for item in facts_list] # this is neat

        return random.sample(facts, min(num_facts, len(facts))) # choose a random sampling of facts from facts that's our # of facts
    
    except Exception as e:
        print(f"An error has occured: {e}")
        return []

def main():
    url = "https://www.thefactsite.com/1000-interesting-facts/"

    facts = scape_the_facts(url)

    for i, fact in enumerate(facts, 1):
        print(f"{i}: {fact}")

# boilerplate to run the main() function
if __name__ == "__main__":
    main()