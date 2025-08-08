highest= -99999
lowest = 99999
prevTemp = 99999
prevCount=0
averageTemp=0
file = open("dailyTempReadings.txt",'r')
for line in file:
    lineX=float(line.strip())
    averageTemp+=lineX
    if lineX < lowest:
        lowest=lineX
    if highest<lineX:
        highest=lineX
    if prevTemp < lineX:
        prevCount+=1
    prevTemp=lineX
print(f'''
Average Temperature: {round(averageTemp,0)}
Highest Temperature: {round(highest,0)}
Lowest Temperature: {round(lowest,0)}
Days temperature increased relative to previous day: {prevCount}''')
file.close()
    