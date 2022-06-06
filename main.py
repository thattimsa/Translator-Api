# მოდულების იმპორტი
import json
import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
Text = input("ჩაწერე ტექსტი ინგლისურად: ")
payload = f'q={Text}&target=geo&source=en'
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
	"X-RapidAPI-Key": "387c6bd0a3msh34af642f823e62fp155357jsn771561bafcc1"
}


# შენახვა
response = requests.request("POST", url, data=payload, headers=headers)
result_json = response.text
res = json.loads(result_json)
res_structurised = json.dumps(res, indent=4)

print(res_structurised)

print(response.text)
