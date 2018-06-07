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

metafile = 'QPP1_metafile.txt'
medfolder = 'C:\\Users\\jaimeHP\\Documents\\Test Data\\'
tablerows, header = jmf.metafilereader(metafile)

data={}
data['licks'] = []
data['intake'] = []
data['nlicks'] = []
data['offset'] = []
data['lickdata'] = []

for i in tablerows:
    if i[5] == '16/05/2018':
        file = medfolder + i[0]
        medlicks = jmf.medfilereader(file, varsToExtract=['e', 'f'], remove_var_header=True)
        data['licks'].append(medlicks[0])
        data['offset'].append(medlicks[1])
        data['nlicks'].append(len(medlicks[0]))
        data['intake'].append(int(i[11]))
        data['lickdata'].append(jmf.lickCalc(medlicks[0], offset=medlicks[1]))

data['licksperml'] = []
for licks, ml in zip(data['nlicks'], data['intake']):
    try:
        data['licksperml'].append(licks/ml)
    except ZeroDivisionError:
        data['licksperml'].append(0)

data['median_licklength'] = []
data['licks_adjusted'] = []

for i in data['lickdata']:
    i['median_licklength'] = np.median(i['licklength'])
    data['median_licklength'].append(i['median_licklength'])
    data['licks_adjusted'].append(np.sum(i['licklength']/i['median_licklength']))

f1 = plt.figure()
ax = f1.add_subplot(1,2,1)
ax.scatter(data['nlicks'], data['intake'])

average_ratio = np.mean(data['licksperml'])
sd_ratio = np.std(data['licksperml'])

ax.text(0,0, 'Average {:.1f} \u00B1 {:.1f} licks per ml'.format(average_ratio, sd_ratio))

ax2 = f1.add_subplot(1,2,2)
ax.scatter(data['licks_adjusted'], data['intake'])

plt.show()

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