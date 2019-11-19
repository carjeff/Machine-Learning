import pandas as pd

print("---初始数据集---\n")
data=pd.DataFrame([
    ['red','class1','yi',0.233333],
    ['green','class2','er',0.654321],
    ['blue','class1','san',0.123456]])
data.columns=['color','class','id','value']
print(data)

print("---映射后数据集---\n")
mapp1={
    'yi':11,
    'er':22,
    'san':33}
data['id']=data['id'].map(mapp1)
mapp2={label:idx for idx,label in enumerate(set(data['class']))}
data['class']=data['class'].map(mapp2)
print(data)

print("---「one-hot」后数据集---\n")
data=pd.get_dummies(data)

print(data)
