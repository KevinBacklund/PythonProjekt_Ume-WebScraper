import requests
import json
import matplotlib.pyplot as plot


def main():
    req=requests.get("https://opendata.umea.se/api/records/1.0/search/?dataset=befolkningsfoeraendringar-helar&q=")
    dict = json.loads(req.text)
    with open("befolkning.json","w") as datafh:
        json.dump(dict, datafh, indent=4)
    print("Tillgänglig data:")
    printFields()
    while True:
        cmdline = input(">")
        if cmdline != "sluta":
            befolkning = joson_search(cmdline)
            if befolkning != "fel":
                befolkningsorted = {}
                for ar in sorted(befolkning):
                    befolkningsorted.update({ar:befolkning[ar]})
                graf(befolkningsorted, cmdline)
        if cmdline == "sluta":
            break

def graf(befolkningsorted, title):
    fig, ax = plot.subplots()
    ax.plot(befolkningsorted.keys(),befolkningsorted.values())
    ax.set_title(f"Umeå {title}")
    ax.set_xlabel("år")
    ax.set_ylabel("befolkning")
    plot.show()

def joson_search(searchterm):
    fields = FindFields()
    befolkning = {}
    try:
        for field in fields:
            befolkning.update({field["ar"]:field[searchterm]})
        return befolkning
    except KeyError:
        print("Denna data finns inte")
        return "fel"

def FindFields():
    with open("befolkning.json") as datafh:
        data = json.load(datafh)
    records = data["records"]
    fields = []
    for key in records:
        fields.append(key["fields"])
    return fields
def printFields():
    fields = FindFields()
    fieldstr = ""
    for field in fields[0].keys():
        if field != "ar":
            fieldstr += f"\n{field}"
    print(fieldstr)

if __name__ == '__main__':
    main()