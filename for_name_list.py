# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


name_list = ["MP_SMPL1", "MA_SMPL1",  "MA_SMPL2",  "MA_SMPL3",  "MA_SMPL4",  "MB_SMPL1", "MB_SMPL2", "MB_SMPL3", "MB_SMPL4", "MC_SMPL1", "MC_SMPL2", "MC_SMPL3", "MC_SMPL4"]

def plotprint(usinp):
    #usinp = i
    len_usinp = len(str(usinp))
    usinp_e = usinp + 'e' + '.csv'
    usinp_title = usinp
    s = open(usinp).read()#прочитали исходный файл
    s = s.replace(',', '.')#меняем запятую на точкуу
    f = open(usinp_e, 'w')#открыли файл (создали)
    f.write(s)#записали
    f.close()#закрыли
    frame = pd.read_csv(usinp_e, sep = "\t", header = None, names = ['Time', 'Cur1', 'Volt1', 'Volt2', 'Volt3', 'Cur4'], skiprows = 1)
    allarray = np.array(frame)
    Time = np.array(frame['Time'])
    Cur1 = np.array(frame['Cur1'])
    Cur2 = np.array(frame['Cur1'])
    Volt1 = np.array(frame['Volt1'])
    Volt2 = np.array(frame['Volt2'])
    Volt3 = np.array(frame['Volt3'])
    Cur4 = np.array(frame['Cur4'])
    plt.figure(num = 1, dpi= 300)
    #plt.suptitle(usinp_title, fontsize=16)
    plt.plot(Time, Volt3, "r")
    plt.xlabel('Time, s')
    plt.ylabel('Voltage, V')
    #plt.title(u'Вольт-амперная характеристика', fontsize=12)
    plt.grid(True)
    #вывод
    plt.draw()
    plt.figure(1).savefig(usinp_title + 'e' + '.png')
    plt.figure(1).savefig(usinp_title + 'e' + '.pdf')
    plt.clf()
for i in name_list:
    plotprint(i)
