import requests
import json
import random
def picker_get_price(src_post,dest_post,weight):
    src_postal_code = src_post
    destinition_postal_code = dest_post
    wieght_parcel = weight
    link = "https://pickrr.com/api/homepage-shipping-calculator/?from_pincode=" + src_postal_code + "&weight=" + wieght_parcel + "&to_pincode=" + destinition_postal_code
    data = requests.get(link)
    data = json.loads(data.text)
    return data["price"]

