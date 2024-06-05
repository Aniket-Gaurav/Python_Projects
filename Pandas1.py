import pandas as pd

data = {
    'Product' : ['A','B','C','D'],
    'Sales' : [150,200,600,900],
    'Profit' : [50,70,100,130]
}

df = pd.DataFrame(data)
print(df)
print(df['Sales'])

high_sales = df[df['Sales']>200]

print(high_sales)

df['Revenue'] = df['Sales'] * df['Profit']
print(df)

df = df.drop('Revenue', axis=1)
print(df)

grouped = df.groupby('Product').sum()
print(grouped)

pivot = df.pivot_table(values='Sales', index='Product', aggfunc='sum')
print(pivot)
