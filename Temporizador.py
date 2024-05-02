from time import sleep
min = int(input("Qtos minutos:"))


for m in range(min):
    for s in range(60):
        print(f'{m:02d}:{s:02d}')
        sleep(1)
print(f'{min:02d}:00')
