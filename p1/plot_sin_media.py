import numpy as np
import matplotlib.pyplot as plt

men_means = (57360, 43481) #medias


ind = np.arange(len(men_means))  # the x locations for the groups
print(str(ind))
width = 0.20  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, men_means, width,
                color='SkyBlue', label='Lecturas')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Lecturas')
ax.set_title('Número de lecturas')
ax.set_xticks(ind)
plt.yticks(np.arange(0,80000,10000))
#plt.grid(True) #Reja
ax.set_xticklabels(('Bubble Sort', 'Bubble Sort Optimizado')) #Barras titulos
ax.legend()


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                    '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "center")


plt.show()
