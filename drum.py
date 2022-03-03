import random
import subprocess
import time

tones = ["s", "bom", "t", "k", "p", "f"]
# tones = ["poffertjes", "crackertjes"]
while True:
    duration = random.randrange(0, 500) / 1000

    if True:  # random.randrange(0, 100) > 25:
        subprocess.run(["say", random.choice(tones), "-r", "700"])

    # time.sleep(duration)


