import requests
import json
#requests Get JSON
#JSON -> list[Dict(år:befolkning)]
#Dict -> matplotlib graf

def main():
    req=requests.get("https://opendata.umea.se/api/records/1.0/search/?dataset=befolkningsfoeraendringar-helar&q=")
    dict = json.loads(req.text)
    with open("befolkning.json","w") as datafh:
        json.dump(dict, datafh, indent=4)
    with open("befolkning.json") as datafh:
        data = json.load(datafh)
    records = data["records"]
    fields = []
    for key in records:
        fields.append(key["fields"])
    befolkning = []
    for field in fields:
        print(field["ar"])
        print(field["folkmangd"])
        befolkning.append({field["ar"]:field["folkmangd"]})
    print(befolkning)

if __name__ == '__main__':
    main()