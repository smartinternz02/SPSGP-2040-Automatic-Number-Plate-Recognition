import requests

url = "https://zyanyatech1-license-plate-recognition-v1.p.rapidapi.com/recognize_url"

querystring = {"image_url":"http://eslamoda.com/wp-content/uploads/sites/2/2014/11/america-carro-600x600.jpg"}

headers = {
    'x-rapidapi-key': "d9a2b6475emsh890c2568688f89fp1d481ajsn28c7cb4f8a78",
    'x-rapidapi-host': "zyanyatech1-license-plate-recognition-v1.p.rapidapi.com"
    }

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)