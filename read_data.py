import pandas as pd

import warnings
warnings.filterwarnings("ignore")

# read file
xl = pd.ExcelFile('WBL50.xlsx')
print('Sheet names:', xl.sheet_names)  # see all sheet names
print('-------' * 8)

# read selected sheet
df = xl.parse('WBL2021')
print(df.head())
print('-------' * 8)

# filter columns
print('Column names:', df.columns)
print('-------' * 8)

cols = ['economy', 'Region', 'Income group',
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

# encode variables
for column in cols_indicators:
    women[column] = women[column].map({'Yes': 1, 'No': 0})

# create Total column to get sum of all YES
women["Total"] = women[cols_indicators].sum(axis=1)

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
print("Percentage of countries that don't violate any women's right: {}%".format(round((no_violation/(len(women)) * 100), 2)))
print('-------' * 8)

# correlation w/ HFI
# Sub-Saharan Africa, South Asia, LatAm, MENA
# Entrepreneurship + Mobility
# Overall change in score vs selected regions
#

