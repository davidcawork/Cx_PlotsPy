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



ocupacion_teorica = (0.80, 0.24,0,0.20,0,0.60,0.70,0.12,0,0.18,0.50,0.45)
ocupacion_sim = (0.8069,0.2403,0,0.2064,0,0.6030,0.7049,0.1201,0,0.1800,0.5076,0.45)
ocupacion_sim_err=(0.031901616, 0.00501488, 0, 0.020003681,0, 0.020788954,0.023793987,0.00250744,0,0.007058405,0.018253989,0.001767958)


index = np.arange(len(ocupacion_teorica))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(index - width/2, ocupacion_teorica, width, color='SkyBlue', label='Ocupación Teórica')
rects2 = ax.bar(index + width/2, ocupacion_sim, width, yerr=ocupacion_sim_err, color='Teal', label='Ocupación Simulada')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Ocupación')
plt.yticks(np.arange(0,1,0.1))
plt.grid(True)
ax.set_title('Ocupación en los Enlaces')
#ax.set_xticks(ind)
ax.set_xticks(index + width / 2)
ax.set_xticklabels(('a-b', 'b-a', 'a-c', 'c-a', 'b-c','c-b','b-bd','bd-b','c-bd','bd-c','adsl-ul','adsl-dl'))
ax.legend()



autolabel(rects1, "left")
autolabel(rects2, "right")

plt.show()