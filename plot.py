# Problem #10 : 26th Mar
# import the numpy and matplotlib modules
import numpy as np
import matplotlib.pyplot as plt
#set my range as 0 to 4, incrementing by 1 using the arange function (start,stop,step)
t = np.arange(0,4,1)
# define t as t itself, then t squared(t*t) , then 2t (t+t). The r- b- and g- define the colour of lines on the plotted graph.
plt.plot(t, t, 'r-', t, t*t, 'b-', t, t*2, 'g-')
# define the Label for the X axis
plt.xlabel('the input number')
# define the Label for the Y axis
plt.ylabel('the result')
# Show the plotted graph
plt.show()

