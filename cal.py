'''create with virtual environment so installed below libraries in terminal. consider to install libraries 
before run the code''''


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

file_path = 'Adidas US Sales Datasets.xlsx'
worksheet = 'Adidas US Sales Datasets'
df = pd.read_excel(
    'Adidas US Sales Datasets.xlsx', skiprows=4, usecols="B:N")

df = df.iloc[:9658]


df.columns = ['Retailer', 'Retailer ID', 'Invoice Date',	'Region', 'State', 'City', 'Product',
              '	Price per Unit', 'Units Sold', 'Total Sales', 'Operating Profit', '	Operating Margin', 'Sales Method']
df['Invoice Date'] = pd.to_datetime(df['Invoice Date'])

df_pro_jan = df[(df['Invoice Date'] >= '2020-01-01') &
                (df['Invoice Date'] <= '2020-01-31')]

total_sales_jan = df_pro_jan['Total Sales'].sum()
print("January total income of adidas is", total_sales_jan)


df_pro_feb = df[(df['Invoice Date'] >= '2020-02-01') &
                (df['Invoice Date'] <= '2020-02-29')]

total_sales_feb = df_pro_feb['Total Sales'].sum()
print("February total income of adidas is", total_sales_feb)

df_pro_mar = df[(df['Invoice Date'] >= '2020-03-01') &
                (df['Invoice Date'] <= '2020-03-31')]

total_sales_mar = df_pro_mar['Total Sales'].sum()
print("March total income of adidas is", total_sales_mar)

df_pro_apr = df[(df['Invoice Date'] >= '2020-04-01') &
                (df['Invoice Date'] <= '2020-04-30')]

total_sales_apr = df_pro_apr['Total Sales'].sum()
print("April total income of adidas is", total_sales_apr)

df_pro_may = df[(df['Invoice Date'] >= '2020-05-01') &
                (df['Invoice Date'] <= '2020-05-31')]

total_sales_may = df_pro_may['Total Sales'].sum()
print("May total income of adidas is", total_sales_may)


df_pro_june = df[(df['Invoice Date'] >= '2020-06-01') &
                 (df['Invoice Date'] <= '2020-06-30')]

total_sales_june = df_pro_june['Total Sales'].sum()
print("June total income of adidas is", total_sales_june)

df_pro_july = df[(df['Invoice Date'] >= '2020-07-01') &
                 (df['Invoice Date'] <= '2020-07-31')]

total_sales_july = df_pro_july['Total Sales'].sum()
print("July total income of adidas is", total_sales_july)

df_pro_aug = df[(df['Invoice Date'] >= '2020-08-01') &
                (df['Invoice Date'] <= '2020-08-31')]

total_sales_aug = df_pro_aug['Total Sales'].sum()
print("August total income of adidas is", total_sales_aug)

df_pro_sep = df[(df['Invoice Date'] >= '2020-09-01') &
                (df['Invoice Date'] <= '2020-09-30')]

total_sales_sep = df_pro_sep['Total Sales'].sum()
print("September total income of adidas is", total_sales_sep)

df_pro_oct = df[(df['Invoice Date'] >= '2020-10-01') &
                (df['Invoice Date'] <= '2020-10-31')]

total_sales_oct = df_pro_oct['Total Sales'].sum()
print("Octomber total income of adidas is", total_sales_oct)

df_pro_nov = df[(df['Invoice Date'] >= '2020-11-01') &
                (df['Invoice Date'] <= '2020-11-30')]

total_sales_nov = df_pro_nov['Total Sales'].sum()
print("November total income of adidas is", total_sales_nov)

df_pro_dec = df[(df['Invoice Date'] >= '2020-12-01') &
                (df['Invoice Date'] <= '2020-12-31')]

total_sales_dec = df_pro_dec['Total Sales'].sum()
print("December total income of adidas is", total_sales_dec)


months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'octomber', 'November', 'December']
total_sales = [total_sales_jan, total_sales_feb, total_sales_mar, total_sales_apr, total_sales_may, total_sales_june,
               total_sales_july, total_sales_aug, total_sales_sep, total_sales_oct, total_sales_nov, total_sales_dec]

df_monthly_sale = pd.DataFrame({'Month': months, 'sales': total_sales})

plt.figure(figsize=(12, 12))
plt.plot(df_monthly_sale['Month'], df_monthly_sale['sales'], marker='o')

plt.xlabel('Month')
plt.ylabel('sales')
plt.title('Monthly behave of income in 2020')

plt.grid(True)

plt.show()
