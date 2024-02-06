def translateToRovarspraket(inputText):
    consonant = "bcdfghjklmnpqestvwxyzBCDFGHJKLMNPQRSTTVWXYZ"
    outputText = ""
    for char in inputText:
        if char in consonant:
            outputText += char + "o" + char
        else:
            outputText += char
    return outputText


def translateToPlainText(inputText):
    consonant = "bcdfghjklmnpqestvwxyzBCDFGHJKLMNPQRSTTVWXYZ"
    outputText = ""
    index = 0
    while index < len(inputText):
        if inputText[index] in consonant:
            outputText += inputText[index]
            index += 3
        else:
            outputText += inputText[index]
            index += 1
    return outputText


userInputText = input("Enter a string to translate: ")

rovarspraketText = translateToRovarspraket(userInputText)
print(f"Rovarspraket: {rovarspraketText}")

plainText = translateToPlainText(rovarspraketText)
print(f"Plain Text: {plainText}")
