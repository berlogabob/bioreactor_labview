# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
usinp = "lux_v.txt"
#usinp = (raw_input('-> '))#ввод имени, открываемого файла
#print "user input: ", type(usinp)
len_usinp = len(str(usinp))
#print type(len_usinp)
usinp_e = usinp[0:-4] + 'e' + usinp[-4:len_usinp]
#print usinp_e
#название файла без разширения, для отображения на граффике
usinp_title = usinp[0:-4]

#создаем датафрэйм
frame = pd.read_csv(usinp_e, sep = "\t", header = None, names = ['lux', 'diode V', 'pwm', 'photocell V'], skiprows = 1)

allarray = np.array(frame)
#print allarray
lux = np.array(frame['lux'])
#print x
diode = np.array(frame['diode V'])
#print y
pwm = np.array(frame['pwm'])
photocell = np.array(frame['photocell V'])
#print mv

"""
"""

#зона вывода графф
plt.figure(num = 1, figsize=(10,6), dpi= 300)
plt.suptitle(usinp_title, fontsize=16)
#plt.subplots_adjust(hspace=0.4)#
#первый графф
#plt.subplot(2,1,1)
plt.plot(photocell, lux)
plt.xlabel('Volts')
plt.ylabel('lux')
#plt.title(u'Вольт-амперная характеристика', fontsize=12)
plt.grid(True)
#второй графф
"""
plt.subplot(2,1,2)
plt.plot(mv, ma, '-r')
plt.xlabel('Volts, mV')
plt.ylabel('I, mA')
plt.title(u'Вольт-амперная характеристика', fontsize=12)
plt.grid(True)
"""
#вывод
plt.figure(1).savefig(usinp_title + '_photocell' + '.png')
plt.figure(1).savefig(usinp_title + '_photocell' + '.pdf')
#plt.show()
