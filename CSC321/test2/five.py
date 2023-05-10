# This script generates random words between a random duration, pause halfway, rests for 2 secs and the continues
import time
import random

start_time = time.time()  # remember when we started
dur = random.randint(5, 7)
half_dur = dur/2
max_dur = start_time + dur
random_words = ["Big", "Small", "Peewee"]

print("Duration (sec): ", "0 sec -", dur, "sec")


while (time.time() - start_time) < dur:
  if (time.time() - start_time) <= half_dur or (time.time() - start_time) >= half_dur + 2:
    print(random_words[random.randint(0, 2)])

