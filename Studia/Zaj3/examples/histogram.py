from pylab import *
import matplotlib.pyplot as plt
f = figure(figsize=(3,5),dpi = 100)
f.subplots_adjust(hspace = 0.4,bottom = 0.02)
subplot(211)
x=randn(1000)
hist(x,50)
title("histogram")
subplot(212)
x = [1,2,3,4]
l=map(str,x)
e = [0,0,0.05,0]
labels = 'Python','C++','Ruby','Java'
sizes =[250,140,210,200]
colors = ['gold','yellowgreen','lightcoral','lightskyblue']
explode=(0.1,0,0,0)
plt.pie(sizes,explode = explode,labels = labels, colors = colors,autopct='%1.1f%%',shadow = True,startangle = 140)
plt.axis('equal')
title('wykres kolowy')
savefig('hist.png')
show()