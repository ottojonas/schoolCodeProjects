import csv

def getBirdData(birdDataNew):
    with open("birdDataNew.txt", "r", newline = "") as file: 
        datareader = csv.reader(file)
        data = [row for row in datareader]
        return data
birdData = getBirdData("birdDataNew") 
print(birdData)

#number of sites 
sitesNo = len(birdData)
print(f"there are {sitesNo} sites")

#number of birds in site 7
print(f"there were {birdData[6][1]} birds in site 7")

#number of birds in the last site 
print(f"there were {birdData[-1][1]} birds in the last site")

#total number of birds 
totalBirds = sum(int(row[1]) for row in birdData)
print(f"there were {totalBirds} birds in total")

#average number of birds 
average = totalBirds / sitesNo
print("there were", f"{average:.2f}", "on average")

#number of birds per site 
totalA = sum(int(row[1]) for row in birdData if "A" in row[0])
totalB = sum(int(row[1]) for row in birdData if "B" in row[0])
totalC = sum(int(row[1]) for row in birdData if "C" in row[0])
totalD = sum(int(row[1]) for row in birdData if "D" in row[0])
print(f"there were {totalA} birds in site A")
print(f"there were {totalB} birds in site B")
print(f"there were {totalC} birds in site C")
print(f"there were {totalD} birds in site D")

with open("birdData.csv", "w", newline = "") as file: 
    writer = csv.writer(file)
    field = ["site", "birds spotted in site"]
    writer.writerow(field) 
    for row in birdData: 
        writer.writerow(row)