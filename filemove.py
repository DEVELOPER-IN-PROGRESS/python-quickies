import os

source_folder = 'D:/Chronopolis/Bell'
dest_folder = 'D:/Chronopolis/'

try:
    if os.path.exists(f'{dest_folder}/filename'):
        print('file Already Present at location ')
    else:
	    os.replace(f'{source_folder}/filename' , f'{dest_folder}/filename' )
	    print('File moved')
except FileNotFoundError:
    print('File Dosen\'t Exist')
