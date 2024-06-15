import requests
file_path= input("enter the path to the file you want to scan: ")
APIkey= '631396087b7bdcd13074d93bccf5a69c8b5462ee5cc9018ddc4e1354e0df8137'

def UploadFileToServer(APIkey, file_path):
    urlPost= 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': APIkey}
    files = {'file': open(file_path, 'rb')}
    request = requests.post(urlPost, data=params, files=files)
    
    if request.status_code == 200:
        if request.headers['Content-Type'] == 'application/json':
            return request.json()['resource']
    else:
        print("Error, something went wrong.")
        
def ServerResponse(file_id):
    urlGet= 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': APIkey, 'resource': file_id}
    request = requests.get(urlGet, params=params)
   
    if request.status_code == 200:
        if request.headers['Content-Type'] == 'application/json':
            respond= request.json()
            for result in respond['scans'].items():
                if result['detected'] == True:
                    return True
                else:
                    return False
    else:
        print("Error, something went wrong.")
   
file_id = UploadFileToServer(APIkey, file_path)
finalResult = ServerResponse(file_id)
if finalResult:
    print("your file has a virus.")
else:
    print("your file is virus free!")