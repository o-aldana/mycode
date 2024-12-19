#!/usr/bin/python3


# 3rd party library
import requests

# Define URL as a global constant (this will not change)
MAJORTOM = 'https://api.coindesk.com/v1/bpi/currentprice.json'

def main():
    """making API requests"""
    
    # Call the web service
    resp = requests.get(MAJORTOM)  # sends an HTTP GET
    
    # strip JSON data off response and convert
    # to python data types
    data = resp.json()
            
    # display our Pythonic data
    #print("\n\nConverted Python data")
    #print(data)
    

    usd_amt = data['bpi']['USD']['rate']
    print('Bitcoin in USD is',usd_amt)
    
    #astros = data.get('people') # people is a list of dict
    #print(astros) # this is the list of dict

    # for-loop across astros
    # display names of those in space
    #for astro in astros:
    #    print(f"Riding on the {astro['craft']} is:", astro['name'])

if __name__ == '__main__':
    main()

