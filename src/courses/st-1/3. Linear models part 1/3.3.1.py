import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib

matplotlib.use('TkAgg')  # Используйте 'TkAgg' для интерактивного отображения в обычной среде Python
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

df = pd.read_csv('src/courses/st-1/3. Linear models part 1/data.csv')

df.columns = ['Timestamp', 'Age', 'Industry', 'Job', 'Job context', 'Salary',
              'Amount of monetary compensation', 'Currency',
              'Currency special', 'Income context', 'Country',
              'State in USA', 'City', 'Work expirince all',
              'Work expirince in current field', 'Education', 'Gender', 'Race'
              ]


# print(df.shape) # count of data
# print(df.dtypes) # get types of data
# print(df.describe()) # get statistic
# print(df.duplicated().sum()) # get amount of dup
# print(df.isna().sum()) # get about empty fields

def get_exchange_rate(currency, timestamp, currency_special):
    rates = {
        'TRY': 0.032,
        'CAD': 0.74,
        'GBP': 1.26,
        'EUR': 1.26,
        'JPY': 0.0067,
        'SEK': 0.096,
        'CHF': 1.13,
        'AUD/NZD': 0.65,
        'ZAR': 0.053,
        'HKD': 0.13,
        'NOK': 0.095,
        'PLN': 0.25,
        'SGD': 0.74,
        'INR': 0.012,
        'USD': 1,
    }
    if currency in rates:
        return rates[currency]
    elif currency_special in rates:
        return rates[currency_special]
    else:
        return None


usa_names = ['United States', 'US', 'USA',
             'usa', 'U.S.', 'United States ', 'us',
             'Usa', 'United States of America', 'United states', 'USA ',
             'United states ', 'united states', 'United States of America ',
             'U.S. ', 'U.S>', 'ISA', 'US ', 'United State', 'U.S.A',
             'U.S.A.', 'America', 'united states of america', 'Us', 'The United States',
             'United State of America', 'United Stated', 'u.s.', 'UNITED STATES', 'united States',
             'USA-- Virgin Islands', 'U.S', 'Unites States ', 'Usa ', 'U.S.A. ',
             'U. S. ', 'United Sates', 'United States of American ''Uniited States',
             'Worldwide (based in US but short term trips aroudn the world)',
             'United Sates of America', 'United States', 'america', 'Unted States', 'United Statesp',
             'United Stattes', 'United Statea', 'Unites States', 'United Statees',
             'UNited States', 'Uniyed states', 'Uniyes States', 'United States of Americas',
             'U.A.', 'U. S.' 'US of A', 'United States of america ',
             'U.SA', 'United Status', ' U.S.', 'Serbia', 'Canada and USA',
             'Virginia', 'U.s.', 'U.s.a.', 'USS', 'Uniteed States', 'United Stares',
             ' US', 'Unites states ', 'Us ', 'Unite States', 'The US',
             'united states ', 'United States (I work from home and my clients are all over the US/Canada/PR',
             'United states of America ', 'For the United States government, but posted overseas',
             'From Romania, but for an US based company', 'UnitedStates', 'Uniited States',
             'United States of america', 'United statew', ' United States', 'United Statues',
             'Untied States', 'United States of American ', 'USA (company is based in a US territory, I work remote)',
             'USAB', 'Unitied States', 'United Sttes', 'united stated', 'United States Of America',
             'Uniter Statez', 'U. S ', 'United states of America',
             'USA tomorrow ', 'United Stateds', 'Japan, US Gov position',
             'n/a (remote from wherever I want)', 'US govt employee overseas, country withheld', 'usa ',
             'San Francisco', 'Usat', '🇺🇸 ', 'Unitef Stated', 'UA',
             'United Stares ', 'United STates', 'USaa', 'uSA',
             'United States- Puerto Rico', 'California ', 'US of A',
             'uS', 'USD', "USA, but for foreign gov't", 'U. S.', 'United y',
             'United Statss', 'United states of america', 'UsA',
             'I work for a UAE-based organization, though I am personally in the US.',
             'United  States', 'United States is America',
             'United States of American', 'U.S.A ', 'United Statws']

uk_names = ['United Kingdom', 'United Kingdom ', 'Scotland ',
            'United Kingdom', 'UK ', 'England/UK',
            'UK', 'Great Britain ', 'Englang',
            'Scotland', 'UK (England)',
            'England', 'UK', 'Wales (United Kingdom)', 'England ',
            'Ireland', 'United kingdom ', 'Uk', 'united kingdom',
            'Great Britain', 'UK for U.S. company',
            'England', 'U.K. (northern England)', 'U.K',
            'Ireland', 'Wales (UK)', 'ireland'
                                     'Northern Ireland', 'europe', 'United Kingdom (England)',
            'United Kingdom.', 'Northern Ireland ', 'england',
            'United kingdom', 'United Kingdomk', 'UK (Northern Ireland)',
            'England, Gb', 'UK, remote', 'ENGLAND', 'England, UK.',
            'England, United Kingdom', 'U.K.', 'Scotland, UK', 'Wales', 'United Kindom',
            'Wales, UK', 'Unites kingdom', 'U.K. ',
            'Wales, UK', 'England, UK', 'Uk ', 'uk',
            'Northern Ireland, United Kingdom', 'uk',
            'UK, but for globally fully remote company']

canada_names = ['canada', 'Canada ', 'Canada, Ottawa, ontario', 'CANADA ',
                'Canadw', 'CANADA', 'Can', 'Canda', 'Canad', 'Csnada', 'Canadá', 'Canada ', 'Canad', 'Csnada', 'Canada']

ger_names = ['Germany ', 'germany', 'Company in Germany. I work from Pakistan.', 'Germany']

indexes_to_drop = []
for index, row in df.iterrows():
    if row['Currency'] != 'USD':
        exchange_rate = get_exchange_rate(row['Currency'], row['Timestamp'], row['Currency special'])
        if exchange_rate is None:
            indexes_to_drop.append(index)
        else:
            df.at[index, 'Currency'] = 'USD'
            df.at[index, 'Salary'] = float(row['Salary'].replace(',', '')) * exchange_rate
    if row['Country'] in usa_names:
        df.at[index, 'Country'] = 'USA'
    elif row['Country'] in uk_names:
        df.at[index, 'Country'] = 'UK'
    elif row['Country'] in canada_names:
        df.at[index, 'Country'] = 'CAN'
    elif row['Country'] in ger_names:
        df.at[index, 'Country'] = 'GER'
    else:
        df.at[index, 'Country'] = 'OTHER_WORLD'

filtered_df = df[df['City'].isna()]
for index, row in filtered_df.iterrows():
    country_capital = {
        'USA': ' Washington',
        'OTHER_WORLD': 'Madrid',
        'CAN': 'Ottawa',
        'UK': 'London',
    }
    df.at[index, 'City'] = country_capital[row['Country']]

df.drop(indexes_to_drop, inplace=True)
df.drop('Currency', axis=1, inplace=True)
df.drop('Currency special', axis=1, inplace=True)
df.drop('State in USA', axis=1, inplace=True)
df.drop('Income context', axis=1, inplace=True)
df.drop('Job context', axis=1, inplace=True)

filtered_df = df[df['Amount of monetary compensation'].notna()]
for index, row in filtered_df.iterrows():
    if type(row['Salary']) is str:
        df.at[index, 'Salary'] = row['Amount of monetary compensation'] + float(row['Salary'].replace(',', ''))
    else:
        df.at[index, 'Salary'] = row['Amount of monetary compensation'] + row['Salary']
df.drop('Amount of monetary compensation', axis=1, inplace=True)
df = df.dropna()

filtered_df = df[df['Salary'].notna()]
for index, row in filtered_df.iterrows():
    if type(row['Salary']) is str:
        df.at[index, 'Salary'] = float(row['Salary'].replace(',', ''))

print(df.dtypes) # get types of data

bins = list(range(0, 310000, 10000))
labels = [f"{i}k-{i+10}k" for i in range(0, 300, 10)]
df['Salary Range'] = pd.cut(df['Salary'], bins=bins, labels=labels, right=False)
countries = df['Country'].unique()
fig, axs = plt.subplots(len(countries), 1, figsize=(10 * 0.6, 6 * len(countries) * 0.6))

for ax, country in zip(axs, countries):
    country_data = df[df['Country'] == country]
    salary_range_counts = country_data['Salary Range'].value_counts().sort_index()
    salary_range_counts.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
    ax.set_title(f'Salary distribution in {country}')
    ax.set_xlabel('Salary range')
    ax.set_ylabel('Quantity')
    ax.grid(True, axis='y')

plt.tight_layout()
plt.show()


def create_combined_distribution_plot(column_name):
    categories = df[column_name].unique()
    categories = np.sort(categories)
    df['Salary Range'] = pd.cut(df['Salary'], bins=bins, labels=labels, right=False)
    plot_data = {}
    for category in categories:
        plot_data[category] = df[df[column_name] == category]['Salary Range'].value_counts().reindex(labels,
                                                                                                     fill_value=0)
    plt.figure(figsize=(15, 8))
    width = 1 / (len(categories) + 1)
    positions = np.arange(len(labels))

    for i, category in enumerate(categories):
        plt.bar(positions + i * width, plot_data[category], width, label=category)

    plt.xticks(positions + width, labels, rotation=45)
    plt.title(f'Salary distribution by {column_name}')
    plt.xlabel('Salary range')
    plt.ylabel('Quantity')
    plt.legend(title=column_name)
    plt.grid(True, axis='y')
    plt.show()

# create_combined_distribution_plot('Age')
# create_combined_distribution_plot('Work expirince in current field')
# create_combined_distribution_plot('Work expirince all')

create_combined_distribution_plot('Gender')
