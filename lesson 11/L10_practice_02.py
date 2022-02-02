# -*- coding: utf-8 -*-
# L10_practice_02.py
"""
1. Дан файл "L10_practice_02.json", который состоит из списка пользователей.
2. Откройте данный файл и выведите на экран информацию о всех пользователях в формате:
    <username>, <name>, <address>: <street> <suite> <city> <zipcode>
"""
import json


filename = 'd:\\study_projects\\python_lessons\\lesson 11\\L10_practice_02.json'

with open(filename, 'r', encoding='utf-8') as f:
    loaded_json = json.load(f)
    
for ljson in loaded_json:
    formatted_loaded_json = f"{ljson['username']}, {ljson['name']}, address: {ljson['address']['street']}, {ljson['address']['suite']}, {ljson['address']['city']}, {ljson['address']['zipcode']}"
    print(formatted_loaded_json)
    """
    Bret, Leanne Graham, address: Kulas Light, Apt. 556, Gwenborough, 92998-3874
    Antonette, Ervin Howell, address: Victor Plains, Suite 879, Wisokyburgh, 90566-7771
    Samantha, Clementine Bauch, address: Douglas Extension, Suite 847, McKenziehaven, 59590-4157
    Karianne, Patricia Lebsack, address: Hoeger Mall, Apt. 692, South Elvis, 53919-4257
    Kamren, Chelsey Dietrich, address: Skiles Walks, Suite 351, Roscoeview, 33263
    Leopoldo_Corkery, Mrs. Dennis Schulist, address: Norberto Crossing, Apt. 950, South Christy, 23505-1337
    Elwyn.Skiles, Kurtis Weissnat, address: Rex Trail, Suite 280, Howemouth, 58804-1099
    Maxime_Nienow, Nicholas Runolfsdottir V, address: Ellsworth Summit, Suite 729, Aliyaview, 45169        
    Delphine, Glenna Reichert, address: Dayna Park, Suite 449, Bartholomebury, 76495-3109
    Moriah.Stanton, Clementina DuBuque, address: Kattie Turnpike, Suite 198, Lebsackbury, 31428-2261  
    """
