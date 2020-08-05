#!/usr/bin/python
import subprocess
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib import ticker
from matplotlib.pyplot import cm 
import numpy as np
import pylab
import random
from math import exp,ceil,log
import sys
import os.path
from os import path
import numpy as np

#matplotlib.rcParams['ps.useafm'] = True
#matplotlib.rcParams['pdf.use14corefonts'] = True
#matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

wide = False
if wide:
    fig, ax = plt.subplots(figsize=(10,5)) 
else:    
    fig, ax = plt.subplots()    



plt.grid()
plt.gcf().subplots_adjust(bottom=0.15)

wb_file = 'fct_wb50_pint_mi0_log1.05_diffFreq.dat'
fb_file = 'fct_fb50_pint_mi0_log1.05_diffFreq.dat'

PINT_1_over_1___fb_95p = [float(line.split()[9]) for line in open(fb_file).readlines()[0:]]    # facebook
PINT_1_over_16__fb_95p = [float(line.split()[6])  for line in open(fb_file).readlines()[0:]]    # facebook
PINT_1_over_256_fb_95p = [float(line.split()[3])  for line in open(fb_file).readlines()[0:]]    # facebook

fb_x_axis = [int(line.split()[1]) for line in open(fb_file).readlines()[0:]] # fb flow sizes

PINT_1_over_1___wb_95p = [float(line.split()[9]) for line in open(wb_file).readlines()[0:]]    # facebook
PINT_1_over_16__wb_95p = [float(line.split()[6])  for line in open(wb_file).readlines()[0:]]    # facebook
PINT_1_over_256_wb_95p = [float(line.split()[3])  for line in open(wb_file).readlines()[0:]]    # facebook


wb_x_axis = [int(line.split()[1]) for line in open(wb_file).readlines()[0:]] # wb flow sizes

plt.plot(np.linspace(0, 10, num=20),PINT_1_over_256_wb_95p, color='purple'  , linestyle='-' , marker='o', markersize=9, alpha=1 , label='$p=1/256$',linewidth=4.0)
plt.plot(np.linspace(0, 10, num=20),PINT_1_over_16__wb_95p, color='blue'    , linestyle='-.', marker='*', markersize=9, alpha=1 , label='$p=1/16$' ,linewidth=4.0)
plt.plot(np.linspace(0, 10, num=20),PINT_1_over_1___wb_95p, color='green'   , linestyle='--' , marker='s', markersize=9, alpha=.5, label='$p=1$'    ,linewidth=4.0)


ax.set_xticks(range(1,11))
ax.set_xticklabels([str(x) if x < 1000 else str(int(x/1000. + .5)) + 'K' if x < 1000.**2 else str(int(x/1000.**2 + .5)) + 'M' for x in wb_x_axis[1::2]])

if wide:
    plt.legend(loc='upper left',prop={'size':23},ncol=1)
else:  
    plt.legend(loc='upper left',prop={'size':28},ncol=1)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='y', which='major', labelsize=28)
plt.ylabel(r'Slowdown', fontsize=28)    
plt.xlabel('Flow Size [Bytes]', fontsize=28)
plt.ylim([1,11])
#plt.yscale('log', basey=2)
#plt.xlim([0, maxPkts])
plt.tight_layout()
if wide:
    plt.savefig('ProbHPCC_PINT_wb_wide.pdf')
    plt.savefig('ProbHPCC_PINT_wb_wide.png') 
else: 
    plt.savefig('ProbHPCC_PINT_wb.pdf')
    plt.savefig('ProbHPCC_PINT_wb.png')
#plt.show()

plt.clf()
if wide:
    fig, ax = plt.subplots(figsize=(10,5)) 
else:    
    fig, ax = plt.subplots() 
plt.grid()
plt.gcf().subplots_adjust(bottom=0.15)

plt.ylim([1,11])
plt.plot(np.linspace(0, 10, num=20),PINT_1_over_256_fb_95p, color='purple'  , linestyle='-' , marker='o', markersize=9, alpha=1 , label='$p=1/256$',linewidth=4.0)
plt.plot(np.linspace(0, 10, num=20),PINT_1_over_16__fb_95p, color='blue'    , linestyle='-.', marker='*', markersize=9, alpha=1 , label='$p=1/16$' ,linewidth=4.0)
plt.plot(np.linspace(0, 10, num=20),PINT_1_over_1___fb_95p, color='green'   , linestyle='--' , marker='s', markersize=9, alpha=.5, label='$p=1$'    ,linewidth=4.0)

#plt.xticks(np.arange(len(wb_x_axis)), wb_x_axis)
#ax.set_xticks(np.linspace(wb_x_axis[0], wb_x_axis[-1], num=20))
ax.set_xticks(range(1,11))
ax.set_xticklabels([str(x) if x < 1000 else str(int(x/1000. + .5)) + 'K' if x < 1000.**2 else str(int(x/1000.**2 + .5)) + 'M' for x in fb_x_axis[1::2]])


if wide:
    plt.legend(loc='upper left',prop={'size':23},ncol=1)
else:  
    plt.legend(loc='upper left',prop={'size':28},ncol=1)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='y', which='major', labelsize=28)
plt.ylabel(r'Slowdown', fontsize=28)    
plt.xlabel('Flow Size [Bytes]', fontsize=28)
#plt.show()
plt.tight_layout()
if wide:
    plt.savefig('ProbHPCC_PINT_fb_wide.pdf')
    plt.savefig('ProbHPCC_PINT_fb_wide.png') 
else: 
    plt.savefig('ProbHPCC_PINT_fb.pdf')
    plt.savefig('ProbHPCC_PINT_fb.png')
exit()

HPCC = 0

#plt.tight_layout()
#for p in pRange:
#print histogram, 
for i,a in enumerate(aRange):
    linestyle = '-' if i < 3 else '--'
    if True:
        for j,p2 in enumerate(p2Range):
            if j > 2:
                linestyle = ':'
            if a != 7.75:
                continue
            #print 'HERE', hybridAverages
            #plt.plot(xrange(maxPkts+2),[k]+hybridAverages[p2][i], linestyle, label='Hybrid('+str(p2)+')')
            linestyle = '-'
            plt.plot(xrange(maxPkts+2),[k]+hybridAverages[p2][i], linestyle, label='Hybrid',linewidth=4.0)
            #plt.plot(xrange(maxPkts+2),[k]+hybridAverages[p2][i], linestyle, label='Hybrid('+str(p2)+','+str(a)+')')
    p = a/k
    #print histogram, 
    #print averages[i], p           
    #plt.plot(xrange(maxPkts+1),averages[i], linestyle, label=str(a) + ' / k')
    #plt.plot(xrange(maxPkts+2),[k]+averages[i], linestyle, label='XOR('+str(p)+')')
    #plt.plot(xrange(maxPkts+2),[k]+averages[i], linestyle, label='XOR')
    if True:
        #plt.plot(xrange(maxPkts+2),[k]+averages[i], linestyle, label='XOR('+str(a)+')')
        if a != 1:
            continue
        linestyle = '--'
        plt.plot(xrange(maxPkts+2),[k]+averages[i], linestyle, label='XOR',linewidth=4.0)
    sys.stdout.flush()

        
linestyle = ':'    
plt.plot(xrange(maxPkts+1),averagesCC, linestyle, label='Baseline',linewidth=4.0)    
plt.legend(loc='best',prop={'size':24},ncol=1)
plt.tick_params(axis='both', which='major', labelsize=28)
plt.ylabel(r'$E$[Missing Hops]', fontsize=28)    
plt.xlabel('Number of Packets', fontsize=28)
plt.xlim([0, maxPkts])
plt.savefig(fName+'.pdf')
plt.savefig(fName+'.png')
#plt.show()

