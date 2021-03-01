# Вариант 12
# RGB <--> XYZ <--> HLS
from tkinter import *
from tkinter import messagebox, colorchooser
import colorsys

MainWindow = Tk()
MainWindow.title("Салей Илья, 3 курс, 13 группа")
MainWindow.attributes("-fullscreen", True)
MainWindow["bg"] = "#87CEEB"

varR = DoubleVar()
varR.set(0.0)
varG = DoubleVar()
varG.set(0.0)
varB = DoubleVar()
varB.set(0.0)

varX = DoubleVar()
varX.set(0.0)
varY = DoubleVar()
varY.set(0.0)
varZ = DoubleVar()
varZ.set(0.0)

varH = DoubleVar()
varH.set(0.0)
varL = DoubleVar()
varL.set(0.0)
varS = DoubleVar()
varS.set(0.0)

labWarning = Label(text="Warning: rounding has been performed",
                   font=("Times New Roman", "24"),
                   bg="#87CEEB",
                   fg="#FF0000")
labWarning.pack()
labWarning.place(relx=0.45, rely=0.01)
labWarning.place_forget()

btnExit = Button(text="Exit",
                 bg="#00BFFF",
                 fg="#000000",
                 font=("Times New Roman", "36"),
                 bd=10,
                 command=MainWindow.quit,
                 width=6)
btnExit.pack()
btnExit.place(relx=0.865, rely=0.85)

labAuthor = Label(text="Салей Илья, 3 курс, 13 группа, Вариант 12",
                  font=("Times New Roman", "24"),
                  bg="#87CEEB")
labAuthor.pack()
labAuthor.place(relx=0.01, rely=0.01)

labChosenColor = Label(text="Selected color",
                  font=("Times New Roman", "28"),
                  bg="#87CEEB")
labChosenColor.pack()
labChosenColor.place(relx=0.83, rely=0.01)

canvas = Canvas(width=780,
                height=650,
                bg="#000000",
                highlightbackground="#00BFFF")
canvas.place(relx=0.485, rely=0.075)

colorDialog = colorchooser.Chooser(MainWindow)

def openColorDialog():
    global varR
    global varG
    global varB
    global varX
    global varY
    global varZ
    global varH
    global varL
    global varS
    color = colorDialog.show()
    varR.set(int(color[0][0]))
    varG.set(int(color[0][1]))
    varB.set(int(color[0][2]))
    xyz_list = FromRgbToXYZ(varR.get(), varG.get(), varB.get())
    varX.set(xyz_list[0])
    varY.set(xyz_list[1])
    varZ.set(xyz_list[2])
    hls_list = FromRgbToHLS(varR.get(), varG.get(), varB.get())
    varH.set(hls_list[0])
    varL.set(hls_list[1])
    varS.set(hls_list[2])
    canvas.config(bg=color[1])

btnChooseColor = Button(text="Color from palette",
                        bg="#00BFFF",
                        fg="#000000",
                        font=("Times New Roman", "36"),
                        bd=10,
                        command=openColorDialog,
                        width=20)
btnChooseColor.pack()
btnChooseColor.place(relx=0.49, rely=0.85)

def FromRGBtoColorHex(R, G, B):
    return '#%02x%02x%02x' % (int(R.get()), int(G.get()), int(B.get()))

def g(x):
    if x >= 0.04045:
        return ((x + 0.055)/1.055) ** 2.4
    else:
        return x/12.92

def FromRgbToXYZ(R, G, B):
    xyz_list = []
    Rn = g(R / 255)*100
    Gn = g(G / 255)*100
    Bn = g(B / 255)*100
    X = Bn * 0.180437 + Gn * 0.357576 + Rn * 0.412456
    Y = Bn * 0.072175 + Gn * 0.715152 + Rn * 0.212673
    Z = Bn * 0.950304 + Gn * 0.119192 + Rn * 0.0193339
    if X > 100.0 or Y > 100.0 or Z > 100.0:
        labWarning.place(relx=0.45, rely=0.01)
    else:
        labWarning.place_forget()
    xyz_list.append(X)
    xyz_list.append(Y)
    xyz_list.append(Z)
    return xyz_list

def FromXYZtoRgb(X, Y, Z):
    X /= 100
    Y /= 100
    Z /= 100
    R = 3.2404542 * X - 1.5371385 * Y - 0.4985314 * Z
    G = -0.9692660 * X + 1.8760108 * Y + 0.0415560 * Z
    B = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    R *= 255
    G *= 255
    B *= 255
    rgb_list = [R, G, B]
    if rgb_list[0] > 255.0 or rgb_list[1] > 255.0 or rgb_list[2] > 255.0:
        labWarning.place(relx=0.45, rely=0.01)
    else:
        labWarning.place_forget()
    return rgb_list

def FromRgbToHLS(R, G, B):
    R /= 255
    G /= 255
    B /= 255
    hls_list = list(colorsys.rgb_to_hls(R, G, B))
    hls_list[0] *= 100
    hls_list[1] *= 100
    hls_list[2] *= 100
    return hls_list

def FromHLStoRgb(H, L, S):
    H /= 100
    L /= 100
    S /= 100
    rgb_list = list(colorsys.hls_to_rgb(H, L, S))
    rgb_list[0] *= 255
    rgb_list[1] *= 255
    rgb_list[2] *= 255
    return rgb_list

def changeColorFromRGB(scaleInfo):
    global canvas
    global varR
    global varG
    global varB
    global varX
    global varY
    global varZ
    global varH
    global varL
    global varS
    xyz_list = FromRgbToXYZ(varR.get(), varG.get(), varB.get())
    varX.set(xyz_list[0])
    varY.set(xyz_list[1])
    varZ.set(xyz_list[2])
    hls_list = FromRgbToHLS(varR.get(), varG.get(), varB.get())
    varH.set(hls_list[0])
    varL.set(hls_list[1])
    varS.set(hls_list[2])
    canvas.config(bg=FromRGBtoColorHex(varR, varG, varB))

def changeColorFromXYZ(scaleInfo):
    global canvas
    global varR
    global varG
    global varB
    global varX
    global varY
    global varZ
    global varH
    global varL
    global varS
    rgb_list = FromXYZtoRgb(varX.get(), varY.get(), varZ.get())
    varR.set(rgb_list[0])
    varG.set(rgb_list[1])
    varB.set(rgb_list[2])
    hls_list = FromRgbToHLS(varR.get(), varG.get(), varB.get())
    varH.set(hls_list[0])
    varL.set(hls_list[1])
    varS.set(hls_list[2])
    canvas.config(bg=FromRGBtoColorHex(varR, varG, varB))

def changeColorFromHLS(scaleInfo):
    global canvas
    global varR
    global varG
    global varB
    global varX
    global varY
    global varZ
    global varH
    global varL
    global varS
    rgb_list = FromHLStoRgb(varH.get(), varL.get(), varS.get())
    varR.set(rgb_list[0])
    varG.set(rgb_list[1])
    varB.set(rgb_list[2])
    xyz_list = FromRgbToXYZ(varR.get(), varG.get(), varB.get())
    varX.set(xyz_list[0])
    varY.set(xyz_list[1])
    varZ.set(xyz_list[2])
    canvas.config(bg=FromRGBtoColorHex(varR, varG, varB))

labRGB = Label(text="RGB - 0, ..., 255",
               font=("Times New Roman", "48"),
               bg="#87CEEB")
labRGB.pack()
labRGB.place(relx=0.11, rely=0.065)

labRGB_R = Label(text="R",
               font=("Times New Roman", "36"),
               bg="#87CEEB")
labRGB_R.pack()
labRGB_R.place(relx=0.01, rely=0.15)

scrollR = Scale(bg="#00BFFF",
                activebackground="#7B68EE",
                fg="#000000",
                highlightbackground="#00BFFF",
                bd=3,
                orient=HORIZONTAL,
                sliderlength=20,
                length=256,
                width=20,
                to=255,
                relief="ridge",
                troughcolor="#ADD8E6",
                command=changeColorFromRGB,
                variable=varR)
scrollR.pack()
scrollR.place(relx=0.06, rely=0.15)

textR = Entry(MainWindow,
              width=10,
              bd=5,
              font=("Times New Roman", "32"),
              textvariable=varR,
              state="disabled")
textR.place(relx=0.24, rely=0.147)

btnSetR_Flag = True

def SetR_Foo():
    global varR
    global btnSetR_Flag
    if btnSetR_Flag:
        textR.config(state="normal")
        btnSetR.config(text="Confirm R")
        btnSetR_Flag = False
    else:
        changeColorFromRGB("SetR_Foo")
        textR.config(state="disabled")
        btnSetR.config(text="Set R")
        btnSetR_Flag = True

btnSetR = Button(text="Set R",
                        bg="#00BFFF",
                        fg="#000000",
                        font=("Times New Roman", "14"),
                        bd=10,
                        command=SetR_Foo,
                        padx=5,
                        pady=5,
                        width=8)
btnSetR.pack()
btnSetR.place(relx=0.4, rely=0.147)

labRGB_G = Label(text="G",
               font=("Times New Roman", "36"),
               bg="#87CEEB")
labRGB_G.pack()
labRGB_G.place(relx=0.01, rely=0.225)

scrollG = Scale(bg="#00BFFF",
                activebackground="#7B68EE",
                fg="#000000",
                highlightbackground="#00BFFF",
                bd=3,
                orient=HORIZONTAL,
                sliderlength=20,
                length=256,
                width=20,
                to=255,
                relief="ridge",
                troughcolor="#ADD8E6",
                command=changeColorFromRGB,
                variable=varG)
scrollG.pack()
scrollG.place(relx=0.06, rely=0.225)

textG = Entry(MainWindow,
              width=10,
              bd=5,
              font=("Times New Roman", "32"),
              textvariable=varG,
              state="disabled")
textG.place(relx=0.24, rely=0.222)

btnSetG_Flag = True

def SetG_Foo():
    global varG
    global btnSetG_Flag
    if btnSetG_Flag:
        textG.config(state="normal")
        btnSetG.config(text="Confirm G")
        btnSetG_Flag = False
    else:
        changeColorFromRGB("SetG_Foo")
        textG.config(state="disabled")
        btnSetG.config(text="Set G")
        btnSetG_Flag = True

btnSetG = Button(text="Set G",
                        bg="#00BFFF",
                        fg="#000000",
                        font=("Times New Roman", "14"),
                        bd=10,
                        command=SetG_Foo,
                        padx=5,
                        pady=5,
                        width=8)
btnSetG.pack()
btnSetG.place(relx=0.4, rely=0.222)

labRGB_B = Label(text="B",
               font=("Times New Roman", "36"),
               bg="#87CEEB")
labRGB_B.pack()
labRGB_B.place(relx=0.01, rely=0.3)

scrollB = Scale(bg="#00BFFF",
                activebackground="#7B68EE",
                fg="#000000",
                highlightbackground="#00BFFF",
                bd=3,
                orient=HORIZONTAL,
                sliderlength=20,
                length=256,
                width=20,
                to=255,
                relief="ridge",
                troughcolor="#ADD8E6",
                command=changeColorFromRGB,
                variable=varB)
scrollB.pack()
scrollB.place(relx=0.06, rely=0.3)

textB = Entry(MainWindow,
              width=10,
              bd=5,
              font=("Times New Roman", "32"),
              textvariable=varB,
              state="disabled")
textB.place(relx=0.24, rely=0.297)

btnSetB_Flag = True

def SetB_Foo():
    global varB
    global btnSetB_Flag
    if btnSetB_Flag:
        textB.config(state="normal")
        btnSetB.config(text="Confirm B")
        btnSetB_Flag = False
    else:
        changeColorFromRGB("SetB_Foo")
        textB.config(state="disabled")
        btnSetB.config(text="Set B")
        btnSetB_Flag = True

btnSetB = Button(text="Set B",
                        bg="#00BFFF",
                        fg="#000000",
                        font=("Times New Roman", "14"),
                        bd=10,
                        command=SetB_Foo,
                        padx=5,
                        pady=5,
                        width=8)
btnSetB.pack()
btnSetB.place(relx=0.4, rely=0.297)

labXYZ = Label(text="XYZ - 0, ..., 100 %",
               font=("Times New Roman", "48"),
               bg="#87CEEB")
labXYZ.pack()
labXYZ.place(relx=0.11, rely=0.375)

labXYZ_X = Label(text="X",
               font=("Times New Roman", "36"),
               bg="#87CEEB")
labXYZ_X.pack()
labXYZ_X.place(relx=0.01, rely=0.46)

scrollX = Scale(bg="#00BFFF",
                activebackground="#7B68EE",
                fg="#000000",
                highlightbackground="#00BFFF",
                bd=3,
                orient=HORIZONTAL,
                sliderlength=20,
                length=256,
                width=20,
                to=100,
                relief="ridge",
                troughcolor="#ADD8E6",
                command=changeColorFromXYZ,
                variable=varX)
scrollX.pack()
scrollX.place(relx=0.06, rely=0.46)

textX = Entry(MainWindow,
              width=10,
              bd=5,
              font=("Times New Roman", "32"),
              textvariable=varX,
              state="disabled")
textX.place(relx=0.24, rely=0.457)

btnSetX_Flag = True

def SetX_Foo():
    global varX
    global btnSetX_Flag
    if btnSetX_Flag:
        textX.config(state="normal")
        btnSetX.config(text="Confirm X")
        btnSetX_Flag = False
    else:
        changeColorFromXYZ("SetX_Foo")
        textX.config(state="disabled")
        btnSetX.config(text="Set X")
        btnSetX_Flag = True

btnSetX = Button(text="Set X",
                        bg="#00BFFF",
                        fg="#000000",
                        font=("Times New Roman", "14"),
                        bd=10,
                        command=SetX_Foo,
                        padx=5,
                        pady=5,
                        width=8)
btnSetX.pack()
btnSetX.place(relx=0.4, rely=0.457)

labXYZ_Y = Label(text="Y",
               font=("Times New Roman", "36"),
               bg="#87CEEB")
labXYZ_Y.pack()
labXYZ_Y.place(relx=0.01, rely=0.535)

scrollY = Scale(bg="#00BFFF",
                activebackground="#7B68EE",
                fg="#000000",
                highlightbackground="#00BFFF",
                bd=3,
                orient=HORIZONTAL,
                sliderlength=20,
                length=256,
                width=20,
                to=100,
                relief="ridge",
                troughcolor="#ADD8E6",
                command=changeColorFromXYZ,
                variable=varY)
scrollY.pack()
scrollY.place(relx=0.06, rely=0.535)

textY = Entry(MainWindow,
              width=10,
              bd=5,
              font=("Times New Roman", "32"),
              textvariable=varY,
              state="disabled")
textY.place(relx=0.24, rely=0.532)

btnSetY_Flag = True

def SetY_Foo():
    global varY
    global btnSetY_Flag
    if btnSetY_Flag:
        textY.config(state="normal")
        btnSetY.config(text="Confirm Y")
        btnSetY_Flag = False
    else:
        changeColorFromXYZ("SetY_Foo")
        textY.config(state="disabled")
        btnSetY.config(text="Set Y")
        btnSetY_Flag = True

btnSetY = Button(text="Set Y",
                        bg="#00BFFF",
                        fg="#000000",
                        font=("Times New Roman", "14"),
                        bd=10,
                        command=SetY_Foo,
                        padx=5,
                        pady=5,
                        width=8)
btnSetY.pack()
btnSetY.place(relx=0.4, rely=0.532)

labXYZ_Z = Label(text="Z",
               font=("Times New Roman", "36"),
               bg="#87CEEB")
labXYZ_Z.pack()
labXYZ_Z.place(relx=0.01, rely=0.61)

scrollZ = Scale(bg="#00BFFF",
                activebackground="#7B68EE",
                fg="#000000",
                highlightbackground="#00BFFF",
                bd=3,
                orient=HORIZONTAL,
                sliderlength=20,
                length=256,
                width=20,
                to=100,
                relief="ridge",
                troughcolor="#ADD8E6",
                command=changeColorFromXYZ,
                variable=varZ)
scrollZ.pack()
scrollZ.place(relx=0.06, rely=0.61)

textZ = Entry(MainWindow,
              width=10,
              bd=5,
              font=("Times New Roman", "32"),
              textvariable=varZ,
              state="disabled")
textZ.place(relx=0.24, rely=0.607)

btnSetZ_Flag = True

def SetZ_Foo():
    global varZ
    global btnSetZ_Flag
    if btnSetZ_Flag:
        textZ.config(state="normal")
        btnSetZ.config(text="Confirm Z")
        btnSetZ_Flag = False
    else:
        changeColorFromXYZ("SetZ_Foo")
        textZ.config(state="disabled")
        btnSetZ.config(text="Set Z")
        btnSetZ_Flag = True

btnSetZ = Button(text="Set Z",
                        bg="#00BFFF",
                        fg="#000000",
                        font=("Times New Roman", "14"),
                        bd=10,
                        command=SetZ_Foo,
                        padx=5,
                        pady=5,
                        width=8)
btnSetZ.pack()
btnSetZ.place(relx=0.4, rely=0.607)

labHLS = Label(text="HLS - 0, ..., 100 %",
               font=("Times New Roman", "48"),
               bg="#87CEEB")
labHLS.pack()
labHLS.place(relx=0.11, rely=0.685)

labHLS_H = Label(text="H",
               font=("Times New Roman", "36"),
               bg="#87CEEB")
labHLS_H.pack()
labHLS_H.place(relx=0.01, rely=0.77)

scrollH = Scale(bg="#00BFFF",
                activebackground="#7B68EE",
                fg="#000000",
                highlightbackground="#00BFFF",
                bd=3,
                orient=HORIZONTAL,
                sliderlength=20,
                length=256,
                width=20,
                to=100,
                relief="ridge",
                troughcolor="#ADD8E6",
                command=changeColorFromHLS,
                variable=varH)
scrollH.pack()
scrollH.place(relx=0.06, rely=0.77)

textH = Entry(MainWindow,
              width=10,
              bd=5,
              font=("Times New Roman", "32"),
              textvariable=varH,
              state="disabled")
textH.place(relx=0.24, rely=0.767)

btnSetH_Flag = True

def SetH_Foo():
    global varH
    global btnSetH_Flag
    if btnSetH_Flag:
        textH.config(state="normal")
        btnSetH.config(text="Confirm H")
        btnSetH_Flag = False
    else:
        changeColorFromHLS("SetH_Foo")
        textH.config(state="disabled")
        btnSetH.config(text="Set H")
        btnSetH_Flag = True

btnSetH = Button(text="Set H",
                        bg="#00BFFF",
                        fg="#000000",
                        font=("Times New Roman", "14"),
                        bd=10,
                        command=SetH_Foo,
                        padx=5,
                        pady=5,
                        width=8)
btnSetH.pack()
btnSetH.place(relx=0.4, rely=0.767)

labHLS_L = Label(text="L",
               font=("Times New Roman", "36"),
               bg="#87CEEB")
labHLS_L.pack()
labHLS_L.place(relx=0.01, rely=0.845)

scrollL = Scale(bg="#00BFFF",
                activebackground="#7B68EE",
                fg="#000000",
                highlightbackground="#00BFFF",
                bd=3,
                orient=HORIZONTAL,
                sliderlength=20,
                length=256,
                width=20,
                to=100,
                relief="ridge",
                troughcolor="#ADD8E6",
                command=changeColorFromHLS,
                variable=varL)
scrollL.pack()
scrollL.place(relx=0.06, rely=0.845)

textL = Entry(MainWindow,
              width=10,
              bd=5,
              font=("Times New Roman", "32"),
              textvariable=varL,
              state="disabled")
textL.place(relx=0.24, rely=0.842)

btnSetL_Flag = True

def SetL_Foo():
    global varL
    global btnSetL_Flag
    if btnSetL_Flag:
        textL.config(state="normal")
        btnSetL.config(text="Confirm L")
        btnSetL_Flag = False
    else:
        changeColorFromHLS("SetL_Foo")
        textL.config(state="disabled")
        btnSetL.config(text="Set L")
        btnSetL_Flag = True

btnSetL = Button(text="Set L",
                        bg="#00BFFF",
                        fg="#000000",
                        font=("Times New Roman", "14"),
                        bd=10,
                        command=SetL_Foo,
                        padx=5,
                        pady=5,
                        width=8)
btnSetL.pack()
btnSetL.place(relx=0.4, rely=0.842)

labHLS_S = Label(text="S",
               font=("Times New Roman", "36"),
               bg="#87CEEB")
labHLS_S.pack()
labHLS_S.place(relx=0.01, rely=0.92)

scrollS = Scale(bg="#00BFFF",
                activebackground="#7B68EE",
                fg="#000000",
                highlightbackground="#00BFFF",
                highlightcolor="#FFFFFF",
                bd=3,
                orient=HORIZONTAL,
                sliderlength=20,
                length=256,
                width=20,
                to=100,
                relief="ridge",
                troughcolor="#ADD8E6",
                command=changeColorFromHLS,
                variable=varS)
scrollS.pack()
scrollS.place(relx=0.06, rely=0.92)

textS = Entry(MainWindow,
              width=10,
              bd=5,
              font=("Times New Roman", "32"),
              textvariable=varS,
              state="disabled")
textS.place(relx=0.24, rely=0.917)

btnSetS_Flag = True

def SetS_Foo():
    global varL
    global btnSetS_Flag
    if btnSetS_Flag:
        textS.config(state="normal")
        btnSetS.config(text="Confirm S")
        btnSetS_Flag = False
    else:
        changeColorFromHLS("SetS_Foo")
        textS.config(state="disabled")
        btnSetS.config(text="Set S")
        btnSetS_Flag = True

btnSetS = Button(text="Set S",
                        bg="#00BFFF",
                        fg="#000000",
                        font=("Times New Roman", "14"),
                        bd=10,
                        command=SetS_Foo,
                        padx=5,
                        pady=5,
                        width=8)
btnSetS.pack()
btnSetS.place(relx=0.4, rely=0.917)

MainWindow.mainloop()
