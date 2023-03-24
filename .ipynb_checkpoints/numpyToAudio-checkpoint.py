import numpy as np
from scipy.io.wavfile import write

# RATE = 44100
RATE = 10

testArr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 10, 10]]
npTestArr = np.array(testArr)
# data = np.random.uniform(
#     0.0, 10.0, RATE)  # 1 second worth of random samples between -1 and 1
# scaled = np.int16(data / np.max(np.abs(data)) * 32767)
# write('test.wav', RATE, scaled)

npFinalOutput = np.array([100, 200, 300])
for i in npTestArr:
    for j in range(RATE):
        npFinalOutput = np.append(npFinalOutput, i)

print(npFinalOutput)
