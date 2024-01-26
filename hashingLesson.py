import random


def createData():
    dataSize = int(input("Enter data size: "))
    data = []
    hashTable = []
    for _ in range(dataSize):
        nameLength = random.randint(3, 12)
        tempString = ""
        for _ in range(nameLength):
            char = random.randint(65, 90)
            tempString += chr(char)
        data.append(tempString)
        for _ in range(round(dataSize * 1.10)):
            hashTable.append(None)
    return (data, hashTable)


def calcDiv(data, hashTable):
    tempK = ""
    for i in range(len(data)):
        tempK += str(ord(data[i]))
    hashIndex = int(tempK) % len(hashTable)
    return hashIndex


def divisionMethod(data, hashTable):
    collisions = 0
    for i in range(len(data)):
        hashIndex = calcDiv(data[i], hashTable)
        if hashTable[hashIndex] == None:
            hashTable[hashIndex] = data[i]
        else:
            print("Collision")
            collisions += 1
    print(f"Total collisions: {collisions}")
    return hashTable


def calculateMidSquare(data, hashTable):
    tempK = ""
    for i in range(len(data)):
        tempK += str(ord(data[i]))
    key = int(tempK)
    square = key * key
    hashIndex = int(str(square)[1:3])
    return hashIndex % len(hashTable)


def midSquareMethod(data, hashTable):
    collisions = 0
    for i in range(len(data)):
        hashIndex = calculateMidSquare(data[i], hashTable)
        if hashTable[hashIndex] == None:
            hashTable[hashIndex] = data[i]
        else:
            print("Collsion")
            collisions += 1
    print(f"Total collisions: {collisions}")
    return hashTable


def searchTable(hashTable):
    searchKey = input("Seach name: ")
    index = calcDiv(searchKey, hashTable) % len(hashTable)
    if hashTable[index] == searchKey:
        print("Found")
    else:
        print("Not found")


def printData(hashTable):
    for i in range(len(hashTable)):
        if hashTable[i] is not None:
            print(hashTable[i])


def main():
    choice = ""
    while choice != 5:
        print("1. Create data")
        print("2. Update table")
        print("3. Display table")
        print("4. Search")
        print("5. Quit")
        choice = input("Choice: ")
        if choice == "1":
            data, hashTable = createData()
            hashTable = midSquareMethod(data, hashTable)
        elif choice == "2":
            pass
        elif choice == "3":
            result = printData(hashTable)
            if result is not None:
                print(result)
        elif choice == "4":
            searchTable(hashTable)


main()
