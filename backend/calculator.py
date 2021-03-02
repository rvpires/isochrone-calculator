from math import cos, sin, tan, sqrt, pi, radians, degrees, asin, atan2
#import urllib2
import json
import sys
import datetime
import os
import requests


# Find the location on a sphere a distance 'radius' along a bearing 'angle' from origin
def select_destination(origin_geocode,angle, radius):

    # Harvsines are used to consider earth curvature
    #origin_geocode is the GPS coordinates of origin
    #angle is the angle from it's going to be calculated
    #radius is how long the arch is going to be
    r = 6371.0  # Radius of the Earth in  km
    bearing = radians(angle)  # Bearing in radians converted from angle in degrees
    lat1 = radians(origin_geocode['lat'])
    lng1 = radians(origin_geocode['lng'])

    lat2 = asin(sin(lat1) * cos(radius / r) + cos(lat1) * sin(radius / r) * cos(bearing))
    lng2 = lng1 + atan2(sin(bearing) * sin(radius / r) * cos(lat1), cos(radius / r) - sin(lat1) * sin(lat2))

    lat2 = degrees(lat2)
    lng2 = degrees(lng2)

    return {'lat' : lat2, 'lng' : lng2}

# Find transit time from origin to destinations via mode with trafic on/off on Google Matrix API
# More info : https://developers.google.com/maps/documentation/distance-matrix/overview
def get_transit_time(origin , destinations , mode , traffic):

    API_key = os.environ.get('GOOGLE_MAPS_API_KEY')
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

    #Add origin to query string
    url = url + 'origins=' + str(origin['lat']) + ',' + str(origin['lng'])

    #Add destinations to query string
    url = url + '&destinations='
    for destination in destinations:
        url = url + str(destination['lat']) + ',' + str(destination['lng']) + '|'

    #Add mode to query string
    url = url + '&mode=' + str(mode)

    if(traffic == True):
        url = url + '&traffic_model=best_guess'
        url = url + '&departure_time=now'

    #Add key to query string
    url = url + '&key=' + 'AIzaSyAB8O7xp4FZ4-2gBF_QXiLSxWgzL3tsnm8'

    r = requests.get(url).json()

    times = r['rows'][0]['elements']

    final = []

    for time in times:
        if(time['status'] == 'ZERO_RESULTS'):
            final = final + [None]

        elif(traffic == True):
            final = final + [time['duration_in_traffic']['value']]

        else:
            final = final + [time['duration']['value']]

    return final

# Calculator
def start(origin , n_points , duration , mode , traffic):    

    isochrone = [{'lat' : 0, 'lng' : 0}] * n_points #final return variable that contain the GPS coordinates of the isochrone
    rad = [duration / float(6)] * n_points  # initial r guess based on 10 km/h speed
    phi = [i * (float(360) / n_points) for i in range(n_points)] #angle distribution
    rmin = [0] * n_points
    rmax = [2.0 * duration] * n_points  # rmax based on 120 km/h speed
    margin = 1

    #initial circular mapping of points around the origin
    for i in range(n_points):
        isochrone[i] = select_destination(origin, phi[i], rad[i])

    i = 0
    j = 0

    while (i < 5):

        transit_times = get_transit_time(origin , isochrone , mode, traffic)

        for j in range(n_points):

            #If there are no transit time, short r by half
            if(transit_times[j] == None):
                rmax[j] = rad[j]
                rad[j] = (rad[j] + rmin[j]) / 2
                isochrone[j] = select_destination(origin, phi[j], rad[j])
                continue

              #if its too far away
            if(transit_times[j] > ((duration + margin) * 60)):
                rmax[j] = rad[j]
                rad[j] = (rad[j] + rmin[j]) / 2
                isochrone[j] = select_destination(origin, phi[j], rad[j])

            #its too close
            elif(transit_times[j] < ((duration - margin) * 60)):
                rmin[j] = rad[j]
                rad[j] = (rad[j] + rmax[j]) / 2
                isochrone[j] = select_destination(origin, phi[j], rad[j])

            j = j + 1


        i = i + 1

    return isochrone