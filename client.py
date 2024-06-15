import requests
file_path= input("enter the path to the file you want to scan: ")
APIkey= '631396087b7bdcd13074d93bccf5a69c8b5462ee5cc9018ddc4e1354e0df8137'

def scanFile(APIkey, file_path):
    url= 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': APIkey}
    files = {'file': open(file_path, 'rb')}
    request = requests.post(url, data=params, files=files)

   
finalResult = scanFile(APIkey, file_path)
print("File submitted for scanning. your result:", finalResult)