import matplotlib.pyplot as plt  
data = [1,11,21,31,41,51] 
plt.hist(data, bins=[0,10,20,30,40,50,60], weights=[10,1,40,33,6,8], 
edgecolor="black", color="red") 
plt.title("Example of a Histogram") 
plt.xlabel("Data Values") 
plt.show()