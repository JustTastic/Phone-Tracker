import phonenumbers
from phones import mynumber
from opencage.geocoder import OpenCageGeocode 
from phonenumbers import geocoder
import folium

def main():
    afterHyphenNumber = mynumber.strip("-")
    pepnumber = phonenumbers.parse(afterHyphenNumber.strip(" "))
    location = geocoder.description_for_number(pepnumber, 'en')

    print(location)

    from phonenumbers import carrier

    service_pro = phonenumbers.parse(mynumber)
    print(carrier.name_for_number(service_pro, 'en'))

    key = 'a15216a390094978a45359244788cd21'
    Geocoder = OpenCageGeocode(key)
    query = str(location)
    result = Geocoder.geocode(query)
    # print(result)

    lat = result[0] ['geometry']['lat']
    lng = result[0] ['geometry']['lng']
    # print(lat, lng)

    myMap = folium.Map(location=[lat, lng], zoom_start= 9)
    folium.Marker([lat,lng], popup=location).add_to(myMap)

    myMap.save("location.html")
    print("DONE")


if __name__ == '__main__':
    main()    


