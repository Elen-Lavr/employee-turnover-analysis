df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv') # загрузка данных
pd.set_option('display.max_columns', 100) # раскрыть все стольбцы
pd.set_option('display.float_format', '{:.2f}'.format) # округлять до сотых
df.info() # Общая информация
df.size # Количество значений
[ОПИСАНИЯ ПЕРЕМЕННЫХ](.notebooks/02_Initial_examination_and_data_preparation/variable_description.md)
df.describe() # Статистические сведения о датафрейме
