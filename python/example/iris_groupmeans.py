
import pandas as pd

iris = pd.read_csv('python/example/iris.csv')
iris_group = iris.groupby('Species').mean()
iris_group.to_csv('iris_group.csv')