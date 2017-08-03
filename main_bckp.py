# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
usinp = "MA_SMPL1"
#usinp = (raw_input('-> '))#ввод имени, открываемого файла
#print "user input: ", type(usinp)
len_usinp = len(str(usinp))
#print type(len_usinp)
usinp_e = usinp + 'e' + '.csv'
#print usinp_e
#название файла без разширения, для отображения на граффике
usinp_title = usinp[0:-4]
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
frame = pd.read_csv(usinp_e, sep = ";", header = None, names = ['V', 'mA 1 cell', 'mA 2 cell'], skiprows = 1)

allarray = np.array(frame)
#print allarray
V = np.array(frame['V'])
#print x
ma1 = np.array(frame['mA 1 cell'])
#print y
ma2 = np.array(frame['mA 2 cell'])
#print mv



#зона вывода графф
plt.figure(num = 1, dpi= 300)
plt.suptitle(usinp_title, fontsize=16)
plt.subplots_adjust(hspace=0.4)#
#первый графф
plt.subplot(2,1,1)
plt.plot(V, ma1, V,ma2)
plt.xlabel('V, mV')
plt.ylabel('I, mA')
plt.title(u'Вольт-амперная характеристика', fontsize=12)
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
plt.figure(1).savefig(usinp_title + 'e' + '.png')
plt.figure(1).savefig(usinp_title + 'e' + '.pdf')
plt.show()
