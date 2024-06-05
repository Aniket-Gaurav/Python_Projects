import numpy as np

temperatures = np.array([22, 24, 19, 21, 25, 20, 23])
print(temperatures)

print(temperatures[0])


print(temperatures[:3])


reshaped = temperatures.reshape((7, 1))
print(reshaped)


week2_temperatures = np.array([24, 25, 22, 23, 26, 21, 24])

combined = np.vstack((temperatures, week2_temperatures))
print(combined)


avg_temp = np.mean(temperatures)
print(avg_temp)

adjusted_temps = temperatures + 2
print(adjusted_temps)


high_temps = temperatures[temperatures > 22]
print(high_temps)


sorted_temps = np.sort(temperatures)
print(sorted_temps)
