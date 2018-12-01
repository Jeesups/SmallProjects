from pylab import *
fig = figure (figsize=(12,8), dpi = 100)
#marginesy
fig.subplots_adjust(left = 0.20,bottom = 0.1, right = 0.8,top=0.85,wspace = 0.5,hspace = 0.2)

matplotlib.rc('axes',linewidth = 3) #grubosc ramki
matplotlib.rc('font',family='serif',size=10)#fonty
matplotlib.rc('axes',titlesize = 180) #font tytulu
matplotlib.rc('axes',labelsize = 14) #font opisu osi
matplotlib.rc('axes',edgecolor=(0.62,0.3,0))#kolor ramki
matplotlib.rc('axes',facecolor=(1.0,0.9,0.75))#kolor tla
matplotlib.rc('xtick.major',size =10) #x-kreska podzialki
matplotlib.rc('ytick.major',size= 5) #y-kreska podzialki
x=linspace(-2*pi,2*pi,100)
subplot(221)
plot(x,sin(x), c = 'red')
title(u'Tytul')
xlabel(u'os-x')
ylabel(u'os-y')
subplot(222)
plot(x,sin(x)/x,lw = 3,ls='--')
title("$y(x) = \\frac{\\sin x}{x}$")
grid()#siatka
subplot(223)
plot(x,exp(-x**2),label="$y(x) = e^{-x^2}$")
legend(loc = 3, prop={'size':16})#zmiana rozmiaru legendy
subplot(224)
plot(x,x**2,c='green',ls='',marker="*")
text(-3,30,"dodatkowy opis")
text(-6.3,20,u"dodatkowy duży opis",fontsize = 16)
#savefig("../pics/mpl_08.png")#zapisz do pliku
show()