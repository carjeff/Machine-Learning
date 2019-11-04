import pandas as pd
import numpy as np
import math
import pprint
from learning_lib import train_test_split

pp = pprint.PrettyPrinter(indent=4)

def load_data():
    # Only include the first 8 descriptive features and the target label
    data = pd.read_csv("heart.csv", usecols=[
                       "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "target"])
    return data



def create_thresholds(dataset, names, nstds=3):
    # Assume the data is normally-distributed
    thresholds = {}
    print(dataset.columns)
    for feature in names:
        if feature in dataset.columns:
            col = dataset[feature]
            mint, maxt = np.min(col), np.max(col)
            mean, stddev = np.mean(col), np.std(col)
            ts = [mint]
            for n in range(-nstds - 1, nstds):
                t = round(n * stddev + mean)
                if t >= mint and t <= maxt:
                    ts.append(t)
            thresholds[feature] = ts
    return thresholds

def entropy(dataset):
    counts = dataset["target"].value_counts()
    """
        Similar to doing the following manually:
            counts = {}
            for val in data["target"]:
                counts[val] = counts.get(val, 0) + 1
    """
    total = dataset["target"].shape[0]
    sum = 0.
    for count in counts:
        p = count/total
        sum += p * math.log(p)
    return - sum


def best_splite(dataset,thresholds):
    best_info_gain = 0.0
    best_label = None
    
    #不包括最后一个target 的 feature
    labels = list(dataset.columns)[:-1]
    #print(labels)
    #靶特性的熵
    init_entropy = entropy(dataset)

    #对于连续特性切割值
    def partition(feature,dataset,thresholds):
        def find_threshold(feature, val,thresholds):
        # Guaranteed to find a threshold somewhere between min and max
            for t in reversed(thresholds[feature]):
                if val >= t:
                    return t
            print(feature, val,"wrong")
            print(thresholds[feature])
            #raise Exception("Unexpected return without threshold")
            
        features = dataset.columns
        ps = {}
        #print(data[feature])
        for j, val in enumerate(dataset[feature]):
            #print(feature,val)
            # Treat categorical and continuous feature values differently
            val = find_threshold(feature, val,thresholds)
            p = ps.get(val, pd.DataFrame(columns=features))
            ps[val] = p.append(dataset.loc[j, features])
        return ps

    for _, label in enumerate(dataset.columns):
        label_entropy = 0.0
        if label in thresholds:
            levels = partition(label, dataset,thresholds)
            for level in levels.values():
                prob = level.shape[0] / dataset.shape[0]
                label_entropy += prob * entropy(level)
        else:
            levels = dataset[label].unique().tolist()
            for level in levels:
                level_data = dataset[dataset[label] == level]
                #竟然可以这样用
                prob = level_data.shape[0] / dataset.shape[0]
                label_entropy+=prob*entropy(level_data)
        info_gain = init_entropy - label_entropy

        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_label = label
                 
    return best_label
    
def splite_dataset(dataset, column, level, thresholds):
    if column in thresholds:
        subdata = dataset[dataset[column] >= level]
        del subdata[column]
        return subdata.reset_index(drop=True)
    else:
        subdata = dataset[dataset[column] == level]
        del subdata[column]
        return subdata.reset_index(drop=True)

def top_amount_level(target_list):
    class_count = target_list.value_counts().to_dict()  # 计算靶标签的不同水平的样本量，并转化为字典
    # 字典的items方法可以将键值对转成[(), (), ...]，可以使用列表方法
    sorted_class_count = sorted(class_count.items(), key=lambda x:x[1], reverse=True)
    return sorted_class_count[0][0]

def creat_tree(dataset):

    #终止条件
    #print("in")
    #拆出来最后一列的值
    TargetList = dataset.iloc[:, -1]
    #print(TargetList)
    
    #print(TargetList.unique())
    #程序终止条件1 靶标签在该数据集上只有一个水平，返回该标签
    if TargetList.unique().shape[0] <= 1:
        return TargetList[0]
    #程序终止条件2 数据集只剩下靶标签这一列数据，返回数量最多的水平
    if dataset.shape[1] == 1:
        return top_amount_level(TargetList)
    
    thresholds = create_thresholds(
    dataset, ["age", "chol", "trestbps", "thalach"], nstds=3)
    print(thresholds)
    
    #the best feature
 

    BestFeature = best_splite(dataset, thresholds)
    print(BestFeature)
    if BestFeature in thresholds:
        BestFeatureLevels = thresholds[BestFeature]
    else:
        BestFeatureLevels = dataset[BestFeature].unique().tolist()
    print(BestFeatureLevels)
 
    #这一层准备生成的字典
    tree = {BestFeature: {}}
    
    for level in reversed (BestFeatureLevels):
        LevelSubdataset = splite_dataset(dataset, BestFeature, level, thresholds)
        dataset = dataset[dataset[BestFeature] < level]
        print("///////////////////////")
        print(LevelSubdataset)
        print("************************")
        tree[BestFeature][level] = creat_tree(LevelSubdataset)
    
    return tree
    
    


def main():
    data=load_data()
    train_data, test_data = train_test_split(data, test_size=0.25)
    train_data.drop(columns="index",inplace=True)
    #print(data)
    #print(train_data)
    tree={}    
    creat_tree(train_data)
    #print(tree)


if __name__ == "__main__":
    main()
    

    

