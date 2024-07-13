import matplotlib.pyplot as plt

# Data for plotting

categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 55, 70, 85]

# Create the plot

plt.figure(figsize=(10,6))
plt.bar(categories, values, color='slateblue')
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(True)


# Show the plot
plt.show()

