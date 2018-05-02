import requests
import json
import csv
import pandas as pd
import time

with open('Transactions.csv','a') as f: # Use this line to open up a csv file that you will write into. 


    while True:
        data_request=requests.get('https://api.blockcypher.com/v1/eth/main/txs') # Makes API call to BlockCypher. This will generate a response that contains the data we want.
        json=data_request.json() # Makes sure that API response is JSON
        df = pd.DataFrame(json,dtype=object) # Turns JSON response into a Dataframe, a data structure supported by Python's Pandas module.
        [df.to_csv(f, header=False) for i in range (1)] # Loads data frame into the csv. The dataframe will contain multiple rows of data
        time.sleep(120) #Script sleeps for 120 seconds to give the API a break. You can reduce the time it sleeps, but you will likely have your API limits throttled (unless you pay for more)
