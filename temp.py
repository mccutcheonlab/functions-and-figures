import JM_general_functions as jmf
import matplotlib.pyplot as plt
import numpy as np

def licklengthFig(ax, data, contents = '', color='grey'):          
    if len(data['longlicks']) > 0:
        longlicklabel = str(len(data['longlicks'])) + ' long licks,\n' +'max = ' + '%.2f' % max(data['longlicks']) + ' s.'        
    else:
        longlicklabel = 'No long licks.'
    
    figlabel = str(len(data['licklength'])) + ' total licks.\n' + longlicklabel

    ax.hist(data['licklength'], np.arange(0, 0.3, 0.01), color=color)
    ax.text(0.9, 0.9, figlabel, ha='right', va='top', transform = ax.transAxes)
    ax.set_xlabel('Lick length (s)')
    ax.set_ylabel('Frequency')
    ax.set_title(contents)




metafile = 'R:\\DA_and_Reward\\fn55\\QPP1_metafile.txt'
medfolder = 'R:\\DA_and_Reward\\fn55\\QPP-1 (fn55)\\Pretrain 16-05-18\\'
tablerows, header = jmf.metafilereader(metafile)

data={}
data['medlicks'] = []
data['intake'] = []

for i in tablerows:
    if i[5] == '16/05/2018':
        file = medfolder + i[0]
        data['medlicks'].append(jmf.medfilereader(file, varsToExtract=['b', 'c'], remove_var_header=True))
        data['intake'].append(i[11])

data['licksperml'] = []
for licks, ml in zip(data['medlicks'], data['intake']):
    data['licksperml'].append(licks/ml)





f1 = plt.figure()
ax = f1.add_subplot(1,1,1)
ax.scatter(data['medlicks'], data['intake'])

average_ratio = np.mean(data['licksperml'])
sd_ratio = np.std(data['licksperml'])

ax.text(0,0, 'Average {.2f} {.2f} licks per ml'.format(average_ratio, sd_ratio))



print('hey')



# file = 'R:\\DA_and_Reward\\fn55\QPP-1 (fn55)\\Pref test Quin 0 21-05-18\\!2018-05-21_13h55m.Subject QPP1.5197'


# cas_on,cas_off,malt_on,malt_off = jmf.medfilereader(file, varsToExtract=['b', 'c', 'e', 'f'], remove_var_header=True)

# file = 'R:\\DA_and_Reward\\kp259\\DPCP3\\med\\!2017-11-26_12h13m.Subject dpcp3.18'

# cas_on,cas_off = jmf.medfilereader(file, varsToExtract=['e', 'f'], remove_var_header=True)

# casdata = jmf.lickCalc(cas_on, offset=cas_off)

# f1 = plt.figure()
# ax = f1.add_subplot(1,1,1)

# licklengthFig(ax, casdata)

# plt.show()

# alllonglicks = np.sum(casdata['longlicks'])

# print('Done')