## Шаг 1: Первичное улучшение вида данных

- **Переименование столбцов:** Теперь короткие и точно описывают содержание.
- **Получение данных о количестве записей:**
  ![Данные о количестве записей](../../../../media/st-1/3.%20Linear%20models%20part%201/1.Data_Count.png)
- **Получение типов данных:**
  ![Типы данных](../../../../media/st-1/3.%20Linear%20models%20part%201/2.Data_Types.png)
- **Получение описательной статистики:**
  ![Описательная статистика](../../../../media/st-1/3.%20Linear%20models%20part%201/3.Data_Statistics.png)
- **Проверка на наличие дубликатов:**
  ![Проверка на дубликаты](../../../../media/st-1/3.%20Linear%20models%20part%201/4.Check_on_duplicates.png)
- **Получение данных о пропусках:**
  ![Данные о пропусках](../../../../media/st-1/3.%20Linear%20models%20part%201/5.Check_on_Empty_Data.png)

## Шаг 2: Конвертация зарплат

- Приведение колонок `Salary` и `Amount of monetary compensation` к единой шкале измерения - доллару США.
- Операции включают получение записей в не-USD валюте, конвертацию через API курса валют, и обновление данных.
- Удаление полей `currency` и `Currency special`.
  ![Обновленные статистические данные](../../../../media/st-1/3.%20Linear%20models%20part%201/6.Data_Statistics2.png)

## Шаг 3: Унификация названий стран

- Приведение дубликатов названий стран к одному формату, например, 'United States', 'US', 'USA' -> 'USA'.
  ![Унификация стран](../../../../media/st-1/3.%20Linear%20models%20part%201/7.Check_on_Empty2.png)

## Шаг 4: Очистка данных

- Удаление ненужных полей и заполнение пропусков по городам столицами соответствующих стран.
  ![Очистка данных](../../../../media/st-1/3.%20Linear%20models%20part%201/8.Check_on_Empty3.png)

## Шаг 5: Удаление всех значений NaN

- Удалены все записи с `NaN`.
  ![Удаление NaN](../../../../media/st-1/3.%20Linear%20models%20part%201/9.Check_on_Empty4.png)

## Шаг 6: Создание графиков

- **Распределение зарплат по странам (с акцентом на США):**
  ![Распределение по странам](../../../../media/st-1/3.%20Linear%20models%20part%201/10.Figure1.png)
- **Зависимость зарплаты от возраста:**
  ![Зависимость от возраста](../../../../media/st-1/3.%20Linear%20models%20part%201/10.Figure2.png)
- **Зависимость зарплаты от опыта на текущей позиции:**
  ![Зависимость от текущего опыта](../../../../media/st-1/3.%20Linear%20models%20part%201/10.Figure3.png)
- **Зависимость зарплаты от общего опыта работы:**
  ![Зависимость от общего опыта](../../../../media/st-1/3.%20Linear%20models%20part%201/10.Figure4.png)
- **Зависимость зарплаты от гендера:**
  ![Зависимость от гендера](../../../../media/st-1/3.%20Linear%20models%20part%201/10.Figure5.png)



## Step 1: Initial Data Appearance Improvement

- **Renaming columns:** Now shorter and accurately describe the content.
- **Obtaining the count of records:**
  ![Data Count](../../../../media/st-1/3.%20Linear%20models%20part%201/1.Data_Count.png)
- **Obtaining data types:**
  ![Data Types](../../../../media/st-1/3.%20Linear%20models%20part%201/2.Data_Types.png)
- **Obtaining descriptive statistics:**
  ![Data Statistics](../../../../media/st-1/3.%20Linear%20models%20part%201/3.Data_Statistics.png)
- **Checking for duplicates:**
  ![Check on Duplicates](../../../../media/st-1/3.%20Linear%20models%20part%201/4.Check_on_duplicates.png)
- **Obtaining data on missing values:**
  ![Check on Empty Data](../../../../media/st-1/3.%20Linear%20models%20part%201/5.Check_on_Empty_Data.png)

## Step 2: Converting 'Salary' and 'Amount of monetary compensation' to a unified measurement scale - USD

- Retrieving all records where the currency value is not equal to USD.
- Starting the data iteration process.
- Obtaining Timestamp for the record and the Currency value.
- Using an API to get the exchange rate.
- Converting foreign currency to USD.
- Updating the data.
- Removing the 'currency' and 'Currency special' fields.
  ![Updated Statistical Data](../../../../media/st-1/3.%20Linear%20models%20part%201/6.Data_Statistics2.png)

## Step 3: Standardizing Country Names

- The dataset contains many duplicates; need to standardize to one 'United States', 'US', 'USA' -> 'USA'.
- Arrays of strings were prepared with the dataset and used for transformation.
  ![Country Standardization](../../../../media/st-1/3.%20Linear%20models%20part%201/7.Check_on_Empty2.png)

## Step 4: Eliminating Unnecessary Data/Empty Values

- Removed the 'state' field as there are multiple countries and a 'city' field is available (unnecessary information).
- Missing city data were filled with capitals from the countries (best obtained by state if America and taking the largest city in the state).
  ![Data Cleaning](../../../../media/st-1/3.%20Linear%20models%20part%201/8.Check_on_Empty3.png)
- 'Job context' and 'Income context' were removed.

## Step 5: Removing all NaN values
  ![Removing NaN](../../../../media/st-1/3.%20Linear%20models%20part%201/9.Check_on_Empty4.png)

## Step 6: Creating Charts

- **First chart showing salary distribution by countries (most relevantly the USA):**
  ![Distribution by Countries](../../../../media/st-1/3.%20Linear%20models%20part%201/10.Figure1.png)
- **Chart showing the dependency of salary on age:**
  ![Dependency on Age](../../../../media/st-1/3.%20Linear%20models%20part%201/10.Figure2.png)
- **Chart showing the dependency of salary on experience in the current position:**
  ![Dependency on Current Experience](../../../../media/st-1/3.%20Linear%20models%20part%201/10.Figure3.png)
- **Chart showing the dependency of salary on overall work experience:**
  ![Dependency on Overall Experience](../../../../media/st-1/3.%20Linear%20models%20part%201/10.Figure4.png)
- **Chart showing the dependency of salary on gender:**
  ![Dependency on Gender](../../../../media/st-1/3.%20Linear%20models%20part%201/10.Figure5.png)
