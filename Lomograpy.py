import requests
import json


url_base = 'http://api.lomography.com/v1/'
url_location = 'location/around/'
url_boundingbox = 'location/within/'
auth_url = '?api_key='




#GET http://api.lomography.com/v1/photos/popular
def get_popular_photos(self_page, api_key):
    #This will return the most popular photos (uploaded in the last month).

    api_key = str(api_key)
    
    if self_page == None:
        self_page = 1

    self_page = str(self_page)

    response = requests.get(url_base+'photos/popular?page='+self_page+'&api_key='+api_key)
    if response.status_code == 200:
        return response
    
    elif response.status_code == 401:
        print("Error 401 Unauthorized")

    else:
        print("Error 404 not found")




#GET http://api.lomography.com/v1/photos/recent
def get_recent_photos(api_key):
    #This will return the most recent photos (right as they are uploaded).

    api_key = str(api_key)

    response = requests.get(url_base+'photos/recent'+auth_url+api_key)
    
    if response.status_code == 200:
        return response
    
    elif response.status_code == 401:
        print("Error 401 Unauthorized")

    else:
        print("Error 404 not found")




#GET http://api.lomography.com/v1/photos/selected
def get_handpicked_collection(api_key):
    #This will return a handpicked collection of photos.

    api_key = str(api_key)

    response = requests.get(url_base+'photos/selected'+auth_url+api_key)

    if response.status_code == 200:
        return response
    
    elif response.status_code == 401:
        print("Error 401 Unauthorized")

    else:
        print("Error 404 not found")




#GET http://api.lomography.com/v1/cameras
def get_most_used_camera(api_key):
    #This will return the most used cameras.

    api_key = str(api_key)

    response = requests.get(url_base+'cameras'+auth_url+api_key)

    if response.status_code == 200:
        return response
    
    elif response.status_code == 401:
        print("Error 401 Unauthorized")

    else:
        print("Error 404 not found")




#GET http://api.lomography.com/v1/cameras/:id
def get_camerea_by_id(self_id, api_key):
    #This will return a single camera.

    api_key = str(api_key)
    self_id = str(self_id)

    response = requests.get(url_base+'cameras/'+self_id+'/'+auth_url+api_key)

    if response.status_code == 200:
        return response
    
    elif response.status_code == 401:
        print("Error 401 Unauthorized")

    else:
        print("Error 404 not found")




#GET http://api.lomography.com/v1/cameras/:id/photos/popular
def get_popular_photos_by_camera_id(self_id, api_key):
    #This will return the most popular photos (uploaded in the last month) taken with that camera.

    api_key = str(api_key)
    self_id = str(self_id)

    response = requests.get(url_base+'cameras/'+self_id+'/photos/popular'+auth_url+api_key)

    if response.status_code == 200:
        return response
    
    elif response.status_code == 401:
        print("Error 401 Unauthorized")

    else:
        print("Error 404 not found")




#GET http://api.lomography.com/v1/cameras/:id/photos/recent
def get_recent_photos_by_camera_id(self_id, api_key):
    #This will return the most recent photos (right as they are uploaded) taken with that camera.

    api_key = str(api_key)
    self_id = str(self_id)

    response = requests.get(url_base+'cameras/'+self_id+'/photos/recent'+auth_url+api_key)

    if response.status_code == 200:
        return response
    
    elif response.status_code == 401:
        print("Error 401 Unauthorized")

    else:
        print("Error 404 not found")




#GET http://api.lomography.com/v1/films
def get_most_used_films(api_key):
    #This will return the most used films.

    api_key = str(api_key)

    response = requests.get(url_base+'films'+auth_url+api_key)

    if response.status_code == 200:
        return response
    
    elif response.status_code == 401:
        print("Error 401 Unauthorized")

    else:
        print("Error 404 not found")




#GET http://api.lomography.com/v1/films/:id
def get_films_by_id(self_id, api_key):
    #This will return a single film.

    api_key = str(api_key)
    self_id = str(self_id)

    response = requests.get(url_base+'films/'+self_id+'/'+auth_url+api_key)

    if response.status_code == 200:
        return response
    
    elif response.status_code == 401:
        print("Error 401 Unauthorized")

    else:
        print("Error 404 not found")




#GET http://api.lomography.com/v1/films/:id/photos/popular
def get_popular_photos_by_film_id(self_id, api_key):
    #This will return the most popular photos (uploaded in the last month) taken with that film.

    api_key = str(api_key)
    self_id = str(self_id)

    response = requests.get(url_base+'films/'+self_id+'/photos/popular'+auth_url+api_key)

    if response.status_code == 200:
        return response
    
    elif response.status_code == 401:
        print("Error 401 Unauthorized")

    else:
        print("Error 404 not found")




#GET http://api.lomography.com/v1/films/:id/photos/recent
def get_recent_photos_by_film_id(self_id, api_key):
    #This will return the most recent photos (right as they are uploaded) taken with that film.

    api_key = str(api_key)
    self_id = str(self_id)
    
    response = requests.get(url_base+'films/'+self_id+'/photos/recent'+auth_url+api_key)

    if response.status_code == 200:
        return response
    
    elif response.status_code == 401:
        print("Error 401 Unauthorized")

    else:
        print("Error 404 not found")




#GET http://api.lomography.com/v1/location/within/:latitude_north/:longitude_east/:latitude_south/:longitude_west/photos/recent
def get_recent_by_boundingbox(self_latitude_north, self_longitude_east, self_latitude_south, self_longitude_west, api_key):
    #This will return the most recent photos within a certain bounding box. The order is latitude north, longitude west, latitude south and longitude east.

    api_key = str(api_key)

    self_latitude_north = str(self_latitude_north)
    self_longitude_east = str(self_longitude_east)
    self_latitude_south = str(self_latitude_south)
    self_longitude_west = str(self_longitude_west)

    response = requests.get(url_base+url_boundingbox+self_latitude_north+'/'+self_longitude_east+'/'+self_latitude_south+'/'+self_longitude_west+'/photos/recent'+auth_url+api_key)

    if response.status_code == 200:
        return response
    
    elif response.status_code == 401:
        print("Error 401 Unauthorized")

    else:
        print("Error 404 not found")




#GET http://api.lomography.com/v1/location/within/:latitude_north/:longitude_east/:latitude_south/:longitude_west/photos/popular
def get_popular_photos_by_boundingbox(self_latitude_north, self_longitude_east, self_latitude_south, self_longitude_west, api_key):
    #This will return the most polular photos within a certain bounding box. The order is latitude north, longitude west, latitude south and longitude east.

    api_key = str(api_key)

    self_latitude_north = str(self_latitude_north)
    self_longitude_east = str(self_longitude_east)
    self_latitude_south = str(self_latitude_south)
    self_longitude_west = str(self_longitude_west)

    response = requests.get(url_base+url_boundingbox+self_latitude_north+'/'+self_longitude_east+'/'+self_latitude_south+'/'+self_longitude_west+'/photos/popular'+auth_url+api_key)

    if response.status_code == 200:
        return response
    
    elif response.status_code == 401:
        print("Error 401 Unauthorized")

    else:
        print("Error 404 not found")





#GET http://api.lomography.com/v1/location/around/:latitude/:longitude/:radius/photos/distance
def get_nearest_photos(self_latitude, self_longitude, self_radius, api_key):
    #This will return the nearest photos within a certain radius (in km) to the origin point.

    api_key = str(api_key)

    self_latitude = str(self_latitude)
    self_longitude = str(self_longitude)
    self_radius = str(self_radius)

    response = requests.get(url_base+url_location+self_latitude+'/'+self_longitude+'/'+self_radius+'/photos/distance/'+auth_url+api_key)

    if response.status_code == 200:
        return response
    
    elif response.status_code == 401:
        print("Error 401 Unauthorized")

    else:
        print("Error 404 not found")




#GET http://api.lomography.com/v1/location/around/:latitude/:longitude/:radius/photos/recent
def get_recent_in_radius(self_latitude, self_longitude, self_radius, api_key):
    #This will return the most recent photos within a certain radius (in km) to the origin point.

    api_key = str(api_key)

    self_latitude = str(self_latitude)
    self_longitude = str(self_longitude)
    self_radius = str(self_radius)

    response = requests.get(url_base+url_location+self_latitude+'/'+self_longitude+'/'+self_radius+'/photos/recent/'+auth_url+api_key)

    if response.status_code == 200:
        return response
    
    elif response.status_code == 401:
        print("Error 401 Unauthorized")

    else:
        print("Error 404 not found")




#GET http://api.lomography.com/v1/location/around/:latitude/:longitude/:radius/photos/popular
def get_popular_in_radius(self_latitude, self_longitude, self_radius, api_key):
    #This will return the most popular photos within a certain radius (in km) to the origin point.

    api_key = str(api_key)

    self_latitude = str(self_latitude)
    self_longitude = str(self_longitude)
    self_radius = str(self_radius)

    response = requests.get(url_base+url_location+self_latitude+'/'+self_longitude+'/'+self_radius+'/photos/popular/'+auth_url+api_key)

    if response.status_code == 200:
        return response
    
    elif response.status_code == 401:
        print("Error 401 Unauthorized")

    else:
        print("Error 404 not found")
