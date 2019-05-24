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



retardo_teorico = (0.018,0.01254,0.00062)
Retardo_sim = (0.0181,0.0186,0)
#Retardo_sim_err= (0.331863536, 0.001540341, 0.0444078,0.020436927,0.070376684,0.00194687)


index = np.arange(len(retardo_teorico))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(index - width/2, retardo_teorico, width, color='seagreen', label='Pb teórica')
rects2 = ax.bar(index + width/2, Retardo_sim, width,  color='lightgreen', label='Pb simulada')

# Add some text for labels, title and custom x-axis tick labels, etc.
#ax.set_ylabel('Retardo (seg)')
plt.yticks(np.arange(0,0.05,0.005))
plt.grid(True)
ax.set_title('Pb extremo a extremo')
#ax.set_xticks(ind)
ax.set_xticks(index + width / 2)
ax.set_xticklabels(('A - B', 'A-C-TF-C','B-TF-C'))
ax.legend()



autolabel(rects1, "left")
autolabel(rects2, "right")

plt.show()