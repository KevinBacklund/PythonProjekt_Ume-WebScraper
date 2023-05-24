import requests
import json
import matplotlib.pyplot as plot


def main():
    req=requests.get("https://opendata.umea.se/api/records/1.0/search/?dataset=befolkningsfoeraendringar-helar&q=")
    dict = json.loads(req.text)
    with open("befolkning.json","w") as datafh:
        json.dump(dict, datafh, indent=4)
    befolkning = joson_search()
    befolkningsorted = {}
    for ar in sorted(befolkning):
        befolkningsorted.update({ar:befolkning[ar]})
    graf(befolkningsorted)

def graf(befolkningsorted):
    fig, ax = plot.subplots()
    ax.plot(befolkningsorted.keys(),befolkningsorted.values())
    ax.set_title("Umeå befolkning")
    ax.set_xlabel("år")
    ax.set_ylabel("befolkning")
    plot.show()

def joson_search():
    with open("befolkning.json") as datafh:
        data = json.load(datafh)
    records = data["records"]
    fields = []
    for key in records:
        fields.append(key["fields"])
    befolkning = {}
    for field in fields:
        befolkning.update({field["ar"]:field["folkmangd"]})
    return befolkning

if __name__ == '__main__':
    main()