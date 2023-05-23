import requests
import json
import matplotlib.pyplot as plot
#requests Get JSON
#JSON -> Dict(år:befolkning
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
    befolkning = {}
    for field in fields:
        befolkning.update({field["ar"]:field["folkmangd"]})
    print(befolkning)
    befolkningsorted = {}
    for a in sorted(befolkning):
        befolkningsorted.update({a:befolkning[a]})
    fig, ax = plot.subplots()
    ax.plot(befolkningsorted.keys(),befolkningsorted.values())
    ax.set_title("Umeå befolkning")
    ax.set_xlabel("år")
    ax.set_ylabel("befolkning")
    plot.show()
if __name__ == '__main__':
    main()