import cv2
import pytesseract
from tkinter import *
from tkinter.filedialog import askopenfilename
from multi_stage_process import *
from PIL import Image, ImageTk


def ImgToTxt():
    global txt
    filename = askopenfilename()
    pytesseract.pytesseract.tesseract_cmd='path/to/tesseract.exe' #change the path as per your file
    img = cv2.imread(filename)
    gray = get_grayscale(img)
    thresh = thresholding(gray)
    txt = pytesseract.image_to_string(thresh)
    print(txt)
    raw_img=Image.open(filename)
    img2=ImageTk.PhotoImage(raw_img)
    w=img2.width()
    h=int((img2.height()/w)*500)
    fin_img=raw_img.resize((500, h), Image.ANTIALIAS)
    img2=ImageTk.PhotoImage(fin_img)
    lab.configure(image=img2)
    lab.image=img2
    txtbox.delete("1.0","end")
    txtbox.insert(END, txt)
    #button position change
    B.configure(image=buttonTxt, height=51, width=197)
    B.place( x = 350 , y = 140)


# UI <front-end>

frame = Tk()
# set Title
frame.title('Simulacrum Processing')

# Set the Geometry
#1830x800
#getting screen width and height of display
width= frame.winfo_screenwidth() 
height= frame.winfo_screenheight()
#setting tkinter window size
frame.geometry("%dx%d" % (width, height))
bgImg = PhotoImage(file="./img/bgrd.png")
background_label = Label(image=bgImg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
frame.state('zoomed')

#Header button Upload image
HeaderButtionIcon1 = PhotoImage(file="./img/headesUploadImg.png")
HBU = Button(frame,image=HeaderButtionIcon1, fg="#303030", bg="#303030", borderwidth=0, highlightthickness=0,pady=0, padx=0, command = ImgToTxt)
HBU.place( x = 1160, y = 25)

#<Help Frame UI>
PopUPImg = PhotoImage(file="./img/pop.png")
def popup():
    top= Toplevel(frame)
    top.geometry("474x474")
    top.title("Simulacrum Processing")
    HelpImg=Label(top, image=PopUPImg,width = 474,height =474)
    HelpImg.place(x=0,y=0,relwidth=1, relheight=1)

#Header button Help image
HeaderButtionIcon2 = PhotoImage(file="./img/headesHelpImg.png")
HBH = Button(frame,image=HeaderButtionIcon2, fg="#303030", bg="#303030", borderwidth=0, highlightthickness=0,pady=0, padx=0, command = popup)
HBH.place( x = 1355, y = 25)

#output img label
uploadImg = PhotoImage(file="./img/upload_img.png")
buttonTxt = PhotoImage(file="./img/txtButton.png")
lab = Label(frame, bg="#FBEAEB", fg="#303030" ,image=uploadImg, width = 500)
lab.place( x=200 , y=210)

# Output TextBox Creation
txtbox = Text(frame,width = 50,font=("Poppins bold", 12))
txtbox.place( x = 860 , y=210)
 
#button
ButtonIcon = PhotoImage(file="./img/buttonIco.png")
B = Button(frame,image=ButtonIcon, bg="#FBEAEB", fg="#303030", borderwidth=0, highlightthickness=0,pady=0, padx=0, command = ImgToTxt)
B.place( x = 390 , y = 380)

frame.mainloop()