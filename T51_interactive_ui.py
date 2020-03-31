import os
from time import sleep
from T51_common import *
from T51_image_filters import *

loadedImages = []

def selectImage(loadedImages, argDescription):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        for image in range(len(loadedImages)):
            print("{}. {} | {}".format(image + 1, loadedImages[image][0].filename, loadedImages[image][1]))
        imgSelection = input("\nSelect Image {}: ".format(argDescription))
        try:
            if int(imgSelection) <= len(loadedImages):
                return loadedImages[int(imgSelection) - 1]
            else:
                print("Please Select a Valid Image!")
                sleep(1.5)
        except:
            print("Please Enter a Number!")
            sleep(1.5)

def filter(selectionData: list):
    if len(loadedImages) == 0:
        return False
    else:
        args = []
        imageDescription = ""
        loadedImageArgs = ""
        for argument in selectionData[4]:
            if argument[0] == "image":
                if len(loadedImages) == 1:
                    args.append(loadedImages[0][0])
                    imageDescription += "{} ({}) ->".format(loadedImages[0][0].filename, loadedImages[0][1])
                else:
                    image = selectImage(loadedImages, argument[1])
                    args.append(image[0])
                    imageDescription += "{} ({}) ->".format(args[-1].filename, image[1]) 
            elif argument[0] == "static":
                args.append(argument[1])
                if loadedImageArgs == "" and len(selectionData[4]) > 1:
                    loadedImageArgs += (" (" + str(argument[1]))
                elif len(selectionData[4]) > 1:
                    loadedImageArgs += (" + " + str(argument[1]))
            elif argument[0] == "input":
                args.append(input("Please enter " + argument[1] + ": "))
                if loadedImageArgs == "" and len(selectionData[4]) > 1:
                    loadedImageArgs += (" (" + str(argument[1]) + ": " + args[-1])
                elif len(selectionData[4]) > 1:
                    loadedImageArgs += (" + " + str(argument[1]) + ": " + args[-1])
        
        if loadedImageArgs != "":
            loadedImageArgs += ")"
        if selectionData[2] == "save":
            selectionData[3](*args)
        else:
            loadedImages.append([selectionData[3](*args), selectionData[3].__name__ + loadedImageArgs])
    
            loadedImages[-1][0].filename = imageDescription
            print("Filter Successfully Applied!")
            show(loadedImages[-1][0])
        return True

def action(actionPos: list):
    validSelection = False
    userInput = input("Select an option: ")
    for selectionData in actionPos:
        if userInput.upper() in selectionData:
            validSelection = True
            if selectionData[2] == "load":
                loadedImages.append([selectionData[3](), "Stock"])
                return mainMenu
            elif selectionData[2] == "save" or selectionData[2] == "filter":
                filterResult = filter(selectionData)
                if filterResult == False:
                    print("No image found!\nPlease load an image...")
                    sleep(1.5)
                return mainMenu
            elif selectionData[2] == "quit":
                if selectionData[3]() == True:
                    return 1
                else:
                    return mainMenu
    print("This command does not exist...")
    sleep(1)
    return mainMenu

def display(menuData: list):
    os.system('cls' if os.name == 'nt' else 'clear')
    selectionPos = []
    usedChars = ""
    menuWidth = max([len(x) for x in menuData[1:]]) * 27 - 1
    print("\n{}".format(" " * ((menuWidth - len(menuData[0]))//2) + menuData[0] + " " * ((menuWidth - len(menuData[0]))//2)), end="")
    for row in range(1, len(menuData)):
        print("\n{}".format("-" * menuWidth))
        for selection in menuData[row]:
            commandLetter = ""
            commandDisplay = ""
            for character in range(len(selection[0])):
                if selection[0][character] not in usedChars:
                    commandLetter = selection[0][character]
                    commandDisplay = selection[0][:character] + "(" + selection[0][character] + ")" + selection[0][(character + 1):]
                    usedChars += commandLetter
                    break
            selectionPos.append([commandLetter.upper(), selection[0].upper(), selection[1], selection[2], selection[3]])
            print("{0:<25}| ".format(commandDisplay), end="")
    print("\n{}\n".format("-" * menuWidth))
    return action(selectionPos)

mainMenu = [
    "T51 Image Filtering Tool",
    [
        ["Load Image", "load", image_load, [[]]],
        ["Save-as", "save", image_save, [["image", "to save as"]]]
    ],
    [
        ["2-tone", "filter", two_tone, [["image", "to apply 2-tone filter"], ["static", "cyan"], ["static", "yellow"]]],
        ["3-tone", "filter", three_tone, [["image", "to apply 3-tone filter"], ["static", "cyan"], ["static", "magenta"], ["static", "yellow"]]],
        ["Xtreme contrast", "filter", extreme_contrast, [["image","to apply the extreme contrast effect"]]],
        ["Tint sepia", "filter", sepia, [["image","to add a sepia tone"]]],
        ["Posterize", "filter", posterize, [["image", "to posterize"]]]
    ],
    [
        ["Edge detect", "filter", detect_edges, [["image", "to isolate the edges of the image"], ["input", "threshold"]]],
        ["Improved Edge detect", "filter", detect_edges_better, [["image", "to isolate the edges of the image"], ["input", "threshold"]]],
        ["Vertical Flip", "filter", vertical, [["image", "to flip vertically"]]],
        ["Horizontal Flip", "filter", horizontal, [["image", "to flip horizontally"]]]
    ],
    [
        ["Quit", "quit", quit_program, [[]]]
    ]
]

actionReturn = mainMenu
while True:
    actionReturn = display(actionReturn)
    if actionReturn == 1: quit()
