import pandas
def calculate(col):
    count = col.shape[0]
    cardinality = col.nunique()
    counts = col.value_counts()
    try:
        miss_value = counts[0]
    except:
        miss_value = 0
    mean_value = col.mean()
    col.replace(0,mean_value, inplace=True)
    min_value =col.min()
    max_value = col.max()
    standard = col.std()
    first_quartile = col.quantile(0.25)
    median = col.median()
    third_quartile = col.quantile(0.75)

    result = [count, cardinality, miss_value, min_value, max_value, mean_value, standard, first_quartile, median
              , third_quartile]

    return result


def main():
    data = load_data()
    first_result = pandas.DataFrame(columns=['Count', 'Cardinality', 'Missing Values', 'Min Values', 'Max Values', 'Mean',
                                             'Standard Deviation', 'First Quartile Value', 'Median'])
    features = data.columns.tolist()
    for feature in features:
        col = data[feature]
        result = calculate(col)
        final_result.loc[feature] = result
    draw_picture(data)
    pandas.set_option('display.max_columns', 10)
    print(final_result)