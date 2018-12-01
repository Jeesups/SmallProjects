from pylab import *
figure(figsize=(12,8),dpi = 100) #1200x800 pixeli
x = linspace(-2*pi,2*pi,100)
subplot(2,2,1)
plot(x,sin(x))
subplot(2,2,2)
plot(x,sin(x)/x)
subplot(2,2,3)
plot(x,exp(-x**2))
subplot(224)
plot(x,sqrt(1-x**2))
show()