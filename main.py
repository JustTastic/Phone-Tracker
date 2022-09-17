from distutils.errors import LibError
import os
import phonenumbers
from phones import mynumber
from opencage.geocoder import OpenCageGeocode 
from phonenumbers import geocoder
import folium
import subprocess
import webbrowser

def main():
    person_number = phonenumbers.parse(mynumber)
    location = geocoder.description_for_number(person_number, 'en')

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
    try: 
        cmd = "pip install phonenumbers folium opencage"
        process = subprocess.Popen(cmd, shell=True, stdout= subprocess.DEVNULL, stderr=subprocess.PIPE)
        out, err = process.communicate()
        if process.returncode == 0:
            process.wait()
            print("Necessary libraries has been install!!")
            main()
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            locationHTML = 'file://' + os.path.realpath('location.html')
            webbrowser.get('chrome').open_new_tab(locationHTML)
            #! webbrowser.reload(locationHTML)
        else:
            print("Library Not Found Or Not Written Correctly : {0}".format(err))
    except LibError:
        print("Nessesory libraries FAILED TO INSTALL!!")
