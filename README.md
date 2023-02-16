# Criminal_Analysis



<hr></hr>

``` python
import csv
f = open(r"C:\Users\a22\Downloads\범죄발생_요일_2019.csv",encoding='euc-kr')
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
# ax1.xaxis.tick_top()
ax1.get_xaxis().set_visible(False) 
# ax1.xaxis.tick_bottom())


kwargs = dict(marker=[(-1, -0.5), (1, 0.5)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)
ax1.tick_params(labeltop=False)
# plt.xlabel('Day')
# plt.ylabel('Count')
# plt.title('요일별 범죄 건수')
# plt.plot(sal, label = '살인', color = 'red')
# plt.plot(sung, label = '성폭력', color = 'orange')
# plt.plot(ma, label = '마약', color = 'blue')
plt.xticks(x,day)
plt.legend()
plt.show()
```

![요일별](https://user-images.githubusercontent.com/113042318/219282384-24e0ced7-8a65-419e-9b70-f591dd3ac111.png)





직업별
``` python
import csv
f = open("C:\\Users\\a13\\Desktop\\web\\day33\\범죄자_직업_2019.csv",encoding='euc-kr')
data = csv.reader(f)
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
font_path = "C:\Windows\Fonts\H2GTRM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc("font", family = font)
crime = ['살인','성폭행','마약']
job = []
results = np.array([[3,0,12,2,2,28,1,1,0,58,1,3,12,66,54,1,0,2,5,0,5,13,4,0,16,13,0,1,395,244],
                    [75,72,280,84,103,727,166,105,8,5525,39,90,288,904,1982,149,14,54,118,23,124,869,420,4,4633,49,14,83,6961,5249],
                    [2,1,9,2,12,25,6,6,0,228,1,18,15,84,136,44,0,3,7,1,48,82,2,4,143,89,1,6,1150,614]])
for i in data:
    if '범죄분류' in i[0]:
        for x in i[1:]:
            job.append(x)
        print(job)
fig, ax = plt.subplots()
im = ax.imshow(results)
ax.set_xticks(np.arange(len(job)))
ax.set_xticklabels(job)
ax.set_yticks(np.arange(len(crime)))
ax.set_yticklabels(crime)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
for i in range(len(crime)):
    for j in range(len(job)):
        text = ax.text(j, i, results[i, j],
                       ha="center", va="center", color="w")
ax.set_title("범죄자 직업")
fig.tight_layout()
plt.show()


```

![직업별](https://user-images.githubusercontent.com/113042318/219282989-7bb4a09b-6820-4d2a-abcc-69499d2bc0b1.png)




``` python
import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib import font_manager, rc
font_path = "C:\Windows\Fonts\H2GTRM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc("font", family = font)
with open(r"C:\Users\a14\Downloads\범죄자_교육정도_2019(1).csv",encoding="cp949") as f:
    data = csv.reader(f)
    a = []
    sort_edu = []
    for i in data:
        # print(i)
        a.append(i)
    for i in range(len(a[0])):
        sort_edu.append(a[0][i])
# i[1] i[16]부터
# print(type(data))
kill = a[1][:]
kill1 = []
assult = a[2][:]
assult1 = []
drug = a[4][:]
drug1 = []
sort_edu.remove("범죄분류")
assult.remove("성폭력")
kill.remove("살인")
drug.remove("마약류관리에관한법률(마약)")
for i in kill:
    kill1.append(int(i))
for i in assult:
    assult1.append(int(i))
for i in drug:
    drug1.append(int(i))
# print(drug)
# print(kill)
# print(drug)
# print(sort_edu)
# print(a)
print(type(kill))
# y = [a[1][0],a[2][0],a[5][0]]
# count = [kill]
x = np.arange(0,19,1)
# print(count)
# print(len(kill))
# print(sort_edu)
fig, (ax1, ax2) = plt.subplots(2,1, sharex=True)
fig.subplots_adjust(hspace=0.05)
# ax1.plot(x,kill1,label="살인")
ax1.plot(x,assult1,c ="red", label="성폭행")
# ax1.plot(x,drug1, label="마약")

ax2.plot(x,kill1,label="살인")
# ax2.plot(x,assult1,label="성폭행")
ax2.plot(x,drug1, label="마약")

# ax1.set_ylim(700, 10000)
# ax2.set_ylim(0, 500)

# ax1.spines["bottom"].set_visible(False)
# ax2.spines["top"].set_visible(False)
# ax1.xaxis.tick_top()
# ax1.tick_params(labeltop=False)
# ax2.xaxis.tick_bottom()

# kwargs = dict(marker=[(-1, -0.5), (1, 0.5)], markersize=12,
#               linestyle="none", color='k', mec='k', mew=1, clip_on=False)
# ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
# ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# ax1.xticks(x, sort_edu, rotation=45)

# plt.plot(x,kill1,label="살인")
# plt.plot(x,assult1,label="성폭행")
# plt.plot(x,drug1, label="마약")
plt.xticks(x, sort_edu, rotation=90)
ax1.legend()
plt.legend()
plt.show()

```
![학력별](https://user-images.githubusercontent.com/113042318/219283606-21e351b4-038e-41d4-97e4-6e65fde68a91.PNG)
