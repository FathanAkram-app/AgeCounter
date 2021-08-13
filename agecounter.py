from datetime import datetime
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import theme
sg.theme('topanga')
window = sg.Window(
    title="Your Lived", 
    layout=[
        [sg.Text(key="date",size=(21,2),font=('Oswald',32))]
    ], 
    
)
inputYear = int(input('year born: '))
inputMoth = int(input('month born: '))
inputDate = int(input('date born: '))


while window(timeout=20)[0] != sg.WIN_CLOSED:
    a = datetime.now() - datetime(inputYear, inputMoth, inputDate)
    window['date']("age "+str(a.total_seconds()/31536000))
    