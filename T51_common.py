from Cimpl import *

def image_load():
    print("Select an Image to Load:")
    return load_image(choose_file())


def image_save(image):
    save_as(image)
    return True

def quit_program():
    print("Any existing changes are not saved automatically.\nAre you sure you would like to quit? (Y/N)")
    while True:
        quitInput = input().upper()
        if quitInput == "Y" or quitInput == "YES":
            return True
        elif quitInput == "N" or quitInput == "NO":
            return False


