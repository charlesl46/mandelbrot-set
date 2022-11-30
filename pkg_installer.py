import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'bs4'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'selenium'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'tqdm'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'requests'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'urllib'])

print('All libraries were nicely installed')
