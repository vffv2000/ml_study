# Задание: Анализ данных с использованием логистической регрессии

## Цель задания
Научиться применять модель логистической регрессии для анализа данных и интерпретации результатов в Python с использованием библиотеки `statsmodels`.

## Описание данных
Используйте датасет `college-admissions.csv`, который содержит следующие переменные:
- `admitted` - категориальная переменная, указывающая, был ли студент зачислен (да/нет).
- `hs.gpa` - средний балл за аттестат средней школы.
- `sat.score` - баллы студента за тест SAT.

## Шаги выполнения

**Шаг 1: Подготовка данных**
- Загрузите данные из файла CSV.

**Шаг 2: Построение модели логистической регрессии**
- Примените модель `Logit` из библиотеки `statsmodels` для анализа вероятности зачисления студента в зависимости от его баллов за SAT и среднего балла аттестата.

**Шаг 3: Визуализация и анализ результатов**
- Визуализируйте результаты модели логистической регрессии, используя графики для лучшего понимания влияния независимых переменных на вероятность зачисления.
- Интерпретируйте коэффициенты модели и оцените их статистическую значимость.

**Шаг 4: Тестирование модели**
- Примените полученную модель к новым данным (если доступны) для проверки её эффективности и точности предсказаний.

## Требования
- Для анализа данных использовать Python и библиотеки `pandas`, `statsmodels`, `matplotlib`.
- Корректно интерпретировать результаты анализа.
- В документации к заданию предоставить визуализации и их описание.




# Task: Data Analysis Using Logistic Regression

## Task Objective
Learn how to apply logistic regression modeling for data analysis and result interpretation in Python using the `statsmodels` library.

## Data Description
Use the `college-admissions.csv` dataset, which includes the following variables:
- `admitted` - a categorical variable indicating whether a student was admitted (yes/no).
- `hs.gpa` - high school grade point average.
- `sat.score` - student's SAT test score.

## Execution Steps

**Step 1: Data Preparation**
- Load the data from the CSV file.

**Step 2: Building a Logistic Regression Model**
- Use the `Logit` model from the `statsmodels` library to analyze the probability of student admission based on their SAT scores and high school GPA.

**Step 3: Visualization and Analysis of Results**
- Visualize the results of the logistic regression model using plots for a better understanding of how the independent variables affect the probability of admission.
- Interpret the model coefficients and evaluate their statistical significance.

**Step 4: Model Testing**
- Apply the developed model to new data (if available) to check its effectiveness and accuracy of predictions.

## Requirements
- Use Python and libraries such as `pandas`, `statsmodels`, `matplotlib` for data analysis.
- Correctly interpret the analysis results.
- Provide visualizations and their descriptions in the task documentation.
