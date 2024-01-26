import random


def binFilling(binSize, items, itemsDup):
    bins = [0] * len(items)
    binCount = 0
    for item in items and itemsDup:
        minBinSize = binSize + 1
        binItemCount = 0
        for i in range(binCount):
            if bins[i] >= item and bins[i] - item < minBinSize:
                binItemCount = i
                minBinSize = bins[i] - item
        if minBinSize == binSize + 1:
            bins[binCount] = binSize - item
            binCount += 1
        else:
            bins[binItemCount] -= item
    return binCount


def main():
    numItems = int(input("Enter number of items: "))
    items = sorted(random.sample(range(1, numItems * 2), numItems), reverse=False)
    print(items)
    binSize = int(input("Enter bin size: "))
    scaling = float(input("Enter scaling factor (decimal value between 0-1): "))
    items = [item * scaling for item in items]
    itemsDup = items[:]
    print(items)
    print(itemsDup)
    numBins = binFilling(binSize, items, itemsDup)
    print(f"Number of bins required: {numBins}")


main()
