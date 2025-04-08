import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
data = pd.read_csv("study_data.csv")

# Show first few rows
print("Data Preview:")
print(data.head())

# Plot
plt.scatter(data["Hours"], data["Score"])
plt.title("Study Hours vs Score")
plt.xlabel("Hours")
plt.ylabel("Score")
plt.grid(True)
plt.show()
