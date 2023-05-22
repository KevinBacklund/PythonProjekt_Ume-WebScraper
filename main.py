import requests
#requests Get JSON
#JSON -> Dict(år:befolkning)
#Dict -> matplotlib graf

def main():
    req=requests.get("https://opendata.umea.se/api/records/1.0/search/?dataset=befolkningsfoeraendringar-helar&q=")
    print(req.content)

if __name__ == '__main__':
    main()