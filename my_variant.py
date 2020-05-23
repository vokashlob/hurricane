# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# write your update damages function here:
def update_damage(damage_list):
    new_list = []
    for record in damages:
        if "M" in record:
            new_list.append(float(record[:-1]) * 10 ** 6)
        elif "B" in record:
            new_list.append(float(record[:-1]) * 10 ** 9)
        else:
            new_list.append(record)
    return new_list


updated_damages = update_damage(damages)


# write your construct hurricane dictionary function here:
def dataset_construction():
    hurricanes = {}
    for index in range(len(names)):
        record = {"Name": names[index], "Month": months[index], "Year": years[index],
                  "Max Sustained Wind": max_sustained_winds[index], "Areas Affected": areas_affected[index],
                  "Damage": updated_damages[index], "Deaths": deaths[index]}

        hurricanes[names[index]] = record
    return hurricanes


hurricanes = dataset_construction()


# write your construct hurricane by year dictionary function here:

# var 1
def hurricane_by_year1():
    years = []
    data_by_years = {}
    for key in hurricanes:
        years.append(hurricanes[key]["Year"])
    years_unique = list(set(years))

    for year in years_unique:
        records = []
        for key in hurricanes:
            if year == hurricanes[key]["Year"]:
                records.append(hurricanes[key])

        data_by_years[year] = records
    return data_by_years


data_by_years = hurricane_by_year1()


# var 2
def hurricane_by_year2():
    cane_by_year = {}
    for key in hurricanes:
        current_year = hurricanes[key]["Year"]
        current_cane = hurricanes[key]
        if current_year not in cane_by_year:
            cane_by_year[current_year] = [current_cane]
        else:
            cane_by_year[current_year].append(current_cane)
    return cane_by_year


cane_by_year = hurricane_by_year2()


# write your count affected areas function here:
def affected_areas():
    areas = {}
    for key in hurricanes:
        current_areas = hurricanes[key]["Areas Affected"]
        for area in current_areas:
            if area not in areas:
                areas[area] = 1
            else:
                areas[area] += 1
    return areas


areas = affected_areas()


# write your find most affected area function here:
def most_affected_area():
    number = 0
    for key in areas:
        if areas[key] > number:
            number = areas[key]
            max_area = (key, number)
    return max_area


print(f"Most affected area is {most_affected_area()[0]} with total counts of {most_affected_area()[1]}.")


# print(most_affected_area())


# write your greatest number of deaths function here:
def max_deaths():
    max_deaths = 0
    for key in hurricanes:
        current_deaths = hurricanes[key]["Deaths"]
        if current_deaths > max_deaths:
            max_deaths = current_deaths
            max_deaths_cane = (hurricanes[key]["Name"], max_deaths)
    return max_deaths_cane


print(f"Hurricane that caused the greatest number of deaths is {max_deaths()[0]}. It caused {max_deaths()[1]} deaths.")


# write your catgeorize by mortality function here:
def mortality_rate():
    hurricanes_by_deaths = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for key in hurricanes:
        current_deaths = hurricanes[key]["Deaths"]
        if 0 < current_deaths <= 100:
            hurricanes_by_deaths[1].append(hurricanes[key])
        elif 100 < current_deaths <= 500:
            hurricanes_by_deaths[2].append(hurricanes[key])
        elif 500 < current_deaths <= 1000:
            hurricanes_by_deaths[3].append(hurricanes[key])
        elif 1000 < current_deaths <= 10000:
            hurricanes_by_deaths[4].append(hurricanes[key])
        elif current_deaths > 10000:
            hurricanes_by_deaths[5].append(hurricanes[key])
        else:
            hurricanes_by_deaths[0].append(hurricanes[key])
    return hurricanes_by_deaths


hurricanes_by_deaths = mortality_rate()


# write your greatest damage function here:
def max_damage():
    max_damage = 0
    for key in hurricanes:
        current_damage = hurricanes[key]["Damage"]
        if current_damage == 'Damages not recorded':
            pass
        elif current_damage > max_damage:
            max_damage = current_damage
            max_damage_cane = (hurricanes[key]["Name"], max_damage)
    return max_damage_cane


print(f"hurricane that caused the greatest damage is {max_damage()[0]}. Its damage costs {max_damage()[1]}")


# write your catgeorize by damage function here:
def damage_rate():
    hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for key in hurricanes:
        current_damage = hurricanes[key]["Damage"]
        if current_damage == "Damages not recorded":
            pass
        elif 0 < current_damage <= 100000000:
            hurricanes_by_damage[1].append(hurricanes[key])
        elif 100000000 < current_damage <= 1000000000:
            hurricanes_by_damage[2].append(hurricanes[key])
        elif 1000000000 < current_damage <= 10000000000:
            hurricanes_by_damage[3].append(hurricanes[key])
        elif 10000000000 < current_damage <= 50000000000:
            hurricanes_by_damage[4].append(hurricanes[key])
        elif current_damage > 50000000000:
            hurricanes_by_damage[5].append(hurricanes[key])
        else:
            hurricanes_by_damage[0].append(hurricanes[key])
    return hurricanes_by_damage


hurricanes_by_damage = damage_rate()



