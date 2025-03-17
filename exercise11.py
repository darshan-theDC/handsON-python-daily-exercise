#countdown timer

import time

seconds = int(input("Enter the time duration in seconds : "))

for i in range(seconds, 0, -1):
    print(f"00:00:{i:02}")
    time.sleep(1)
print("Happy birthday..!")