import requests
file_path= input("enter the path to the file you want to scan")
APIkey= '631396087b7bdcd13074d93bccf5a69c8b5462ee5cc9018ddc4e1354e0df8137'

def scanFile(APIkey, file_path):
    url= 'https://www.virustotal.com/vtapi/v2/url/scan'
    params = {'apikey': APIkey}
    files = {'file': open(file_path, 'rb')}
    request = requests.post(url, files=files, params=params)
    json_result = request.json()

    if isinstance(json_result, list):
        for result in json_result:
            if result.get('response_code') == 1:
                if result.get('positives', 0) == 0:
                    return "your file is secure"
                else:
                    return "your file is not secure"
        return "Error, can't determine the file security status"
    else:
        return "Eror, something went wrong"
    
finalResult = scanFile(APIkey, file_path)
print("File submitted for scanning. your result:", finalResult)