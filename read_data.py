import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# read file
xl = pd.ExcelFile('WBL50.xlsx')
print('Sheet names:', xl.sheet_names)  # see all sheet names
print('-------' * 8)

# read selected sheet
df = xl.parse('WBL2021')
df_time = xl.parse('1971-2021')
print(df.head())
print('-------' * 8)

# filter columns
print('Column names:', df_time.columns)
print('-------' * 8)

cols = ['economy', 'Region', 'Income group', 'reportyr',
        'Can a woman apply for a passport in the same way as a man?',
        'Can a woman travel outside the country in the same way as a man?',
        'Can a woman travel outside her home in the same way as a man?',
        'Can a woman choose where to live in the same way as a man?',
        'Can a woman get a job in the same way as a man?',
        'Can a woman work at night in the same way as a man?',
        'Can a woman work in a job deemed dangerous in the same way as a man?',
        'Can a woman work in an industrial job in the same way as a man?',
        'Is there no legal provision that requires a married woman to obey her husband?',
        'Can a woman be head of household in the same way as a man?',
        'Can a woman obtain a judgment of divorce in the same way as a man?',
        'Does a woman have the same rights to remarry as a man?',
        'Can a woman sign a contract in the same way as a man?',
        'Can a woman register a business in the same way as a man?',
        'Can a woman open a bank account in the same way as a man?',
        'Do men and women have equal ownership rights to immovable property?',
        'Do sons and daughters have equal rights to inherit assets from their parents?',
        'Do male and female surviving spouses have equal rights to inherit assets?',
        'Does the law grant spouses equal administrative authority over assets during marriage?']

cols_indicators = ['Can a woman apply for a passport in the same way as a man?',
                   'Can a woman travel outside the country in the same way as a man?',
                   'Can a woman travel outside her home in the same way as a man?',
                   'Can a woman choose where to live in the same way as a man?',
                   'Can a woman get a job in the same way as a man?',
                   'Can a woman work at night in the same way as a man?',
                   'Can a woman work in a job deemed dangerous in the same way as a man?',
                   'Can a woman work in an industrial job in the same way as a man?',
                   'Is there no legal provision that requires a married woman to obey her husband?',
                   'Can a woman be head of household in the same way as a man?',
                   'Can a woman obtain a judgment of divorce in the same way as a man?',
                   'Does a woman have the same rights to remarry as a man?',
                   'Can a woman sign a contract in the same way as a man?',
                   'Can a woman register a business in the same way as a man?',
                   'Can a woman open a bank account in the same way as a man?',
                   'Do men and women have equal ownership rights to immovable property?',
                   'Do sons and daughters have equal rights to inherit assets from their parents?',
                   'Do male and female surviving spouses have equal rights to inherit assets?',
                   'Does the law grant spouses equal administrative authority over assets during marriage?']

women = df[cols]
women_time = df_time[cols]

# encode variables
for column in cols_indicators:
    women[column] = women[column].map({'Yes': 1, 'No': 0})
    women_time[column] = women_time[column].map({'Yes': 1, 'No': 0})

# create Total column to get sum of all YES
women["Total"] = women[cols_indicators].sum(axis=1)
women_time["Total"] = women_time[cols_indicators].sum(axis=1)

# get avg by region
region_df = women.groupby(['Region']).Total.mean().reset_index()

print('Average by Region')
print(region_df)
print('-------' * 8)

# get avg by income
income_df = women.groupby(['Income group']).Total.mean().reset_index()

print('Average by Income group')
print(income_df)
print('-------' * 8)

# percentage of women's rights
women['Total Percentage'] = round(((women['Total'] / 19) * 100), 2)

print("Women's freedoms in percentages")
print(women[['economy', 'Total Percentage']])
print('-------' * 8)

# percentage of countries that violate at least one women's rights
no_violation = len(women[women['Total Percentage'] == 100])

print("Countries that violate at least one women's right:")
print('Total countries:', len(women))
print("Countries that don't violate any women's right:", no_violation)
print("Percentage of countries that don't violate any women's right: {}%".format(
    round((no_violation / (len(women)) * 100), 2)))
print('-------' * 8)

# Sub-Saharan Africa, South Asia, LatAm, MENA
# Entrepreneurship + Mobility
# Overall change in score vs selected regions

placeholder = women_time.groupby(['reportyr'])['Total'].mean()
women_by_region = women_time.groupby(['reportyr', 'Region'])['Total'].mean().reset_index()
women_pivot = women_by_region.pivot(index='reportyr', columns='Region', values='Total')

for i in women_time['Region'].unique():
    a = np.array(women_pivot[i])
    plt.plot(range(1971, 2022), a, label=i)
placeholder.plot(label='Overall Women')
plt.legend(title="Women's Score", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title("Women's Freedom by Region")
plt.xlabel('Year')
plt.ylabel('Score')
plt.show()
