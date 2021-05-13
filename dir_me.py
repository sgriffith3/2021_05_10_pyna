import os

for item in os.listdir("/home/student/pyna"):
    result = os.path.isdir(f'/home/student/pyna/{item}') 
    if result:
        print(f"Directory:\t{item}")
    else: 
        print(f"File:\t{item}")
