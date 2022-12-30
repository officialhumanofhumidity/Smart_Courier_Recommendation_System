import requests
import json

def delhivery_rate_transit(pickup_postcode,delivery_postcode,weight,breadth,length,height):
    data=requests.get("https://serviceability.shiprocket.in/open/courier/serviceability?pickup_postcode="+pickup_postcode+"&delivery_postcode="+delivery_postcode+"&weight="+weight+"&cod=1&declared_value=&breadth="+breadth+"&length="+length+"&height="+height)
    data1= json.loads(data.text)
    data =json.dumps(data1, indent=4)
    with open("delhivery.txt", "w", encoding="utf-8") as f:
        f.write(data)
    #print(jmespath.search("data","price"))
    #print(data.data.available_courier_companies.air)
    parsed_air=data1["data"]["available_courier_companies"]["air"]
    ouput_data={}

    for i in parsed_air:
        ouput_data[i['courier_name']]=i['rate']
    if "Kerry Indev Express" not in ouput_data:
        ouput_data["Kerry Indev Express"] = 0
    return ouput_data


print(delhivery_rate_transit("400001","110004","10","10","20","20"))
