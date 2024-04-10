import time
def create_file(file):
    time.sleep(1)
    with open(file, 'w') as file:
        file.write('')
        
start = time.time()
for i in range(1,101):
    create_file(f'file{i}.txt')
end = time.time()
print("Время : ", end - start)
