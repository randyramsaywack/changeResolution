import win32api
import win32con
import pywintypes

class Resolution:
    def __init__(self, number, xRes, yRes):
        self.number = number
        self.xRes = xRes
        self.yRes = yRes

print("1. 1920 x 1080 (Native)")
print("2. 1656 x 1080 (Slightly Stretched)")
print("3. 1444 x 1080 (Very Stretched)")
print("4. Custom Resolution")

res = input("Select Resolution from list by typing the number: ")

if res == '1':
    selectedRes = Resolution(1, 1920, 1080)
elif res == '2':
    selectedRes = Resolution(2, 1656, 1080)
elif res == '3':
    selectedRes = Resolution(3, 1444, 1080)
elif res == '4':
    xRes = input("Input Width: ")
    yRes = input("Input Height: ")
    selectedRes = Resolution(4, int(xRes), int(yRes))
    
devmode = pywintypes.DEVMODEType()
devmode.PelsWidth = selectedRes.xRes
devmode.PelsHeight = selectedRes.yRes
devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
win32api.ChangeDisplaySettings(devmode, 0)
