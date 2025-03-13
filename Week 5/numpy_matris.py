import numpy as np

matris = np.random.randint(1,10,(2,3))
print("Matris:\n",matris)

transpoz = matris.T
print("transpoz:\n",transpoz)

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
carpim = np.dot(A,B)
print("Matris Çarpımı:\n",carpim)

ters = np.linalg.inv(A)
print("Matrisin Tersi:\n", ters)
