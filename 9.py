import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=np.random.randint(0,101,size=50)
plt.figure(figsize=(14,10))
plt.subplot(2,2,1)
plt.plot(data,marker='o',linestyle='-',color='b')
plt.title('line chart')
plt.xlabel('index')
plt.ylabel('value')
plt.grid(True)

plt.subplot(2,2,2)
plt.scatter(range(len(data)),data,color='r',alpha=0.7)
plt.title('scatter plot')
plt.xlabel('index')
plt.ylabel('value')
plt.grid(True)

#  plot 3 : Histogram
plt.subplot(2,2,3)
plt.hist(data,bins=10,color='g'  ,edgecolor="black")
plt.title("Histogram")
plt.xlabel('value')
plt.ylabel("Frequency")
plt.grid(True)

#  plot 4 : Box Plot 
plt.subplot(2,2,4)
sns.boxenplot(data,color="purple")
plt.title("Box plot")
plt.xlabel("Data")
plt.grid(True)

#  Adjust layout 
plt.tight_layout()

#  show the plots
plt.show()