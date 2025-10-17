df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv') # загрузка данных
pd.set_option('display.max_columns', 100) # раскрыть все стольбцы
pd.set_option('display.float_format', '{:.2f}'.format) # округлять до сотых
df.info() # Общая информация
df.size # Количество значений
[ОПИСАНИЯ ПЕРЕМЕННЫХ]()
df.describe() # Статистические сведения о датафрейме
