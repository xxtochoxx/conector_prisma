import json
import csv
import requests

# Define a function `plus()`
def generateCSV(name_json,name_csv):

    with open(name_json) as json_file:
        data = json.load(json_file)
    
    data_file = open(name_csv, 'w')
    csv_writer = csv.writer(data_file)
     
    header = ['Registry','Repository','Tag','Id','Scan Time','Pass','Type','Distro','Hostname','Layer','CVE ID','Compliance ID','Type','Severity','Packages','Source Package','Package Version','Package License','CVSS','Fix Status','Fix Date','Grace Days','Vulnerability Tags','Description','Cause','Published','Custom Labels'] 
    vulnerability = []
    csv_writer.writerow(header)
     
    for values   in data:
            for tag in values['entityInfo']['tags']:
                registry = (tag['registry'])#OK column1
                repo = tag['repo']#OK column2
                tag = tag['tag']#OK column3
            ent_id = values['entityInfo']['id']#OK column4
            ent_scanTime = values['entityInfo']['scanTime']#OK column5
            v_pass = values['pass']#OK column6
            ent_type = values['entityInfo']['type']#OK column7
            ent_distro = values['entityInfo']['distro']#OK column8
            ent_hostname = values['entityInfo']['hostname']#OK column9
            for vuln in values['entityInfo']['vulnerabilities']:
                vulnerability = []
                vulnerability = [registry,repo,tag,ent_id,ent_scanTime,v_pass,ent_type,ent_distro,ent_hostname,'']#OK column10 ' '
                vulnerability.append(vuln['cve'])#OK column11
                vulnerability.append(vuln['id'])#OK column12
                if vuln['id'] ==  46:
                    tipo = 'SO'
                if vuln['id'] ==  47:
                    tipo = 'java'
                if vuln['id'] ==  411:
                    tipo = 'binary'
                if vuln['id'] ==  424:
                    tipo = 'twistlock'
                vulnerability.append(tipo)#OK column13
                vulnerability.append(vuln['severity'])#OK column14
                vulnerability.append(vuln['packageName'])#OK column15
                vulnerability.append('')#OK column16
                vulnerability.append(vuln['packageVersion'])#OK column17
                vulnerability.append('')#OK column18
                vulnerability.append(vuln['cvss'])#OK column19
                vulnerability.append(vuln['status'])#OK column20
                vulnerability.append(vuln['fixDate'])#OK column21
                vulnerability.append('')#OK column22
                vulnerability.append('')#OK column23
                vulnerability.append(vuln['description'])#OK column24
                vulnerability.append(vuln['cause'])#OK column25
                vulnerability.append(vuln['published'])#OK column26
                vulnerability.append('')#OK column27
                csv_writer.writerow(vulnerability) # Escribir datos

    data_file.close()
    return
    
def import_defect_dojo(name_csv):
    file_format = name_csv + ';type'
    file_format = name_csv
    headers = {
        'accept': 'application/json',
        'content-type': 'multipart/form-data',
    }
    
    data = {'username': 'admin', 'password': 'manuelazo161093'}
    
    files = { 
        'scan_date': (None, '2021-04-28'),
        'minimum_severity': (None, 'Info'),
        'active': (None, 'true'),
        'verified': (None, 'true'),
        'scan_type': (None, 'Twistlock Image Scan'),
        'file': ('jch-mbbk-data-retrieve.csv', open('jch-mbbk-data-retrieve.csv', 'rb')),
        'engagement': (None, '2'),
        'close_old_findings': (None, 'false'),
        'push_to_jira': (None, 'false'),
    }

    response = requests.post('http://172.18.0.1:8080/api/v2/import-scan/', headers=headers,data=data,files=files)
    
    print (response)
    return