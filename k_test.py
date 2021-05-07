from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.datasets import load_iris

# 导入IRIS数据集
iris = load_iris()
iris.data  # 查看数据
model1 = SelectKBest(chi2, k=2)#选择k个最佳特征
model1.fit_transform(iris.data, iris.target)#iris.data是特征数据，iris.target是标签数据，该函数可以选择出k个特征
print(model1.scores_) #得分
print(model1.pvalues_)  #p-values