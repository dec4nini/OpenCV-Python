#Importação das bibliotecas
import cv2
from matplotlib import pyplot as plt

#Carregamento da imagem
img = cv2.imread("Exemplo.jpg")

#Exibindo a imagem
plt.imshow(img)
plt.show()

#Histograma (a função ravel recebe a matriz da imagem (img) e retorna uma matriz 1D)
plt.hist(img.ravel(), 256, [0,256])
plt.show()
