def menu(day):
    if day=="monday":
        return "chole bhature"
    elif day=="tuesday":
        return "poha"
    elif day=="wednesday":
        return "puri sabzi"
    elif day=="thursday":
        return "rajma rice"
    elif day=="friday":
        return "dhosa"
    elif day=="saturday":
        return "egg curry"   
    else:
        return "idali"
print("pure week ka menu ")


mon_menu=menu("monday")
print(mon_menu)
tue_menu=menu("tuesday")
print(tue_menu)
wed_menu=menu("wednesday")
print(wed_menu)   
thu_menu=menu("thursday")
print(thu_menu)
fri_menu=menu("friday")
print(fri_menu)
sat_menu=menu("saturday")
print(sat_menu)
sun_menu=menu("sunday")
print(sun_menu)              