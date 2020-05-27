import pandas as pd
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import dendrogram
from matplotlib import pyplot
from sklearn.cluster import k_means
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from sklearn.cluster import dbscan
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics import adjusted_rand_score
from sklearn.metrics import mutual_info_score
from sklearn.metrics import normalized_mutual_info_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import jaccard_similarity_score

################LIMPEZA DATASET###################

#BIOLOGIA
df = pd.read_csv('baseGeral.csv',encoding = "UTF-8", sep = ";", usecols=[0,2,46,47,48,49,50,
51,53,54,55,56,58,59,0,2,12,15,28,29,36,44])



#ADMINISTRAÇAO
#metade do curso e gera o agrupamento e a tabela e depois a outra metade com todas as disciplinas
'''
#primeiros semestres
df = pd.read_csv('baseGeral.csv',encoding = "UTF-8", sep = ";", usecols=[0,2,46,47,48,49,50,
51,53,54,55,56,58,59])
df2 = df[df['Curso'] == 'Administracao']
selecao = (df2.Período == 1) | (df2.Período == 2) | (df2.Período == 3) | (df2.Período == 4)
df3 = df2[selecao]
df4 = df3.drop(columns=['Curso','Período'])
dados = df4.values

#ultimos semestres

df = pd.read_csv('baseGeral.csv',encoding = "UTF-8", sep = ";", usecols=[0,2,46,47,48,49,50,
51,53,54,55,56,58,59])
df2 = df[df['Curso'] == 'Administracao']
selecao = (df2.Período == 5) | (df2.Período == 6) | (df2.Período == 7) | (df2.Período == 8)
df3 = df2[selecao]
df4 = df3.drop(columns=['Curso','Período'])
dados = df4.values

#merge do dataframe
dfnovo = pd.read_csv('baseGeral.csv',encoding = "UTF-8", sep = ";", usecols=[0,2,12,15,28,29,36,44])
dfnv2 = dfnovo[dfnovo['Curso'] == 'Administracao']
selecaonv = (dfnv2.Período == 5) | (dfnv2.Período == 6) | (dfnv2.Período == 7) | (dfnv2.Período == 8)
dfnv3 = dfnv2[selecaonv]



#############HIERARQUICO############################
#h = linkage(dados, method='average', metric='chebyshev')
#h = linkage(dados, method='complete', metric='chebyshev')
#h = linkage(dados, method='single', metric='chebyshev')
#h = linkage(dados, method='average', metric='euclidean')
h = linkage(dados, method='complete', metric='euclidean')
#h = linkage(dados, method='single', metric='euclidean')

dendrogram(h)
pyplot.show()
rotulos_dist = fcluster(h, t=15, criterion='distance')
rotulos_k = fcluster(h, t=2, criterion='maxclust')

lh1 =[]
lh2 =[]
lh3=[]
lh4=[]
lh5=[]
lh6=[]
lh0=[]
for i in rotulos_k:
    if str(i) == "0":
        lh0.append(i)
    if str(i) == "1":
        lh1.append(i)
    if str(i) == "2":
        lh2.append(i)
    if str(i) == "3":
        lh3.append(i)
    if str(i) == "4":
        lh4.append(i)
    if str(i) == "5":
        lh5.append(i)
    if str(i) == "6":
        lh6.append(i)

print("Quantidade de pessoas por grupos no Hierarquico")
print(len(lh1), "No 1 grupo")
print(len(lh2), "No 2 grupo")
print(len(lh3), "No 3 grupo")
print(len(lh4), "No 4 grupo")
#print(len(lh5), "No 5 grupo")
#print(len(lh6), "No 6 grupo")
#print("\n")


###############KMEANS###########################
centroides, rotulosk, sse = k_means(dados,n_clusters=2,init='random',n_init=100)
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
X = dados
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
#df4.insert(loc=12,column = "Grupo", value = rotulosk)
#criar csv
#merge csv
#res = pd.concat([df4, dfnv3], sort = False)
#res = res.drop(['k'], axis = 1)




####################ANALISE DE SILHUETA########################
s = silhouette_score(dados, rotulos, metric='sqeuclidean')
print(s, "silhueta score")


######################DBSCAN#######################

import numpy as np
from sklearn.datasets.samples_generator import make_blobs
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import DBSCAN
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt1

neigh = NearestNeighbors(n_neighbors=2)
nbrs = neigh.fit(dados)
distances, indices = nbrs.kneighbors(dados)
distances = np.sort(distances, axis=0)
distances = distances[:,1]
plt.plot(distances)
plt.show()
m = DBSCAN(eps=3, min_samples=12)
m.fit(dados)
clusters = m.labels_
cores = ['royalblue', 'maroon', 'forestgreen', 'mediumorchid', 'tan', 'deeppink', 'olive'] 
vetorizador = np.vectorize (lambda x: cores [x% len (cores)])
plt1.scatter (dados [:, 0], dados [:, 1], c = vetorizador (clusters))
plt1.show()
l1 =[]
l2 =[]
ln1 =[]
l3 = []
l0=[]
l4 = []
for i in clusters:
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
    if str(i) == "-1":
        ln1.append(i)
        
print("Quantidade de pessoas por grupos no DBSCAN")
print(len(l0), "No 0 grupo")
print(len(l1), "No 1 grupo")
print(len(l2), "No 2 grupo")
print(len(ln1), "No -1 grupo ")
print(len(l3), "No 3 grupo")
print(len(l4), "No 4 grupo")


##################INDICE RAND######################
#Indice rand do hierarquico e nao hierarquico
ir = adjusted_rand_score(rotulos_k, rotulosk)
print(ir)

# Calculando o IMN.
imn = normalized_mutual_info_score(rotulos_k, rotulosk)
print(imn)

jaccard_similarity_score(rotulos_k, rotulosk)
print(jaccard_similarity_score)
'''
