import PySimpleGUI as sg
import mandelbrot_main as mandelbrot



def init_windows_layouts():

    title = 'Mandelbrot plot'
    size = (500,100)
    font = ('Courier New',11)
    sg.theme('DarkGrey4') 

    #LAYOUTS
    home_layout = [  [sg.Text('Welcome to this mandelbrot plot maker',size=(100,1),justification='c')],
                [sg.Button('Start')]]

    resolution_layout = [  [sg.Text('In which resolution would you like to plot ?')],
                [sg.InputText(key='-RESOLUTION-',tooltip='In pixels (px)',font=('Arial',11)),sg.Submit('OK')]]

    folder_layout = [ [sg.Text('In which folder would you like to save the plot ?')],
    [sg.T("Output Folder:", s=15, justification="r"), sg.I(key="-FOLDER-"), sg.FolderBrowse()],
    [sg.Submit('OK')]]

    color_system_layout = [[sg.Text('Which color system would you like to use ? (default : rgb)')],
    [sg.Listbox(['RGB','HSV'],key='-COLOR_SYSTEM-')],
    [sg.Checkbox('Random',key='-RANDOM-')],
    [sg.Submit('OK')]]



    #WINDOWS
    home_window = sg.Window(title,home_layout,font=font, size = size,element_justification='center')
    resolution_layout_window = sg.Window(title,resolution_layout,font=font,size = size,element_justification='center')
    folder_window = sg.Window(title,folder_layout,size=(800,100),font=font,element_justification='center')
    color_system_window = sg.Window(title,color_system_layout,size=(800,150),font=font,element_justification='center')
    return home_window,resolution_layout_window,folder_window,color_system_window

#EVENTS
def main():
    home_window,resolution_layout_window,folder_window,color_system_window = init_windows_layouts()
    while True:
        event,values = home_window.read()
        if event == sg.WIN_CLOSED : 
            home_window.close()
            break
        if event == "Start":
            home_window.close()
            event,values = resolution_layout_window.read()
            resolution = values["-RESOLUTION-"]
            print(resolution)
            resolution_layout_window.close()
            event,values = folder_window.read()
            folder = values["-FOLDER-"]
            print(folder)
            folder_window.close()
            event,values = color_system_window.read()
            c = values["-COLOR_SYSTEM-"]
            random = values["-RANDOM-"]
            print(c,random)
            color_system = 'rgb'
            if c == ['RGB']:
                color_system = 'rgb'
            elif c == ['HSV']:
                color_system = 'hsv'
            print(f'color system = {color_system}')
            color_system_window.close()
            mandelbrot_plot_layout1 = [[sg.Text('Start the plot ?')],[sg.Button('Start')]]
            mandelbrot_plot_window1 = sg.Window('Mandelbrot plot',mandelbrot_plot_layout1,size=(800,100),font=('Courier New',11),element_justification='center')
            mandelbrot_plot_layout2 = [[sg.Text('Finished')],[sg.Quit('Quit')]]
            mandelbrot_plot_window2 = sg.Window('Mandelbrot plot',mandelbrot_plot_layout2,size=(800,100),font=('Courier New',11),element_justification='center')
            event,values = mandelbrot_plot_window1.read()
            if event == "Start":
                mandelbrot.main(resolution,folder,color_system,random)
            mandelbrot_plot_window1.close()
            event,values = mandelbrot_plot_window2.read()
            if event == "Quit":
                mandelbrot_plot_window2.close()

            
    pass

main()



