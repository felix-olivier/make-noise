import random
import pysine


tones = [73.4162, 97.9989, 123.4708, 146.8324, 195.9977] # 9.1770    11.5623    13.7500    18.3540    23.1247    30.8677    36.7081    46.2493    61.7354    73.4162    97.9989   123.4708   146.8324   195.9977   246.9417   329.6276   391.9954   493.8833   659.2551   783.9909
while True:
    duration = random.randrange(0, 5) / 10

    if True:  # random.randrange(0, 100) > 25:
        # duration
        pysine.sine(random.choice(tones), duration=duration)

    else:
        time.sleep(duration)

