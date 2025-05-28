mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

# Create counters and list
missiontotal = 0
missionsuccess = 0
missionspre2000 = []

# Create a loop for missions 
for i in range(len(mission_names)):
    missiontotal += 1

    if mission_success[i]:
        missionsuccess += 1
    
    if mission_years[i] < 2000:
        missionspre2000.append(mission_names[i])

# Create a calculation for success rate
successrate = (missionsuccess / missiontotal) * 100 

# Begin outputting results 
print("\nTotal number of missions is ", missiontotal)
print("Total successful missions is ", missionsuccess)
print("The success rate is {:.2f}%".format(successrate))
# Printing only 2 decimal places for the calculation
print("Missions launched before the year 2000:")
for mission in missionspre2000:
    print("-", mission)
# Formatted output of the missions before 2000