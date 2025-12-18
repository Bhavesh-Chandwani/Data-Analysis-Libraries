import matplotlib.pyplot as plt
import numpy as np
years = [2016, 2017, 2018, 2019, 2020]
dhoni = [850, 780, 720, 650, 500]
kohli = [1200, 1350, 1450, 1300, 1100]
rohit = [900, 1000, 1400, 1500, 1200]
x = np.arange(len(years))
width = 0.25
plt.bar(x-width, dhoni, width=width, label="MS Dhoni")
plt.bar(x, kohli, width=width, label="Virat Kohli")
plt.bar(x+width, rohit, width=width, label="Rohit Sharma")
plt.xlabel("Years")
plt.ylabel("Runs Scored")
plt.title("Comparison Graph of 5 Years")
plt.xticks(x, years)
plt.tight_layout
plt.legend()
plt.show()