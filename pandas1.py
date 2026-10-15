import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],   
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
print(df)
pd.Series([1, 2, 3, 4, 5])
print(df.describe())