#!/usr/bin/env python3

import pandas as pd
import requests
import json
import time

# modify these values as needed

# insert your own API Key (see README)
RAPID_API_KEY = ""
REFS_TEXT_FILE = "./refs.txt"
OUTPUT_FILE_PATH = "./refs-links.csv"


# helper functions
def get_title_from_ref(string):
    """Returns the title string from the full reference. Currently, this only works if the title is the longest line of the reference object"""
    return(max(string.split(.), key=len).strip().replace('"', '').replace("'", ''))

def create_request_url(title):
    """Replaces space characters with '+' to form a suitable query string for the API"""
    q_string = title.replace(' ', '+')
    return f"https://google-search3.p.rapidapi.com/api/v1/search/q={q_string}num=2"

def get_request_data(i, title):
    """Retrieves a link for a given title from the references.
            
            - if no link is found: return 'no link found'
            - if error on req:     return 'request failed'
    """
    
    headers = {
        'x-rapidapi-key': RAPID_API_KEY,
        'x-rapidapi-host': "google-search3.p.rapidapi.com"
    }
    
    query_s = create_request_url(title)
    
    link = ""

    # if you want a verbose output for each link, uncomment the print statements
    
    # print(f"Getting link for [{i}]: {title[:20]}...")
    
    try:
        r = requests.request("GET", query_s, headers=headers)
    except ConnectionError:
        pass
        
    if r.status_code == 200:
        j = json.loads(r.text)
        try:
            link += j['results'][0]['link']
        except:
            link += 'no link found'
    else:
        link += 'request failed'

    # print(f"Done: [{link}]")

    return link


# functional script

# create dataframe from REFS_TEXT_FILE
df = pd.read_csv(REFS_TEXT_FILE, delimiter='\n', header=None, names=['ref_full'])

# create title column from full text
df['title'] = df['ref_full'].apply(lambda x: get_title_from_ref(x))

# search for link using title
start = time.time()
links = []
for i, j in df.iterrows():
    link = get_request_data(i, j['title'])
    links.append(link)

delta = time.time() - start

# add the links to the dataframe
df['link'] = links

# save the output file with the links
df.index += 1
df.to_csv(OUTPUT_FILE_PATH)

print(f"Finished - output file: {OUTPUT_FILE_PATH}\n Total time = {delta:.2f seconds}")