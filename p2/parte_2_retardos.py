import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects, xpos='center'):
    

    xpos = xpos.lower()  
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  

    for rect in rects:
        print(str(rect))
        if rect == 0:
            
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()*offset['center'], 1.01*height,'{}'.format(height), ha=ha['center'], va='bottom')
        else:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,'{}'.format(height), ha=ha[xpos], va='bottom')



retardo_teorico = (0.5049,0.6791,0.1019)
Retardo_sim = (0.5504,0.8001,0.1355)
Retardo_sim_err= (0.090794726,0.074201071,0.001425918)


index = np.arange(len(retardo_teorico))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(index - width/2, retardo_teorico, width, color='gold', label='Retardo teórico')
rects2 = ax.bar(index + width/2, Retardo_sim, width, yerr=Retardo_sim_err, color='olive', label='Retardo simulado')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Retardo (seg)')
plt.yticks(np.arange(0,1,0.1))
plt.grid(True)
ax.set_title('Retardo extremo a extremo (seg)')
#ax.set_xticks(ind)
ax.set_xticks(index + width / 2)
ax.set_xticklabels(('A > BD', 'PC-c > BD','BD > PC-c'))
ax.legend()



autolabel(rects1, "left")
autolabel(rects2, "right")

plt.show()