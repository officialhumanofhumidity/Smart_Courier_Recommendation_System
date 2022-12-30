import requests
import json

data={ "origin": "NAG",
"destination": "BOM",
"product": "DOX",
"service_type": "NOR",
"length": "",
"breadth": "" ,
"height":"",
"weight": "5",
"action":"ff_rate_calculation"
}


link="https://firstflightme.com/wp-admin/admin-ajax.php"
data=requests.post(link,json=data)

print(data)