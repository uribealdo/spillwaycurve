# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:21:00 2020
@author: UribeAldo
"""
import matplotlib.pyplot as plt # combines namespace of numpy and pyplot
import numpy as np
##Vertedero de cresta redonda Bollrich
g=9.81 # gravity m/s2
u=0.55
print("\nINPUT:")
Q=float(input ("Qd (m3/s):"))
k=50
b=np.linspace(1,16,k)
h=(Q/(2/3*u*b*(2*g)**0.5))**(2/3)
#Ancho efectivo
Kp=0.05 #Pillar contraction coefficient
Ka=0.1 #Abutment contraction coefficient
n=0 #Numero de pilares
be=b-2*(n*Kp+Ka)*h
h=(Q/(2/3*u*be*(2*g)**0.5))**(2/3)
#Plotting##########
figura=plt.figure(1)
plt.plot(b,h,color='blue',linewidth=1)
cs=plt.plot([b],[h],'ro',markersize=3)
#plt.colorbar()
plt.xlabel('b [m]')
plt.ylabel('h [m]')
plt.title("Spillway Curve")
plt.text(0.5*b[k-1], 0.5*h[0],r'Q = $\frac{2}{3}\mu \mathrm{b}\mathrm{h^{3/2}}\sqrt{2g}$',fontsize=12)
plt.grid(True)
plt.axis([0,b[k-1] , 0, h[0]])
#########Condicion limite#########
bo=[3,5.5,10,13.5]#float(input ("bo (m):"))
ho=np.zeros(len(bo))
beo=np.zeros(len(bo))
for j in range(len(bo)):
    ho[j]=(Q/(2/3*u*bo[j]*(2*g)**0.5))**(2/3)
    beo[j]=bo[j]-2*(n*Kp+Ka)*ho[j]
    ho[j]=(Q/(2/3*u*beo[j]*(2*g)**0.5))**(2/3)
    # Trazo una línea vertical en la coordenada x=10 color rojo (r)
    # y con trazo punteado
    plt.axvline(bo[j], color='r', ymax=ho[j]/h[0],ls="dotted")
    # Línea horizontal en la coordenada y=10.4 color verde (g)
    # que termina en la limitad de la gráfica (0.5, va de 0 a 1)
    plt.axhline(ho[j], color='g', xmax=bo[j]/b[k-1],ls="dotted")
    # Banda horizontal de y=0 a y=2 de color azul
    # y 30% de transparencia (alpha=0.3)
    #plt.axhspan(0,0.5, alpha=0.3, color='b')
    # Banda vertical de x=0 a x=4 de color amarillo
    # y 30% de transparencia
    plt.axvspan(0, 3*ho[j], alpha=0.3, color='y')
    plt.text(.95*bo[j], 1.1*ho[j],str('('+'%.1f'%bo[j]+','+'%.2f'%ho[j]+')'),fontsize=10)
print("\nQdesign:","%.2f" % Q,"m3/s")
plt.savefig('D:/PYTHON/APL-Task6/curves_spillway', dpi=1200)