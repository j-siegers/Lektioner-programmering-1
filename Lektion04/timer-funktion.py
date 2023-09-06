import time
for i in range(10):
    print('-', end='')
    time.sleep(0.5)
print('\n')

my_list = [" ̶", "\\", "|", "/"]
for i in range(10):
    print(f"\r{my_list[0]}", end="")
    time.sleep(0.3)
    print(f"\r{my_list[1]}", end="")
    time.sleep(0.3)
    print(f"\r{my_list[2]}", end="")
    time.sleep(0.3)
    print(f"\r{my_list[3]}", end="")
    time.sleep(0.3)