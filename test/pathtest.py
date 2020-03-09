import os


PRJ_FLDR = os.path.dirname(os.path.realpath(__file__))

print(os.getcwd())

if os.getcwd() != PRJ_FLDR:
    os.chdir(PRJ_FLDR)
    print(os.getcwd())
    
else:
    print("already in project folder")
    
# print("project folder " + PRJ_FLDR)
# apptemplates = os.path.abspath(os.path.join(PRJ_FLDR))
# print('apptemplates= '+ apptemplates)

# with open(f'{os.path.abspath(os.path.join(PRJ_FLDR))}/testpathfolder/sample.txt', 'w') as f:
#     f.write('Lorem ipsum dolor sit amet, consectetur adipisciing elit.')