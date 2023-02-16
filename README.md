# Criminal_Analysis


``` python
import csv 
a = [[],[],[],[],[],[],[]] #보라색 7개 - 요일, 1개당 24시간

with open(r"C:\Users\a22\Desktop\Python\passby_data.CSV", 'r', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    j = 0
    i = 0
    for row in reader:
        a[i].append(row)
        # print("\n\n==================================",a)
        j=j+1
        if(j % 24 == 0):
            i=i+1
            # print("\n------요일바뀜------\n", a[i])

# 시간대별 주간 평균값 구하기
avgh, avghw, avghy = [], [], []

for j in range(0,24):
    day_sum = 0
    day_wsum = 0
    day_ysum = 0

    for i in range(0,7):
        day_sum = day_sum + int(a[i][j]['num']) # i번째 요일에 j번째 시간대 행인수
        day_wsum = day_wsum + int(a[i][j]['wnum']) # i번째 요일에 j번째 시간대 여성수
        day_ysum = day_ysum + int(a[i][j]['ynum']) # i번째 요일에 j번째 시간대 30대 행인 수

    avgh.append(day_sum/7) #j번째 시간대 주간 행인수 평균
    avghw.append(day_wsum/7) #j번째 시간대 주간 여성 행인 수 평균
    avghy.append(day_ysum/7) #j번째 시간대 주간 30대 행인 수 평균

# 시간대별 평균 유동인구 출력하기
day_title = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']
hour_title = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']

import matplotlib.pyplot as plt

plt.title("Hourly passerby data")
plt.xlabel("Hour")
plt.ylabel("Number of passerby")

plt.plot(hour_title, avghw, c="green", label = "Woman")
plt.plot(hour_title, avghy, c="red", label = "Young")
plt.plot(hour_title, avgh, label = "Hourly")
plt.scatter(hour_title, avgh)
plt.legend()
plt.show()
```
