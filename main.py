# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
usinp = "MP_SMPL1"
#usinp = (raw_input('-> '))#ввод имени, открываемого файла
#print "user input: ", type(usinp)
len_usinp = len(str(usinp))
#print type(len_usinp)
usinp_e = usinp + 'e' + '.csv'
#print usinp_e
#название файла без разширения, для отображения на граффике
usinp_title = usinp
#
s = open(usinp).read()#прочитали исходный файл

#блок замен
#s = s.replace('"', '')#удаляем кавычки
#s = s.replace('sec', '"sec"')#удаляем кавычки
#s = s.replace('mA', '"mA"')#удаляем кавычки
#s = s.replace('mV', '"mV"')#удаляем кавычки
#s = s.replace('    ', '\t')#меняем запятую на точкуу
s = s.replace(',', '.')#меняем запятую на точкуу
#s = s.replace('\n', ', ')#замена новой строки на запятую
#s = s.replace(',', '\t')#замена запятой символом табуляции
#s = s.replace('.', ',')#замена точки заятой

#создаем новый файл для записывания в него изменений
f = open(usinp_e, 'w')#открыли файл (создали)
f.write(s)#записали
f.close()#закрыли

#создаем датафрэйм
frame = pd.read_csv(usinp_e, sep = "\t", header = None, names = ['Time', 'Cur1', 'Volt1', 'Volt2', 'Volt3', 'Cur4'], skiprows = 1)

allarray = np.array(frame)
#print allarray
Time = np.array(frame['Time'])
#print x
Cur1 = np.array(frame['Cur1'])
#print y
Cur2 = np.array(frame['Cur1'])
Volt1 = np.array(frame['Volt1'])
Volt2 = np.array(frame['Volt2'])
Volt3 = np.array(frame['Volt3'])
Cur4 = np.array(frame['Cur4'])



#зона вывода графф
plt.figure(num = 1, dpi= 300)
#plt.suptitle(usinp_title, fontsize=16)
#plt.subplots_adjust(hspace=0.4)#
#первый графф
#plt.subplot(2,1,1)
plt.plot(Time, Volt3, "b")
plt.xlabel('Time, s')
plt.ylabel('Voltage, V')
#plt.title(u'Вольт-амперная характеристика', fontsize=12)
plt.grid(True)
"""
#второй графф
plt.subplot(2,1,2)
plt.plot(mv, ma, '-r')
plt.xlabel('Volts, mV')
plt.ylabel('I, mA')
plt.title(u'Вольт-амперная характеристика', fontsize=12)
plt.grid(True)
"""
#вывод
plt.draw()
plt.figure(1).savefig(usinp_title + 'e' + '.png')
plt.figure(1).savefig(usinp_title + 'e' + '.pdf')
#plt.show()
