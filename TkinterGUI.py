from tkinter import *
from PIL import ImageTk, Image  
import os
# IMPORTANT - https://yangcha.github.io/iview/iview.html for finding (x, y) at any point of any image

def next_frame(nframe):
    nframe.tkraise()

def run_ic():
    os.system('python InvisibleCloak.py')

def run_qr():
    os.system('python QRscanner.py')

def run_fc():
    os.system('python Finger_counter.py')

def run_vc():
    os.system('python Vol_Hand_Control.py')

root = Tk()
root.state('zoomed')     # "IT WILL MAXIMIZE THE WINDOW AS SOON AS WE OPEN AND IT WILL BE FIXED"
root.title("Welcome to OpenCV Projects")
root.geometry("1350x700+0+0")  # 1920x1080 is the size of window starting from (0,0)
# root.configure(bg="#0b3954")

main_frame = Frame(root, bg="#0b3954")       #.place(x=0,y=0, relheight=1, relwidth=1)
fingercounter_frame = Frame(root) 
volumecontrol_frame = Frame(root)
virtualmouse_frame = Frame(root)
invisiblecloak_frame = Frame(root)
qrcode_frame = Frame(root)

for frame in (main_frame, fingercounter_frame, volumecontrol_frame, virtualmouse_frame, invisiblecloak_frame, qrcode_frame):
    frame.place (x=0,y=0, relheight=1, relwidth=1)

main_frame.tkraise()

# 1. FINGER COUNTER
fingercounter_frame.configure(bg="#0b3954")
infcframe = Frame(fingercounter_frame)
infcframe.place(x=250, y=100, height = 500, width=800)
fcLabel3 = Label(infcframe, text = "In this project,\nwe are using Opencv with mediapipe library.\nMake sure that:\n\n1.Camera shutter is open\n2.Only one hand at a time\n3.If you are using your right hand\n  then face your palm towards the screen\n4.If you are using your left hand\n   then face your palm towards you.\n5.Press Q to exit the Program.", justify=LEFT, font=("Times", 15))
fcLabel3.place(x=20, y=0.1, height=400, width = 370)
fcLabel1 = Label(infcframe, text = "1. Finger Counter", relief=SUNKEN, justify=CENTER, font=("Arial Bold", 25))
fcLabel1.place(x=25, y=25, height=50, width=350)
fcLabel2 = Label(infcframe, relief=SUNKEN)
fcLabel2.place(x=400, y=10, height=400, width=415)


fcimg1 = Image.open('Images\\fingercounter2.jpg')
fcimg2 = fcimg1.resize((400,200), Image.ANTIALIAS)
fcimg3 = ImageTk.PhotoImage(fcimg2)
fcBottom_label = Label(infcframe, image = fcimg3)
fcBottom_label.place(x =410,y = 100, height= 200, width = 400)
fcStatus_label = Label(infcframe, relief=SUNKEN)
fcStatus_label.place(x=15, y= 420, height = 90, width = 800)
fcstatus_Button = Button(infcframe, text = "Run Project", command = run_fc)
fcstatus_Button.place(height = 70, width = 200,  x=400, y = 425)
fcback_Button = Button(infcframe, text = "Back", command = lambda: next_frame(main_frame))
fcback_Button.place(height = 70, width = 200,  x=100, y = 425)

# 2. VOLUME CONTROL
volumecontrol_frame.configure(bg="#0b3954")
invfframe = Frame(volumecontrol_frame)
invfframe.place(x=250, y=100, height = 500, width=800)
vcLabel3 = Label(invfframe, text = "In this project,\nwe are using Opencv, pycaw and mediapipe.\nMake sure that:\n\n1.Camera shutter is open\n2.Only one hand at a time\n3.Only use your Index finger and Thumb\n4.If you increase the distance between fingers \n   then volume will increase and vice versa.\n5.Press Q to exit the Program.", justify=LEFT, font=("Times", 15))
vcLabel3.place(x=20, y=0.1, height=400, width = 370)
vcLabel1 = Label(invfframe, text = "2. Volume Control", relief=SUNKEN, justify=CENTER, font=("Arial Bold", 25))
vcLabel1.place(x=25, y=25, height=50, width=350)
vcLabel2 = Label(invfframe, relief=SUNKEN)
vcLabel2.place(x=400, y=10, height=400, width=415)


vcimg1 = Image.open('Images\\volumecontrol.jpg')
vcimg2 = vcimg1.resize((400,200), Image.ANTIALIAS)
vcimg3 = ImageTk.PhotoImage(vcimg2)
vcBottom_label = Label(invfframe, image = vcimg3)
vcBottom_label.place(x =410,y = 100, height= 200, width = 400)
vcStatus_label = Label(invfframe, relief=SUNKEN)
vcStatus_label.place(x=15, y= 420, height = 90, width = 800)
vcstatus_Button = Button(invfframe, text = "Run Project", command = run_vc)
vcstatus_Button.place(height = 70, width = 200,  x=400, y = 425)
vcback_Button = Button(invfframe, text = "Back", command = lambda: next_frame(main_frame))
vcback_Button.place(height = 70, width = 200,  x=100, y = 425)

# 3. QR code scanner 
qrcode_frame.configure(bg="#0b3954")
inqrframe = Frame(qrcode_frame)
inqrframe.place(x=250, y=100, height = 500, width=800)
qrLabel3 = Label(inqrframe, text = "In this project,\nwe are using Opencv with pyzbar.\nMake sure that:\n\n1.Camera shutter is open\n2.Try showing Text QR\n3.Press Q to exit the Program.", justify=LEFT, font=("Times", 15))
qrLabel3.place(x=0.1, y=0.1, height=400, width = 370)
qrLabel1 = Label(inqrframe, text = "3. QR Code Scanner", relief=SUNKEN, justify=CENTER, font=("Arial Bold", 25))
qrLabel1.place(x=25, y=25, height=50, width=350)
qrLabel2 = Label(inqrframe, relief=SUNKEN)
qrLabel2.place(x=400, y=10, height=400, width=415)


qrimg1 = Image.open('Images\\qrcode.png')
qrimg2 = qrimg1.resize((400,200), Image.ANTIALIAS)
qrimg3 = ImageTk.PhotoImage(qrimg2)
qrBottom_label = Label(inqrframe, image = qrimg3)
qrBottom_label.place(x =410,y = 100, height= 200, width = 400)
qrStatus_label = Label(inqrframe, relief=SUNKEN)
qrStatus_label.place(x=15, y= 420, height = 90, width = 800)
qrstatus_Button = Button(inqrframe, text = "Run Project", command = run_qr)
qrstatus_Button.place(height = 70, width = 200,  x=400, y = 425)
qrback_Button = Button(inqrframe, text = "Back", command = lambda: next_frame(main_frame))
qrback_Button.place(height = 70, width = 200,  x=100, y = 425)


# 4. INVISIBLE CLOAK
invisiblecloak_frame.configure(bg="#0b3954")
inicframe = Frame(invisiblecloak_frame)
inicframe.place(x=250, y=100, height = 500, width=800)
icLabel3 = Label(inicframe, text = "In this project,\nwe are using Opencv.\nMake sure that:\n\n1.Camera shutter is open\n2.The program requires initial 5 seconds to\n   scan the background\n3.Then you can stand in front of the camera \n   and blend yourself using plain red cloth.\n4.Press Q to exit the Program.", justify=LEFT, font=("Times", 15))
icLabel3.place(x=20, y=0.1, height=400, width = 370)
icLabel1 = Label(inicframe, text = "4. Invisible Cloak", relief=SUNKEN, justify=CENTER, font=("Arial Bold", 25))
icLabel1.place(x=25, y=25, height=50, width=350)
icLabel2 = Label(inicframe, relief=SUNKEN)
icLabel2.place(x=400, y=10, height=400, width=415)


icimg1 = Image.open('Images\\invisiblecloak.jpeg')
icimg2 = icimg1.resize((400,200), Image.ANTIALIAS)
icimg3 = ImageTk.PhotoImage(icimg2)
icBottom_label = Label(inicframe, image = icimg3)
icBottom_label.place(x =410,y = 100, height= 200, width = 400)
icStatus_label = Label(inicframe, relief=SUNKEN)
icStatus_label.place(x=15, y= 420, height = 90, width = 800)
icstatus_Button = Button(inicframe, text = "Run Project", command = run_ic)
icstatus_Button.place(height = 70, width = 200,  x=400, y = 425)
icback_Button = Button(inicframe, text = "Back", command = lambda: next_frame(main_frame))
icback_Button.place(height = 70, width = 200,  x=100, y = 425)



# ---------END OF SUB FRAMES---------

# "TRIED TO ADD IMAGE LABEL IN ANOTHER FRAME"
#image_frame = Frame(root, bg= "red").place(x =0,y = 0, relwidth = 1, relheight = 1)
# x and y are starting positions of the frame, relwidth and relheight(0.0 - 1.0) are relative height and width to their parent 

# "TO RESIZE A IMAGE"
# img1 = Image.open('C:\\Users\\lenovo\\Downloads\\huaweibg.jpg')
# img2 = img1.resize((1920,1080), Image.ANTIALIAS)
# img3 = ImageTk.PhotoImage(img2)
mfimg3 = ImageTk.PhotoImage(Image.open('Images\\Opencvbg2.png'))
Bgimglabel = Label(main_frame, image = mfimg3)
Bgimglabel.place(x =0,y = 50, relwidth = 1, relheight = 1)

TitleHead = Label(main_frame, text="OpenCV Projects", font=("Times", 100), bg = '#0b3954',fg = '#ffffff')
TitleHead.place(x = 200, y=50)



Button1 = Button(main_frame, text="Finger Counter", command = lambda: next_frame(fingercounter_frame))
Button1.place(x = 590, y = 220)

Button2 = Button(main_frame, text="Volume Control", command = lambda: next_frame(volumecontrol_frame))
Button2.place(x = 765, y = 355)

Button3 = Button(main_frame, text="QR code Scanner", command = lambda: next_frame(qrcode_frame))
Button3.place(x = 590, y = 520)

Button4 = Button(main_frame, text="Invisible cloak", command = lambda: next_frame(invisiblecloak_frame))
Button4.place(x = 420, y = 355)


root.mainloop()