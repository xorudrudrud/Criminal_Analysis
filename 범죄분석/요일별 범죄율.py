import csv
f = open(r"C:\Users\a14\Downloads\범죄발생_요일_2019.csv",encoding='euc-kr')
data = csv.reader(f)
sal = []
sung = []
ma = []
day = ['일요일','월요일','화요일','수요일','목요일','금요일','토요일']
for i in data:
    if '살인' in i[0]:
        for x in i[1:]:
            sal.append(int(x))
    if '성폭력' in i[0]:
        for j in i[1:]:
            sung.append(int(j))
    if '마약' in i[0]:
        for z in i[1:]:
            ma.append(int(z))
#         print(sal)
#         print(sung)
#         print(ma)
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
font_path = "C:\Windows\Fonts\H2GTRM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc("font", family = font)

x = np.arange(0,7)
fig,(ax1,ax2) = plt.subplots(2,1)
fig.subplots_adjust(hspace=0.1)

ax1.plot(x,sal, label = '살인', color = 'red')
ax1.plot(x,sung, label = '성폭력', color = 'orange')
ax1.plot(x,ma, label = '마약', color = 'blue')

ax2.plot(x,sal, label = '살인', color = 'red')
ax2.plot(x,sung, label = '성폭력', color = 'orange')
ax2.plot(x,ma, label = '마약', color = 'blue')


ax1.set_ylim(3000,6000)
ax2.set_ylim(0,800)

ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.xaxis.tick_top()
# ax1.xaxis.tick_bottom()

kwargs = dict(marker=[(-1, -0.5), (1, 0.5)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)
# ax1.tick_params(labeltop=False)
# plt.xlabel('Day')
# plt.ylabel('Count')
# plt.title('요일별 범죄 건수')
# plt.plot(sal, label = '살인', color = 'red')
# plt.plot(sung, label = '성폭력', color = 'orange')
# plt.plot(ma, label = '마약', color = 'blue')
plt.xticks(x,day)
plt.legend()
plt.show()
