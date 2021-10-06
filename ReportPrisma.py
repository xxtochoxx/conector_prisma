import requests
import json
from FunctionsPrisma import generateCSV
from FunctionsPrisma import import_defect_dojo

images_file = open('recursos/Imagenes.csv', 'r')

for name in images_file:
    name_image = name.strip()+str(':*')#Formato para API Prisma
    image = name.strip().split('/')[1]
    #name_json = image+str('.json')
    #name_csv = image+str('.csv')
    name_json = 'reportes/' + name.strip()+str('.json')
    name_csv = 'reportes/' + name.strip()+str('.csv')
    
    url = 'https://us-west1.cloud.twistlock.com/us-3-159241997/api/v1/scans?search=' + str(name_image) + '&limit=1&reverse=true&type=ciImage'
    #response = requests.get('https://us-west1.cloud.twistlock.com/us-3-159241997/api/v1/scans?search=jrvs-des/ach-fulfillment:*&limit=1&reverse=true&type=ciImage', 
    response = requests.get(url, 
    auth=('2661a1e3-a002-4d1a-bfd2-c997f621d454', 'nPNIhOngTxHakm8Ssv53m8Ap85M='))
    
    with open(name_json, 'w') as file_json:
        json.dump(response.json(), file_json)
        file_json.close()
        generateCSV(name_json,name_csv)
    #import_defect_dojo(name_csv)
print ("Se generaron los reportes")