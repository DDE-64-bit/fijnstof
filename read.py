import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

try:
    user_input = int(input("Enter an ID: "))
except ValueError():
    print("Please enter a valid input.")

filtered_data = data[data['id'] == user_input]

plt.plot(filtered_data['Time'], filtered_data['pm1'], label='pm 1')
plt.plot(filtered_data['Time'], filtered_data['pm2.5'], label='pm 2.5')
plt.plot(filtered_data['Time'], filtered_data['pm4'], label='pm 4')
plt.plot(filtered_data['Time'], filtered_data['pm10'], label='pm 10')

plt.xlabel('Time')
plt.ylabel('Amount')
plt.legend()

plt.show()