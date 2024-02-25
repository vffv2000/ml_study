# Задание: Линейная регрессия с категориальными переменными

## Цель задания
Освоить методы работы с категориальными переменными и построение линейной регрессии в Python.

## Данные
Датасет `satgpa.csv` содержит информацию о студентах и их успеваемости.

## Задачи
1. **Обработка категориальных переменных.** В столбце `Attendance` присутствуют значения "yes" и "no". Необходимо заменить их на числовые эквиваленты: 1 и 0.
2. **Построение модели регрессии.** Используя обработанные данные, построить модель линейной регрессии для предсказания успеваемости студентов.
3. **Визуализация результатов.** Построить регрессионные прямые для групп студентов с различной посещаемостью (75% занятий и менее).
4. **Тестирование модели.** Применить полученную модель к тестовым данным и оценить её эффективность.

## Требования
- Использовать библиотеку `pandas` для обработки данных.
- Применить `statsmodels` или `scikit-learn` для построения линейной регрессии.
- Визуализировать данные с помощью `matplotlib`.



# Task: Linear Regression with Categorical Variables

## Task Objective
Learn how to work with categorical variables and build linear regression models in Python.

## Data
The dataset `satgpa.csv` contains information about students and their academic performance.

## Tasks
1. **Handling Categorical Variables.** The `Attendance` column contains "yes" and "no" values. These should be replaced with numeric equivalents: 1 and 0.
2. **Regression Model Building.** Using the processed data, build a linear regression model to predict student performance.
3. **Visualization of Results.** Plot regression lines for groups of students with different attendance rates (75% of classes and below).
4. **Model Testing.** Apply the developed model to test data and evaluate its effectiveness.

## Requirements
- Use the `pandas` library for data processing.
- Apply `statsmodels` or `scikit-learn` for linear regression modeling.
- Visualize data using `matplotlib`.