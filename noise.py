import random
import pysine
import subprocess


tones = [391.9954, 493.8833, 659.2551, 783.9909]
while True:
    duration = random.randrange(0, 5) / 10

    if True:  # random.randrange(0, 100) > 25:
        # duration
        pysine.sine(random.choice(tones), duration=duration)

    else:
        time.sleep(duration)

    # if random.randint(0, 10) >= 9:
    #     subprocess.run(["say", "oh yeah"])
    # subprocess.run(["say", "yeah"])
