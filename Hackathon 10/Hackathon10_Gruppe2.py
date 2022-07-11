# -*- coding: utf-8 -*-
"""
Grundlagen der Informatik 2
Hackathon 10 - Gruppe2

24.01.2022
Eslem Kibar,6040452
Aynur Yalcin,6040468
Alan Akan,6053828

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 


#gelesene Daten
#Impfdatum,BundeslandId_Impfort,Impfstoff,Impfserie,Anzahl
data = np.genfromtxt("Aktuell_Deutschland_Bundeslaender_COVID-19-Impfungen.csv", delimiter=',',dtype="|U10", autostrip=True,skip_header=1)


#leereliste für die Impfungen in Bremen
bremenimpfungen=[]

#Filtern nach Bremen
A = np.where(data[:,1] == "04" )
bremenimpfungen=data[A]
        

#vom 1.1.21 - 31.12.21
bremenimpfungen_datum= bremenimpfungen[6:2112]  


#Liste mit erst Impfungen
B = np.where(bremenimpfungen_datum[:,3] == "1")
bremenimpfungen_1= bremenimpfungen_datum[B]

#filtern nach verschiedenen Impfdosen
#filterung nach Comirnaty
C = np.where(bremenimpfungen_1[:,2]=="Comirnaty")
comirnaty = bremenimpfungen_1[C]
#filterung nach Moderna
D = np.where(bremenimpfungen_1[:,2]=="Moderna")
moderna = bremenimpfungen_1[D]
#filterung nach Astra
E = np.where(bremenimpfungen_1[:,2]=="AstraZenec")
astrazeneca = bremenimpfungen_1[E]
#filterung nach Janssen
F = np.where(bremenimpfungen_1[:,2]=="Janssen")
janssen = bremenimpfungen_1[F]



dates = comirnaty[:,0]
dates1 = moderna[:,0]
dates2 = astrazeneca[:,0]
dates3 = janssen[:,0]



anzahl=bremenimpfungen_1[:,4]
comirnaty_anz = comirnaty[:,4]
moderna_anz = moderna[:,4]
astrazeneca_anz = astrazeneca[:,4]
janssen_anz = janssen[:,4]


#comirnaty
x = []
#moderna
x1 = []
#astra
x2 = []
#janssen
x3 = []

y=[]
for i in anzahl:
    y.append(int(i))
 #Aus String zu int werten 
for i in comirnaty_anz:
    x.append(int(i))
 #Aus String zu int werten    
for i in moderna_anz:
    x1.append(int(i))    
 #Aus String zu int werten    
for i in astrazeneca_anz:
    x2.append(int(i))  
 #Aus String zu int werten    
for i in janssen_anz:
    x3.append(int(i))    



#Plottennn!
fig, ax = plt.subplots() 
ax.plot(dates,x,'b',label="BioNTech/Pfizer")
ax.plot(dates1,x1,'orange',label="Moderna") 
ax.plot(dates2,x2,'r',label="AstraZeneca") 
ax.plot(dates3,x3,'g',label="Johnson&Johnson") 

ax.set_title("Erstimpfung in Bremen")
ax.set_xlabel("Datum")
ax.set_ylabel("Anzahl")
ax.legend(bbox_to_anchor=(1,0),loc='lower left')
ax.minorticks_on()
ax.axis(["2021-01-01", "2021-12-31",0,6000])
ax.xaxis.set_major_locator(mdates.MonthLocator())
fig.set_figheight(10)
fig.set_figwidth(20)
ax.grid(True,color='black',linewidth=0.5,linestyle='-',alpha=0.5)
plt.show()


#save the PLOT 

fig.savefig("Erstimpfung_in_Bremen.pdf")



#Maximum von Erstimpfungen und der Tag
#Comirnaty
xa=np.array(x)
com_max=np.where(xa==xa.max())  
print("Am "+str(*dates[com_max])+" wurden die meisten Personen mit BioNTech/Pfizer geimpft undzwar: "+str(*xa[com_max])+" Impfdosen") 
print("\n") 

#Moderna
xb=np.array(x1)
mod_max=np.where(xb==xb.max())  
print("Am "+str(*dates[mod_max])+" wurden die meisten Personen mit Moderna geimpft undzwar: "+str(*xb[mod_max])+" Impfdosen")    
print("\n") 

#Astra
xc=np.array(x2)
ast_max=np.where(xc==xc.max())  
print("Am "+str(*dates[ast_max])+" wurden die meisten Personen mit AstraZeneca geimpft undzwar: "+str(*xc[ast_max])+" Impfdosen")
print("\n") 

#Janssen
xd=np.array(x3)
jan_max=np.where(xd==xd.max())  
print("Am "+str(*dates[jan_max])+" wurden die meisten Personen mit Johnson&Johnson geimpft undzwar: "+str(*xd[jan_max])+" Impfdosen")   
print("\n")    