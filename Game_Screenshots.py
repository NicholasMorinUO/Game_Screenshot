import pyautogui
import time

#This is the delay added to each action in pyautogui,
#It acts as a safety measure for infinite Loops
pyautogui.PAUSE = 1.0


print('Press Ctrl-C to quit.')

print(pyautogui.size())

try:
    #100 screenshots is arbitrary
    for i in range(100):
        time.sleep(3) #added delay
        f = open("Minecraft_Shot"+str(i)+".png", "w")
        f.close()

        # .screenshot region paramaters:
        # Left, Top, Width, Height
        im = pyautogui.screenshot(region=(1030,380, 825, 1100))
        im.save("Minecraft_Shot"+str(i)+".png")
        print("Took screenshot "+str(i))        
except KeyboardInterrupt: #this exception allows control-c to exit the program
    print('\nDone.')
