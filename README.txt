----------------------------------------------------------------------------
			TEAM 51 Image Filtering Tool
----------------------------------------------------------------------------
Welcome to ECOR 1051 Team 51's Image Filtering Tool guide. This program may bre reffered to as the IFT throughout
this document.

Installation & Execution
-------------------------------------
PRE-INSTALLATION:
The tool runs on Python has been tested for Python v3.7+ (04/01/2020)
**IMPORTANT: THIS PROGRAM HAS NOT BEEN TESTED FOR MAC OSX OR LINUX/UNIX BASED OS'S**
To install Python, visit https://www.python.org/downloads/ and download a compatible version. 
Launch the downloaded installer and check the checkbox asking to "Add Python to PATH"

This tool depends on functions from the Carleton Image Manipulation Python Library (Cimpl) which depends on Pillow.
*Note: Cimpl is included with the tools package*
To install the pillow module, open command line and enter "pip install Pillow"
The "pip" installer should come with Python. If not found, you may have to install it manually.

TOOL INSTALLATION:
Download and extract the filtering tool's compressed file and ensure all files are present within the same directory.

ALTERNATIVE TOOL INSTALLATION:
github stuff

LAUNCH TOOL:
To launch the program, launch T51_interactive_ui.py using a valid Python version.



Overview
-------------------------------------
This IFT is a project developped by the students of ECOR 1051 Team 51 at Carleton University and runs on Python within
the command line terminal. It includes multiple image filters as well as an image loading and saving functionality. 
The program is designed to be extremely dynamic and suit any user's basic needs. It allows the user to easily add
their own filters or functions on top of the existing ones (explained in the next section) as well as loading multiple 
images at a time into memory.

Once the IFT is launched, you must load one or more images into memory using the pre-built Load Image utility. The
program will then re-direct the user to the main menu. From the main menu you may apply a filter to a singular image by
entering the filters name as displayed or the character located behind the ")" within the name. If multiple images are
loaded, the user will be prompted to apply a filter onto a select image from the displayed list of images. The filtered
image will be saved as another image in local/temporary memory so that the user can apply more filters onto the filtered
image or return to another state of a multi-filtered image during the session.

