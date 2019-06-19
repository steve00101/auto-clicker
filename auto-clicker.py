import time, win32api, win32con, sys, math

x, y = win32api.GetCursorPos()
t = 0.1
d = 5.0
key = ord('P')
mKey = ord('I')
xKey = ord('X')
extraInfo = False
count = 0
timerS = time.time()

def click(x, y, t):
    
    while True:
        global count
        global timerS
        pressed = isKeyPressed(key)
        mPressed = isKeyPressed(mKey)
        xPressed = isKeyPressed(xKey)
        if pressed:
            pause()
        elif mPressed:
            menu()
        elif xPressed:
            terminate()
        else:
            if extraInfo == True:
                timerE = time.time()
                tot = timerE - timerS
                sys.stdout.write("\rTOTAL CLICKS: %d\nTIME SPENT CLICKING: %d" % (count, tot))
                sys.stdout.flush()
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
            time.sleep(t)

def check(t, ty):
    if ty == 1:
        try:
            float(t)
        except ValueError:
            print "That's not a valid number....\n\n"
            return False
        else:
            return True
    else:
        try:
            int(t)
        except ValueError:
            temp = float(t)
            if t % math.floor(temp) > 5:
                t = math.ceil(temp)
                print "That's not an integer.... Changing value to " + str(t)
                return t
            elif t % math.floor(temp) <= 5:
                t = math.floor(temp)
                print "That's not an integer.... Changing value to " + str(t)
                return t
        else:
            return t

def init():
    print "Type a click delay as a FLOATING POINT NUMBER or INTEGER (not recommended \
unless you want a long delay) and press ENTER. 0.1 is a good starting value: "
    foo = raw_input()
    return foo      

def pause():
    temp = int(d)
    if extraInfo == True:
        print "\n"
    raw_input("Press ENTER to resume. There will be a " + str(temp) + " second delay before the clicker resumes")
    clock(d)
    click(x, y, t)

def isKeyPressed(key):
    return (win32api.GetKeyState(key) & (1 << 7)) != 0

def clock(f):
    f = int(f)
    while f > 0:
        print f
        time.sleep(1)
        f -= 1

def menu():
    global extraInfo
    global d
    global t
    if extraInfo == True:
        print "\n"
    print "Type one of the following numbers and press ENTER to edit that value:"
    print "(1) Change delay time after un-pausing"
    print "(2) Change click delay time"
    if extraInfo == False:
        print "(3) Display extra info (May cause performance drop)"
    else:
        print "(3) Disable extra info"
    print "(4) Exit menu and return to auto click after " + str(d) + " seconds"
    choice = raw_input()
    while True:
        try:
            int(choice)
        except ValueError:
            print "Invalid command.... Try again."
            choice = raw_input()
        else:
            choice = int(choice)
            if choice in (1, 2, 3, 4):
                break
            else:
                print "Invalid command.... Try again."
                choice = raw_input()
    if choice == 1:
        tempp = int(d)
        print "Type in a new INTEGER value for the un-pause delay and press ENTER."
        print "Current value: " + str(tempp)
        temp = raw_input("New value: ")
        itemp = check(temp, 2)
        while not itemp:
            temp = raw_input("New value: ")
            itemp = check(temp, 2)
        float(itemp)
        d = itemp
        menu()
    elif choice == 2:
        print "Type in a new FLOAT value for the click delay and press ENTER."
        print "Current value: " + str(t)
        temp = raw_input("New value: ")
        itemp = check(temp, 1)
        while not itemp:
            temp = raw_input("New value: ")
            itemp = check(temp, 1)
        temp = float(temp)
        t = temp
        menu()
    elif choice == 3:
        if extraInfo == False:
            print "Extra info enabled"
            extraInfo = True
        else:
            print "Extra info disabled"
            extraInfo = False
        menu()
    elif choice == 4:
        print "Auto clicker resuming in " + str(d) + " seconds."
        clock(d)
        click(x, y, t)

def terminate():
    sys.exit()

print "<**><**><**><**>WELCOME TO THE AUTO-CLICKER<**><**><**><**>\n"
print "==========================READ ME=========================="
print "|There is a 5 second delay before auto-clicker will begin |"
print "|Press (P) to pause                                       |"
print "|Press (I) to access the menu                             |"
print "|Press (X) to terminate the program                       |"
print "==========================================================="
t = init()
i = check(t, 1)
while not i:
    t = init()
    i = check(t, 1)
clock(d)
t = float(t)
click(x, y, t)
