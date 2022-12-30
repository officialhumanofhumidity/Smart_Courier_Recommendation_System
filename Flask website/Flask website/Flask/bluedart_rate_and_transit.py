import this

import requests
import json
def bluedart_rate_transit(destinition_postal,wieght_par,from_add="",to_add="",booking_date=""):
    from_address = ""
    to_address = ""
    src_city = ""
    src_sate = ""
    src_postal_code  = ""
    src_country = ""
    destinition_country = ""
    destinition_postal_code = destinition_postal
    destinition_city = ""
    destinition_state = ""
    booking_date = "7-12-2022"
    booking_time = "12:00 am"
    wieght_parcel = wieght_par
    link = """https://www.bluedart.com/web/guest/home?p_p_id=ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=findPrice&p_p_cacheability=cacheLevelPage&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getSourceLocation=""" + from_address + """&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getDestinationLocation=""" + to_address + """&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getWeightInKg=""" + wieght_parcel + """&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getSourceCity=""" + src_city + """&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getSourceState=""" + src_sate + """&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getSourceCountry=""" + src_country + """&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getSourcePostalCode=""" + destinition_postal_code + """&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getSourceStreetAddress=&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getDestinationCity=""" + destinition_city + """&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getDestinationState=""" + destinition_state + """&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getDestinationCountry=""" + destinition_country + """&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getDestinationCountryCode=IN&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getDestinationPostalCode=""" + destinition_postal_code + """&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getDestinationStreetAddress=&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getBookingDate=""" + booking_date + """&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getBookingTime=""" + booking_time
    # data = requests.get("https://www.bluedart.com/web/guest/home?p_p_id=ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=findPrice&p_p_cacheability=cacheLevelPage&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getSourceLocation=Sitabuldi, Nagpur, Maharashtra, India&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getDestinationLocation=Rail Toly, Gondia, Maharashtra, India&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getWeightInKg=5&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getSourceCity=Nagpur&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getSourceState=Maharashtra&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getSourceCountry=India&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getSourcePostalCode=440012&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getSourceStreetAddress=&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getDestinationCity=Gondia&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getDestinationState=Maharashtra&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getDestinationCountry=India&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getDestinationCountryCode=IN&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getDestinationPostalCode=441601&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getDestinationStreetAddress=&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getBookingDate=18-11-2022&_ratetransitfinderportlet_WAR_RateTransitFinderportlet_INSTANCE_ratetransitportlet_getBookingTime=04:00 PM")

    data = requests.get(link)
    data = json.loads(data.text)
    # print(json.dumps(data,indent=4))

    with open("bluedart_rate_and_transit1.txt", "w", encoding="utf-8") as f:
        f.write((json.dumps(data, indent=4)))

    type = "domestic"  # document air package ground package
    if type == "domestic":
        param_list = {"price": data[1][0]['price'], "transitTime": data[1][0]["transitTime"]}
    elif type == "air":
        param_list = {"price": data[1][1]['price'], "transitTime": data[1][1]["transitTime"]}

    elif type == "ground":
        param_list = {"link":"https://www.bluedart.com/","price": data[1][2]['price'], "transitTime": data[1][2]["transitTime"]}

    return param_list


print(bluedart_rate_transit("440012","20","400001"))