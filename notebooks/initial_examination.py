df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv') # загрузка данных
pd.set_option('display.max_columns', 100) # раскрыть все стольбцы
pd.set_option('display.float_format', '{:.2f}'.format) # округлять до сотых
df.info() # Общая информация
df.size # Количество значений

class DataDescription:
    """
    JobSatisfaction - Удовлетворенность работой (1-4)
    MaritalStatus - Семейное положение  
    MonthlyIncome - Ежемесячный доход
    MonthlyRater - Ежемесячная ставка оплаты труда
    NumCompaniesWorked - Количество лет в компании
    Over18 - Старше 18 лет (Yes/No)
    OverTime - Переработка (Yes/No)
    PercentSalaryHike - Процент повышения зарплаты
    PerformanceRating - Рейтинг производительности (1-4)
    RelationshipSatisfaction - Удовлетворенность отношениями (1-4)
    StandardHours - Стандартное количество рабочих часов
    StockOptionLevel - Шкала от 0 до 3
    TotalWorkingYears - Общий стаж работы
    """
    pass

# === НАЧАЛО ОПИСАНИЯ ПЕРЕМЕННЫХ ===
"""
| Поле                           | Описание                                    |
|--------------------------------|---------------------------------------------|
| **Age** | Возраст сотрудника (в годах)|
| **Attrition** | Уволен (Yes/No)|
| **BusinessTravel** | Командировки (Travel_Rarely, Travel_Frequently, Non-Travel)|
| **DailyRate** | Дневная ставка оплаты (число)|
| **Department** | Отдел (Sales, Research & Developmen, Human Resource)|
| **DistanceFromHome** | Расстояние от дома до работы (в км/милях)|
| **Education** | Образование (от 1 до 5, где Below College - 1, College - 2, Bachelor - 3, Master - 4, Doctor - 5)|
| **EducationField** | Область образования (Life Sciences, Medical, Marketing, Technical Degree, Human Resources и др.)|
| **EmployeeCount** | Количество сотрудников|
| **EmployeeNumber** | Номер сотрудника|
| **EnvironmentSatisfaction** | Удовлетворенность условиями работы (от 1 до 4, где Low - 1, Medium - 2, High - 3, Very High - 4)|
| **Gender** | Пол (Female/Male)|
| **HourlyRate** | Почасовая ставка оплаты (число)|
| **JobInvolvement** | Вовлеченность в работу (от 1 до 4, где Low - 1, Medium - 2, High - 3, Very High - 4)|
| **JobLevel** | Уровень работы (от 1 до 5)|
| **JobRole** | Должность (Sales Executive, Research Scientist, Laboratory Technician, Manufacturing Director, Healthcare Representative, Manager, Sales Representative, Research Director, Human Resources)|
| **JobSatisfaction** | Удовлетворенность работой (от 1 до 4, где Low - 1, Medium - 2, High - 3, Very High - 4)|
| **MaritalStatus** | Семейное положение (Single, Married, Divorced)|
| **MonthlyIncome** | Ежемесячный доход (число)|
| **MonthlyRater** | Ежемесячная ставка оплаты труда (число)|
| **NumCompaniesWorked** | Количество лет, отработанных в компании (число)|
| **Over18** | Старше 18 лет (Yes/No)|
| **OverTime** | Переработка (Yes/No)|
| **PercentSalaryHike** | Процент повышения зарплаты (число)|
| **PerformanceRating** | Рейтинг производительности (от 1 до 4, где Low - 1, Good - 2, Excellent - 3, Outstanding - 4)|
| **RelationshipSatisfaction** | Удовлетворенность отношениями (от 1 до 4, где Low - 1, Medium - 2, High - 3, Very High - 4)|
| **StandardHours** | Стандартное количество рабочих часов в неделю, установленное компанией для сотрудников|
| **StockOptionLevel** | Шкала от 0 до 3|
| **TotalWorkingYears** | Общий стаж работы|
| **TrainingTimesLastYear** | Количество часов обучения в прошлом году|
| **WorkLifeBalance** | Баланс между работой и личной жизнью (от 1 до 4, где Bad - 1, Good - 2, Better - 3, Best - 4)|
| **YearsAtCompany** | Количество лет в компании (число)|
| **YearsInCurrentRole** | Количество лет в текущей должности (число)|
| **YearsSinceLastPromotion** | Количество лет с последнего повышения (число)|
| **YearsWithCurrManager** | Количество лет с текущим менеджером (число)|
"""
# === КОНЕЦ ОПИСАНИЯ ПЕРЕМЕННЫХ ===
 
df.describe() # Статистические сведения о датафрейме
