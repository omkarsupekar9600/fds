import matplotlib.pyplot as plt 
import numpy as np 
#Creating an array of categorical data 
data = ('Java script', 'Java', 'Python', 'C#' ) 
p = [1,2,4,6,8,10] 
y = np.arange(len(data)) 
#Plotting the bar graph 
plt.bar(y, p, align='center', alpha=0.5, edgecolor='black') 
plt.xticks(y, data) 
plt.xlabel('Programming Languages') 
plt.ylabel('No. of Usage(%)') 
plt.title('Programming Languages Used in Projects')
plt.show()