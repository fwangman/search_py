from serpapi import GoogleSearch
import requests
import csv

dict_count = {}

search = GoogleSearch({
    "q": "russell",
    "num": "100",
    "google_domain": "google.com",
    "api_key": "fc465b9c9b14ba2a51677de70a30a33c2f89a9355707b8e9fd48115398972ac8"
  })
result = search.get_dict()

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["title", "link"])
    for i in result["organic_results"]:
        print(i["title"])
        print(i["link"])
        writer.writerow([i["title"], i["link"]])
        #try:
        #    r = requests.get(i["link"])
            #print(r.text)
        #except requests.exceptions.RequestException as e:
        #    print(i["link"] + "failed")


