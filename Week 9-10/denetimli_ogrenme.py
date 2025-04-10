from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


iris = load_iris()

x = iris.data
y = iris.target

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

tree_model = DecisionTreeClassifier()
tree_model.fit(x_train,y_train)
tree_pred = tree_model.predict(x_test)

print("Karar Ağacı Doğruluğu:", accuracy_score(y_test,tree_pred))

forest_model = RandomForestClassifier()
forest_model.fit(x_train,y_train)
forest_pred = forest_model.predict(x_test)

print("Random Forest Doğruluğu:",accuracy_score(y_test,forest_pred))

svm_model = SVC()
svm_model.fit(x_train,y_train)
svm_pred = svm_model.predict(x_test)

print("SVM Doğruluğu:",accuracy_score(y_test,svm_pred))


new_flower = np.array([[5.1,3.5,1.4,0.2]])

predict_tree = tree_model.predict(new_flower)
print("Karar Ağacı Tahmini:",iris.target_names[predict_tree[0]])

predict_forest = forest_model.predict(new_flower)
print("Random Forest Tahmini:", iris.target_names[predict_forest[0]])

predict_svm = svm_model.predict(new_flower)
print("SVM Tahmini:", iris.target_names[predict_svm[0]])

X_petal = x[:, [2,3]]

for label, color, species in zip([0,1,2],['red','green','blue'], iris.target_names[0]):
    plt.scatter(X_petal[y == label, 0],
                X_petal[y == label, 1],
                c=color, label=species)

plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Iris Turlerinin Petal Uzunlugu ve Genisligi")
plt.legend()
plt.grid(True)
plt.show()

y_pred = tree_model.predict(x_test)

cm = confusion_matrix(y_test,y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
disp.plot(cmap=plt.cm.Blues)
plt.title("Karar Agac - Confusion Matrix")
plt.show()