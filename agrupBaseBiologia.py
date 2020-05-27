import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import k_means

df = pd.read_csv('baseGeral.csv',encoding = "UTF-8", sep = ";", usecols=[0,2,46,48,49,
51,53,54,55,56,58,59,12,15,28,29,36,44])
df2 = df[df['Curso'] == 'Biologia']
pt1 = (df2.Período == 1) | (df2.Período == 2) | (df2.Período == 3) | (df2.Período == 4)
dfpt1 = df2[pt1]
df3 = dfpt1.drop(columns=['Curso','Período'])
dadospt1 = df3.values

#saber quantidade por periodo
#df['Período'].value_counts()
#saber o periodo maximo
#df2['Período'].max()




print("DADOS PARTE 1")
print("\n")
###############KMEANS###########################
centroides, rotulosk, sse = k_means(dadospt1,n_clusters=3,init='random',n_init=100)
l1 =[]
l2 =[]
l3=[]
l4=[]
l5=[]
l6=[]
l0=[]
for i in rotulosk:
    if str(i) == "0":
        l0.append(i)
    if str(i) == "1":
        l1.append(i)
    if str(i) == "2":
        l2.append(i)
    if str(i) == "3":
        l3.append(i)
    if str(i) == "4":
        l4.append(i)
    if str(i) == "5":
        l5.append(i)
    if str(i) == "6":
        l6.append(i)
print("Quantidade de pessoas por grupos no K-Means")
print(len(l0), "No 1 grupo")
print(len(l1), "No 2 grupo")
print(len(l2), "No 3 grupo")
print(len(l3), "No 4 grupo")
#print(len(l4), "No 5 grupo")
#print(len(l5), "No 6 grupo \n")



###########################Elbow#######################
print("\n Metódo do cotovelo")
from sklearn.cluster import KMeans
X = dadospt1
wcss = []
 
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'random')
    kmeans.fit(X)
    print ((i,kmeans.inertia_))
    wcss.append(kmeans.inertia_)  
plt.plot(range(1, 11), wcss)
plt.title('O Metodo Elbow')
plt.xlabel('Numero de Clusters')
plt.ylabel('WSS') #within cluster sum of squares
plt.show()
print("\n")

#nova coluna "Grupos"
df3.insert(loc=16,column = "Grupo", value = rotulosk)
#criar csv
df3.to_csv(r'\Users\Pamella\Desktop\PIC 2019\K-Means\agrupamento1ptBiologia.csv', index=False)

###################################################################################

print("DADOS PARTE 2")
print("\n")
pt2 =(df2.Período == 5) | (df2.Período == 6) | (df2.Período == 7) | (df2.Período == 8)
dfpt2 = df2[pt2]
df4 = dfpt2.drop(columns=['Curso','Período'])
dadospt2 = df4.values


###############KMEANS###########################
centroides, rotulosk2, sse = k_means(dadospt2,n_clusters=4,init='random',n_init=100)
l1 =[]
l2 =[]
l3=[]
l4=[]
l5=[]
l6=[]
l0=[]
for i in rotulosk2:
    if str(i) == "0":
        l0.append(i)
    if str(i) == "1":
        l1.append(i)
    if str(i) == "2":
        l2.append(i)
    if str(i) == "3":
        l3.append(i)
    if str(i) == "4":
        l4.append(i)
    if str(i) == "5":
        l5.append(i)
    if str(i) == "6":
        l6.append(i)
print("Quantidade de pessoas por grupos no K-Means")
print(len(l0), "No 1 grupo")
print(len(l1), "No 2 grupo")
print(len(l2), "No 3 grupo")
print(len(l3), "No 4 grupo")
#print(len(l4), "No 5 grupo")
#print(len(l5), "No 6 grupo \n")



###########################Elbow#######################
print("\n Metódo do cotovelo")
from sklearn.cluster import KMeans
X = dadospt2
wcss = []
 
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'random')
    kmeans.fit(X)
    print ((i,kmeans.inertia_))
    wcss.append(kmeans.inertia_)  
plt.plot(range(1, 11), wcss)
plt.title('O Metodo Elbow')
plt.xlabel('Numero de Clusters')
plt.ylabel('WSS') #within cluster sum of squares
plt.show()
print("\n")

#nova coluna "Grupos"
df4.insert(loc=16,column = "Grupo", value = rotulosk2)
#criar csv
df4.to_csv(r'\Users\Pamella\Desktop\PIC 2019\K-Means\agrupamento2ptBiologia.csv', index=False)

