import numpy as np
import matplotlib.pyplot as plt

men_means, men_std = (0.024854, 0.012296, 0.006338, 0.003103, 0.00209, 0.00151,0.00130), (0.001123, 0.000864, 0.000608, 0.000368, 0.000331, 0.000325, 0.000276)


ind = np.arange(len(men_means))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, men_means, width, yerr=men_std,
                color='Coral', label='Ocupación')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Porcentaje medio de Ocupación')
ax.set_title('Ocupación media del Enlace Londres hacia Dublín')
ax.set_xticks(ind)
plt.yticks(np.arange(0,0.03,0.005))
plt.grid(True)
ax.set_xticklabels(('Exp(1)', 'Exp(2)', 'Exp(3)', 'Exp(4)', 'Exp(5)','Exp(6)','Exp(7)'))
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


autolabel(rects1, "right")


plt.show()