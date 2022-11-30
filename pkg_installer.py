import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pysimplegui'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'matplotlib'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'tqdm'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'numpy'])

print('All libraries were nicely installed')
import PySimpleGUI as sg
