from MyConvexHull import myConvexHull
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

print("Pilih dataset: ")
print("1. Iris")
print("2. Breast Cancer")
print("3. Wine")
a = int(input("Masukkan nomor data: "))
if(a==1):
  data = datasets.load_iris()
elif(a==2):
  data = datasets.load_breast_cancer()
elif (a==3):
  data=datasets.load_wine()

#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
print(df.shape)

#figuring
plt.figure(figsize = (10, 6))
colors = ['b','r','g']

#choose feature
for i in range(0,len(data.feature_names)//2+1,2):
  print(i//2+1,"{} vs {}".format(data.feature_names[i],data.feature_names[i+1]))
n=int(input("Masukkan nomor data yang mau dianalisis: "))

#make plot
n=2*(n-1)
plt.title('{} vs {}'.format(data.feature_names[n],data.feature_names[n+1]));
plt.xlabel(data.feature_names[n])
plt.ylabel(data.feature_names[n+1])
for i in range(len(data.target_names)):
  bucket = df[df['Target'] == i]
  bucket = bucket.iloc[:,[n,n+1]].values
  hull = myConvexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
  plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
  for j in range (len(hull.ver)):
    plt.plot([hull.ver[j][0],hull.ver[(j+1)%len(hull.ver)][0]] , [hull.ver[j][1],hull.ver[(j+1)%len(hull.ver)][1]] ,c =colors[i])
plt.legend()
plt.show()