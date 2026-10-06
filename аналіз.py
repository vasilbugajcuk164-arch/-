import pandas as pd
import matplotlib.pyplot as plt



# Завантаження датасету
data = pd.read_excel("Online Retail.xlsx")
def info(data):
    # Перші 10 рядків
    print(data.head(10))

    # Розмір датасету
    print("\nРозмір датасету:")
    print(data.shape)

    # Назви стовпців
    print("\nСтовпці:")
    print(data.columns.tolist())

    # Типи даних
    print("\nТипи даних:")
    print(data.dtypes)

    # Кількість пропущених значень
    print("\nПропущені значення:")
    print(data.isnull().sum())

#очищення даних
def clean_data(data):
    data = data.dropna(subset=['CustomerID'])  # Видалення рядків з пропущеними CustomerID
    #Description
    data = data.drop_duplicates()  # Видалення дублікатів
    #Quantity <= 0
    data = data[data['Quantity'] > 0]  # Видалення рядків з Quantity <= 0
    #UnitPrice <= 0
    data = data[data['UnitPrice'] > 0]  # Видалення рядків з UnitPrice <= 0
    data = data.dropna(subset=['Description'])  # Видалення рядків з пропущеними Description
    print("\nКількість рядків після очищення даних:")
    print(data.shape[0])
    return data

def Creating_new_metrics(data):
    # Revenue = Quantity * UnitPrice
    data['Revenue'] = data['Quantity'] * data['UnitPrice']
    # Додатково з дати
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
    data['Year'] = data['InvoiceDate'].dt.year
    data['Month'] = data['InvoiceDate'].dt.month
    data['Day'] = data['InvoiceDate'].dt.day
    data['Hour'] = data['InvoiceDate'].dt.hour


def statistics(data):
    print("Скільки всього продано товарів (Quantity):", data['Quantity'].sum())
    print("Скільки всього зароблено (Revenue):", data['Revenue'].sum())
    print("Середня ціна товару (UnitPrice):", data['UnitPrice'].mean())
    print("Hайдорожчий товар (UnitPrice):", data['UnitPrice'].max())
    print("Hайдешевший товар (UnitPrice):", data['UnitPrice'].min())
    print("Було замовлень (InvoiceNo):", data['InvoiceNo'].nunique())
    print("Скільки країн представлено в датасеті (Country):", data['Country'].nunique())

def analysis(data):
    # Топ 10 країн за кількістю замовлень
    top_countries = data['Country'].value_counts().head(10)
    print("\nТоп 10 країн за кількістю замовлень:")
    print(top_countries)

    # Топ 10 товарів за кількістю продажів
    top_products = data.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
    print("\nТоп 10 товарів за кількістю продажів:")
    print(top_products)

    # Топ 10 клієнтів за витратами
    top_customers = data.groupby('CustomerID')['Revenue'].sum().sort_values(ascending=False).head(10)
    print("\nТоп 10 клієнтів за витратами:")
    print(top_customers)

   #Аналіз продажів у часі
    print("\nАналіз продажів у часі:")
    print("місяць з найбільшими продажами:", data.groupby('Month')['Revenue'].sum().idxmax())
    print("місяць з найменшими продажами:", data.groupby('Month')['Revenue'].sum().idxmin())
    print("кількість проданих товарів по місяцях:")
    print(data.groupby('Month')['Quantity'].sum())

    print("\nАналіз продажів по годинах:")
    print("година з найбільшими продажами:", data.groupby('Hour')['Revenue'].sum().idxmax())

def visualization(data):
    """1. Продажі по місяцях
    📈 Line chart
    2. ТОП-10 товарів
    📊 Bar chart
    3. ТОП-10 країн
    📊 Bar chart
    4. Виручка по місяцях
    📈 Line chart
    5. Розподіл цін
    📊 Histogram
    6. Продажі по годинах
    📊 Bar chart"""
    plt.figure(figsize=(12, 6))
    print("1. Продажі по місяцях")
    data.groupby('Month')['Revenue'].sum().plot(kind='line', marker='o')
    plt.title('Продажі по місяцях')
    plt.xlabel('Місяць')
    plt.ylabel('Виручка')
    plt.grid()
    plt.show()

    print("2. ТОП-10 товарів")
    top_products = data.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
    top_products.plot(kind='bar')
    plt.title('ТОП-10 товарів за кількістю продажів')
    plt.xlabel('Товар')
    plt.ylabel('Кількість продажів')
    plt.xticks(rotation=45, ha='right')
    plt.show()

    print("3. ТОП-10 країн")
    top_countries = data['Country'].value_counts().head(10)
    top_countries.plot(kind='bar')
    plt.title('ТОП-10 країн за кількістю замовлень')
    plt.xlabel('Країна')
    plt.ylabel('Кількість замовлень')
    plt.xticks(rotation=45, ha='right')
    plt.show()

    print("4. Виручка по місяцях")
    data.groupby('Month')['Revenue'].sum().plot(kind='line', marker='o')
    plt.title('Виручка по місяцях')
    plt.xlabel('Місяць')
    plt.ylabel('Виручка')
    plt.grid()
    plt.show()

    print("5. Розподіл цін")
    data['UnitPrice'].plot(kind='hist', bins=50)
    plt.title('Розподіл цін')
    plt.xlabel('Ціна')
    plt.ylabel('Кількість товарів')
    plt.show()

    print("6. Продажі по годинах")
    data.groupby('Hour')['Revenue'].sum().plot(kind='bar')
    plt.title('Продажі по годинах')
    plt.xlabel('Година')
    plt.ylabel('Виручка')
    plt.xticks(rotation=0)
    plt.show()

def Business_conclusions(data):
    print("Висновки по бізнесу:")
    print("1. Найбільше продажів відбувається в місяці:", data.groupby('Month')['Revenue'].sum().idxmax())
    print("2. Найменше продажів відбувається в місяці:", data.groupby('Month')['Revenue'].sum().idxmin())
    print("3. Найбільше продажів відбувається в годину:", data.groupby('Hour')['Revenue'].sum().idxmax())
    print("4. ТОП-10 товарів за кількістю продажів:")
    print(data.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10))
    print("5. ТОП-10 країн за кількістю замовлень:")
    print(data['Country'].value_counts().head(10))

def main(data):
    info(data)
    data = clean_data(data)
    Creating_new_metrics(data)
    statistics(data)
    analysis(data)
    visualization(data)
    Business_conclusions(data)

if __name__ == "__main__":
    main(data)