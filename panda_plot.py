"""
Plotting
Pandas uses the plot() method to create diagrams.

We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.

"""


#Three lines to make our compiler able to draw:
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')

# Plot the data
df.plot()

# Save the plot to a file (e.g., PNG)
plt.savefig('plot.png')

# Show the plot in a new window
plt.show()

df.plot(kind='bar')


# Save the plot
plt.savefig('bar_plot.png')
# Show plot
plt.show()



df['Calories'].plot(kind='hist', bins=10)
# Save the plot
plt.savefig('histogram.png')
# Show plot
plt.show()



df['Calories'].plot(kind='box')
# Save the plot
plt.savefig('box_plot.png')
# Show plot
plt.show()




df.plot(kind='scatter', x='Duration', y='Calories')
# Save the plot
plt.savefig('scatter_plot.png')
# Show plot
plt.show()




df['Duration'].value_counts().plot(kind='pie', autopct='%1.1f%%')
# Save the plot
plt.savefig('pie_chart.png')
# Show plot
plt.show()




df.plot(kind='area')
# Save the plot
plt.savefig('area_plot.png')
# Show plot
plt.show()



df.plot(kind='hexbin', x='Duration', y='Calories', gridsize=20)
# Save the plot
plt.savefig('hexbin_plot.png')
# Show plot
plt.show()



df.plot(kind='bar', stacked=True)
# Save the plot
plt.savefig('stacked_bar_plot.png')
# Show plot
plt.show()





import seaborn as sns
sns.violinplot(x='Duration', y='Calories', data=df)
# Save the plot
plt.savefig('violin_plot.png')
# Show plot
plt.show()



import seaborn as sns
sns.violinplot(x='Duration', y='Calories', data=df)
# Save the plot
plt.savefig('violin_plot.png')
# Show plot
plt.show()






import numpy as np

categories = ['Duration', 'Pulse', 'Maxpulse', 'Calories']
values = df.loc[0, categories]

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
values = values.tolist()

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='blue', alpha=0.25)
ax.plot(angles, values, color='blue', linewidth=2)
# Save the plot
plt.savefig('radar_chart.png')
# Show plot
plt.show()
