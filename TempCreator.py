import random
file= open("dailyTempReadings.txt",'w')
for i in range(9):
    file.write(str(random.randint(-20,45)))
    file.write('\n')
file.write(str(random.randint(-20,45)))
file.close()