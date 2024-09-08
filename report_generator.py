import pandas as pd
import matplotlib.pyplot as plt

from db import execute_query
from queries import sales_report_query



def generate_sales_report(start_date, end_date):
    query = sales_report_query(start_date, end_date)
    sales_data = execute_query(query)

    print("Отчет по продажам:")
    print(sales_data.head())

    visualize_sales(sales_data)



def visualize_sales(df):
    plt.figure(figsize=(10, 6))
    df.groupby('product_name')['total_sales'].sum().plot(kind='bar')
    plt.title('Общие продажи по продуктам')
    plt.xlabel('Продукт')
    plt.ylabel('Сумма продаж')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()