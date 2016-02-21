# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 12:48:45 2016

@author: Bluefish_
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
from operator import itemgetter

def Set_URL(BASE_URL):
    
    url_dict = {}
    url_dict["AVERY"] = BASE_URL+"avery"
    url_dict["URIS"] = BASE_URL+"business"
    url_dict["BUTLER"] = BASE_URL+"butler"
    url_dict["KENT"] = BASE_URL+"eastasian"
    url_dict["GEOLOGY"] = BASE_URL+"geology"
    url_dict["HEALTH"] = BASE_URL+"health-sciences"
    url_dict["PULITZER"] = BASE_URL+"journalism"
    url_dict["LAW"] = BASE_URL+"law"
    url_dict["LEHMAN"] = BASE_URL+"lehman"
    url_dict["MATH"] = BASE_URL+"math"
    url_dict["MUSIC"] = BASE_URL+"music"
    url_dict["NOCO"] = BASE_URL+"science-engineering"
    url_dict["TEACHERS"] = BASE_URL+"teachers-college"
    return url_dict

def Process_Time(hours):
    
    hours = hours.split()
    hours = hours[2]
    hours = hours[:(len(hours)-5)]
    hours = hours.split("-")
    open_time, close_time = hours[0], hours[1]
    open_time_int, close_time_int = 0, 0   
    
    if 'Noon' == open_time:
        open_time_int = 12
    else:
        open_time = open_time.split(':')
        open_time_int = int(open_time[0])
        if 'pm' in open_time[1]:
            open_time_int += 12
    
    if 'Midnight' == close_time:
        close_time_int = 24
    else:
        close_time = close_time.split(':')
        close_time_int = int(close_time[0])
        if 'pm' in close_time[1]:
            close_time_int += 12
        else:
            close_time_int += 24
    
    return (open_time_int, close_time_int)
    
def Scrape_URL(url_dict):
    
    lib_dict = {}
    
    for key in url_dict.keys():
        
        url = url_dict[key]
        html = urlopen(url)
        soup = BeautifulSoup(html, "lxml")
        today_hours = soup.findAll("td", "today_hours")
        today_date = soup.find("td", "today_date")
        
        date = ''
        for char in today_date:
            if char.isdigit():
                date += char
        date = int(date)
        
        hours = str(today_hours[date - 1])
        lib_dict[key] = Process_Time(hours)
        
    return lib_dict

def get_current_time():
    
    clocktime = str(datetime.now().time())
    clocktime = clocktime.split(':')
    clockhour = clocktime[0]
    return int(clockhour)

def find_open_lib(lib_hours):
    
    open_lib = {}
    cur_time = get_current_time()
    for key, value in lib_hours.items():
        if cur_time in range(value[0],value[1]):
            open_lib[key] = value[1] - cur_time
    result = sorted(open_lib.items(),key = itemgetter(1), reverse = True)
    return result

def print_result(lib_list):
    
    print("Hi, my user. The following is the list of libraries that are \
currently open. Hope you are learning well!\n")
    for item in lib_list:
        lib = item[0]
        t = item[1]
        print("{} Library will close in less than {} hours.\n".format(lib,t))

def main():
        
    lib_url = Set_URL("http://hours.library.columbia.edu/?library=")
    lib_hours = Scrape_URL(lib_url)
    lib_list = find_open_lib(lib_hours)
    print_result(lib_list)
    
main()

