import random
import subprocess
import time

tones = ["say", "oh yeah", "Let's go", "get down", "superb"]
while True:
    duration = random.randrange(0, 1000) / 1000

    if True:  # random.randrange(0, 100) > 25:
        subprocess.run(["say", random.choice(tones), "-r", "50"])

    time.sleep(duration)


