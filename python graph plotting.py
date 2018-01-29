# importing the required module
import matplotlib.pyplot as plt
 
# x axis values
x1= [2000,4000,6000,8000,10000]
# corresponding y axis values
y1 = [0.000000,	0.031000, 0.062000 ,	0.109000   , 0.140000]
 
# plotting the points 
plt.plot(x1, y1, label= "Selection" )

# x axis values
x2= [2000,4000,6000,8000,10000]
# corresponding y axis values
y2=[0.015000	,0.031000	,0.078000	,0.171000	,0.265000]

# plotting the points 
plt.plot(x2, y2,label ="Bubble")

# x axis values
x3= [2000,4000,6000,8000,10000]
# corresponding y axis values
y3= [0.000000	,0.015000,	0.031000,	0.046000,	0.078000]

 # plotting the points 
plt.plot(x3, y3,label ="Insertion")

# x axis values
x4= [2000,4000,6000,8000,10000]
# corresponding y axis values
y4= [0,0,0,0,0]

 # plotting the points 
plt.plot(x4, y4,label ="Quick Sort")

# x axis values
x5= [2000,4000,6000,8000,10000]
# corresponding y axis values
y5= [0,0,0,0,0.015000 ]

 # plotting the points 
plt.plot(x5, y5,label ="Merge Sort")

# naming the x axis
plt.xlabel('Size of Array')
# naming the y axis
plt.ylabel('TIme(sec)')
 
# giving a title to my graph
plt.title('Time Complexities')

# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()
