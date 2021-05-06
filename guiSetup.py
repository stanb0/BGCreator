import PySimpleGUI as sg
import imagedrawsquare

def windowInit():
    values=[0,0,0,0,0,0,0,0,0,0]
    #monitor size
    height=0
    width=0
    #background color
    bgR=0
    bgG=0
    bgB=0
    #line color
    R=0
    G=0
    B=0
    #line width
    linewidth=0
    #filename
    fn="wallpaper"

    sg.theme('dark green 3')

    monitor_size=[
        [sg.Text("Monitor Y")],[sg.Input(key='-Y-',size=(5,1))],
        [sg.Text("Monitor X")],[sg.Input(key='-X-',size=(5,1))]
    ]
    bg_RGB=[
        [sg.Text("Background Color")],
        [sg.Text("R")],[sg.Input(key='-bgR-',size=(5,1))],
        [sg.Text("G")],[sg.Input(key='-bgG-',size=(5,1))],
        [sg.Text("B")],[sg.Input(key='-bgB-',size=(5,1))]
    ]
    line_RGB=[
        [sg.Text("Line Color")],
        [sg.Text("R")],[sg.Input(key='-lineR-',size=(5,1))],
        [sg.Text("G")],[sg.Input(key='-lineG-',size=(5,1))],
        [sg.Text("B")],[sg.Input(key='-lineB-',size=(5,1))]
    ]
    finalOK=[
        [sg.Text("Filename")],[sg.Input(key='-fn-',size=(10,1))],
        [sg.Text("Line Width")],[sg.Input(key='-lineWidth-',size=(5,1))],
        [sg.Button("OK")]
    ]
    image_viewer=[
        [sg.Image(key='-IMAGE-')]
    ]
    layout = [
        [
            sg.Column(monitor_size),
            sg.Column(bg_RGB),
            sg.Column(line_RGB),
            sg.Column(finalOK),
            #sg.VerticalSeparator(pad=None),
            #sg.Column(image_viewer)
        ]
    ]

    window = sg.Window("wildpoptart",layout)

    while True:
        event, values = window.read()
        #monitor size
        height=int(values['-X-'])
        width=int(values['-Y-'])
        #background color
        bgR=int(values['-bgR-'])
        bgG=int(values['-bgG-'])
        bgB=int(values['-bgB-'])
        #line color
        R=int(values['-lineR-'])
        G=int(values['-lineG-'])
        B=int(values['-lineB-'])
        #line width (pixels)
        linewidth=int(values['-lineWidth-'])
        #Filename
        fn=(values['-fn-'])
        if fn=="":
            fn="wallpaper"
        #image preview

        if event == "OK" or event == sg.WIN_CLOSED:
            break
    window.close()

    values = [height,width,bgR,bgR,bgR,R,G,B,linewidth,fn]
    return    values
