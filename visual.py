# Import necessary libraries
import matplotlib.pyplot as plt

# Data for the plots
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Line plot
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.plot(x, y, marker='o')
plt.title('Line Plot')
plt.xlabel('X')
plt.ylabel('Y')

# Scatter plot
plt.subplot(1, 3, 2)
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')

# Bar chart
plt.subplot(1, 3, 3)
plt.bar(x, y)
plt.title('Bar Chart')
plt.xlabel('X')
plt.ylabel('Y')

# Layout so plots do not overlap
plt.tight_layout()

# Display the plot
plt.show()
