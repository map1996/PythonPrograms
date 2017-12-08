from math import radians, sin, cos, acos
#function to calucalate distance for the between two different phc 
def distance_two_latlongs(slatlon,dlatlon1):
    dist = 6371.01 * acos(sin(slatlon[0])*sin(dlatlon1[0]) + cos(slatlon[0])*cos(dlatlon1[0])*cos(slatlon[1] - dlatlon1[1]))
    return dist

import os
nearest_phc=open("geocode_health_centre.csv","r")
phc_data=nearest_phc.read()
phc_data=phc_data.split("\n")
health_centers={}
for data in range(1,len(phc_data)-1):
    list_data=[]
    data_items=[]
    data_items=phc_data[data].split(",")
    key=data_items[1]
    if (key in health_centers):
        list_data.append(data_items[4])
        list_data.append(data_items[6])
        list_data.append(data_items[7])
        health_centers[key].append(list_data)
    else:
        health_centers[key]=[]
        list_data.append(data_items[4])
        list_data.append(data_items[6])
        list_data.append(data_items[7])
        health_centers[key].append(list_data)
nearest_phc.close()

#Enter the District name and latitude and longitude of which you want to go by nearest phc

District_name=input("Enter the District name to see the nearest phc:")
try:
    s_la=float(input("Enter the latitude:"))
    s_lo=float(input("Enter the longitutude:"))
    s_latlon=[s_la,s_lo]
    k=0
    if(District_name in health_centers):
        area_phc=health_centers[District_name] 
        latlon_list=[]
        for i in range(0,len(area_phc)-1):
            latlon_list.append([])
            try:
                latlon_list[k]=[float(area_phc[i][1]),float(area_phc[i][2])]
                k=k+1
            except:
                continue
    
    res_list=[]
    for j in range(0,len(latlon_list)-1):
        res=distance_two_latlongs(latlon_list[j],s_latlon)
        res_list.append(res)
    for i in range(len(res_list)-1):
        if(res_list[i] == min(res_list)):
            s=i
            break
    print(area_phc[i])
    print("Nearest Phc to the Source Lat_lon:",area_phc[i][0])
    
except Exception as e:
    print("Error Code:",e)        
