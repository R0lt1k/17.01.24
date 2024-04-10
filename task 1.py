import time
def create_file(file):
    time.sleep(1)
    with open(file, 'w') as file:
        file.write('')
        
create_file('file.txt')
