import csv

#defined function to export data from .txt file and converted into data the program can read 
def getDataFromFile(houseElf):
    with open("houseElf.txt", "r", newline = '') as file: 
        datareader = csv.reader(file)
        data = []
        for row in datareader: 
            data.append(row)
        return data
data = getDataFromFile("houseElf")
print(data) 

#number of elves with ears both smaller and larger than 10cm
totalOver10 = 0
totalUnder10 = 0 

for i in range(len(data)): 
    if float(data[i][1]) > 10: 
        totalOver10 += 1
    else: 
        totalUnder10 += 1

print(f"there are {totalOver10} elves with ears larger than 10cm")
print(f"there are {totalUnder10} elves with ears shorter than 10cm")

#percentage of C and G in elf dna 
totalCharDNA = 0 
totalCG = 0 

for i in range(len(data)): 
    if "C" in data[i][2]:
        totalCharDNA += len(data[i][2])
        totalCG += data[i][2].count("C")
    if "G" in data[i][2]: 
        totalCharDNA += len(data[i][2])
        totalCG += data[i][2].count("G")

print(f"{(totalCG / totalCharDNA) * 100} of DNA characters were C and G characters")

#exporting data to a csv file called "grangers_analysis"
with open("grangers_analysis.csv", "w", newline = "") as file: 
    writer = csv.writer(file)
    writer.writerow(["elf id", "large or small", "gc content"])
    
    for elf_id, size, dna in data: 
        if float(size) > 10: 
            size = "large"
        else: 
            size = "small" 

        cgContent = (dna.count("C") + dna.count("G")) / len(dna) * 100
        writer.writerow([elf_id, size, f"{cgContent:.2f}%"])

#output of average cg content in all elves
print(f"there was an average of {totalCharDNA / cgContent:.2f} C and G charaters in the elves DNA")