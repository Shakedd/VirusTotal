import requests
file_path= input("enter the path to the file you want to scan: ")
APIkey= '631396087b7bdcd13074d93bccf5a69c8b5462ee5cc9018ddc4e1354e0df8137'

def scanFile(APIkey, file_path):
    url= 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': APIkey}
    files = {'file': open(file_path, 'rb')}
    request = requests.post(url, data=params, files=files)
    
    if request.status_code == 200:
        if request.headers['Content-Type'] == 'application/json':
            return request.json()['resorce']
    else:
        print("Error, something went wrong.")
   
finalResult = scanFile(APIkey, file_path)
print("File submitted for scanning. your result:", finalResult)