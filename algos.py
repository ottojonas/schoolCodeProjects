import random
from timeit import default_timer as timer


def linearSearch(data, searchKey):
    found = False
    length = len(data)
    count = 0
    while count < length and not found:
        if data[count] == searchKey:
            return True
        else:
            count += 1
    pass


def binarySearch(data, searchKey):
    found = False
    head = 0
    tail = len(data) - 1
    while not found and head < tail:
        midPoint = (head + tail) // 2
        if data[midPoint] == searchKey:
            return True
        elif data[midPoint] > searchKey:
            tail = midPoint - 1
        else:
            head = midPoint - 1
        return found
    pass


def bubbleSort(data):
    nlen = len(data) - 1
    while True:
        swap = False
        for i in range(nlen):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swap = True
        if not swap:
            break
        nlen -= 1
    return data


def insertionSort(data):
    for i in range(len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j = j - 1
            data[j + 1] = key
    return data


def mergeSort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    leftHalf = mergeSort(data[:mid])
    rightHalf = mergeSort(data[mid:])
    return merge(leftHalf, rightHalf)


def merge(left, right):
    merged = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            merged.append(left[leftIndex])
            leftIndex += 1
        else:
            merged.append(right[rightIndex])
            rightIndex += 1
    merged += left[leftIndex:]
    merged += right[rightIndex:]
    return merged


def quickSort(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        less = [x for x in data[1:] if x <= pivot]
        greater = [x for x in data[1:] if x > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


def getSearchKey():
    return int(input("Enter search key: "))


def createData():
    numItems = int(input("Enter size of data set: "))
    data = random.sample(range(1, numItems * 2), numItems)
    return data


def viewData(data):
    for i in range(len(data)):
        print(data[i])


def main():
    data = createData()
    tempData = data.copy()
    choice = ""
    while choice != "8":
        print("1. Linear search")
        print("2. Binary search")
        print("3. Bubble sort")
        print("4. Insertion sort")
        print("5. Merge sort")
        print("6. View Data")
        print("7. Restore original data")
        print("8. Quit")
        print("9. Quick Sort")
        choice = input("Make selection: ")
        if choice == "1":
            searchKey = getSearchKey()
            print(linearSearch(data, searchKey))

        elif choice == "2":
            searchKey = getSearchKey()
            print(binarySearch(data, searchKey))

        elif choice == "3":
            start = timer()
            data = bubbleSort(data)
            end = timer()
            print("Total time: %.1f ms" % (1000 * (end - start)))

        elif choice == "4":
            start = timer()
            data = insertionSort(data)
            end = timer()
            print("Total time: %.1f ms" % (1000 * (end - start)))

        elif choice == "5":
            start = timer()
            data = mergeSort(data)
            end = timer()
            print("Total timer: %.1f ms" % (1000 * (end - start)))

        elif choice == "6":
            viewData(data)

        elif choice == "7":
            data = tempData

        elif choice == "9":
            start = timer()
            data = quickSort(data)
            end = timer()
            print("Total time: %.1f ms" % (1000 * (end - start)))


main()
