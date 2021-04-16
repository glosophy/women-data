import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
import seaborn as sns

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

# save file for datviz
women.to_csv('WomenTotal.csv')

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

# Entrepreneurship + Mobility
# Overall change in score vs selected regions

# plot women's score by region
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

# plot entrepreneurship and mobility
mobility = ['economy', 'Region', 'Income group', 'reportyr',
            'Can a woman apply for a passport in the same way as a man?',
            'Can a woman travel outside the country in the same way as a man?',
            'Can a woman travel outside her home in the same way as a man?',
            'Can a woman choose where to live in the same way as a man?']

entrepreneur = ['economy', 'Region', 'Income group', 'reportyr',
                'Can a woman sign a contract in the same way as a man?',
                'Can a woman register a business in the same way as a man?',
                'Can a woman open a bank account in the same way as a man?']

# mobility
mob = women_time[mobility]
mob["total_mobility"] = mob[['Can a woman apply for a passport in the same way as a man?',
                             'Can a woman travel outside the country in the same way as a man?',
                             'Can a woman travel outside her home in the same way as a man?',
                             'Can a woman choose where to live in the same way as a man?']].sum(axis=1)

placeholder1 = mob.groupby(['reportyr'])['total_mobility'].mean()
women_mob = mob.groupby(['reportyr', 'Region'])['total_mobility'].mean().reset_index()
women_mob_pivot = women_mob.pivot(index='reportyr', columns='Region', values='total_mobility')

for j in women_mob['Region'].unique():
    a = np.array(women_mob_pivot[j])
    plt.plot(range(1971, 2022), a, label=j)
placeholder1.plot(label='Overall Women')
plt.legend(title="Women's Mobility Score", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title("Women's Mobility by Region")
plt.xlabel('Year')
plt.ylabel('Score')
plt.show()

# regions with biggest increase/decrease
mob1971, mob2021 = np.array(women_mob[women_mob['reportyr'] == 1971]['total_mobility']), \
                   np.array(women_mob[women_mob['reportyr'] == 2021]['total_mobility'])

regions = [i for i in women_mob['Region'].unique()]

mob_diff = ((mob2021 / mob1971) - 1) * 100

print('Change in Mobility Score (1971-2021):')
for i in range(len(mob_diff)):
    print('{}: {}%'.format(regions[i], round(mob_diff[i], 2)))
print('-------' * 8)

# entrepreneur
ent = women_time[entrepreneur]
ent["total_entrepreneurship"] = ent[['Can a woman sign a contract in the same way as a man?',
                                     'Can a woman register a business in the same way as a man?',
                                     'Can a woman open a bank account in the same way as a man?']].sum(axis=1)

placeholder2 = ent.groupby(['reportyr'])['total_entrepreneurship'].mean()  # for overall score
women_ent = ent.groupby(['reportyr', 'Region'])['total_entrepreneurship'].mean().reset_index()
women_ent_pivot = women_ent.pivot(index='reportyr', columns='Region', values='total_entrepreneurship')

for j in women_ent['Region'].unique():
    a = np.array(women_ent_pivot[j])
    plt.plot(range(1971, 2022), a, label=j)
placeholder2.plot(label='Overall Women')
plt.legend(title="Women's Entrepreneurship Score", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title("Women's Entrepreneurship by Region")
plt.xlabel('Year')
plt.ylabel('Score')
plt.show()

# regions with biggest increase/decrease
ent1971, ent2021 = np.array(women_ent[women_ent['reportyr'] == 1971]['total_entrepreneurship']), \
                   np.array(women_ent[women_ent['reportyr'] == 2021]['total_entrepreneurship'])

ent_regions = [i for i in women_mob['Region'].unique()]

ent_diff = ((ent2021 / ent1971) - 1) * 100

print('Change in Entrepreneurship Score (1971-2021):')
for i in range(len(ent_diff)):
    print('{}: {}%'.format(regions[i], round(ent_diff[i], 2)))
print('-------' * 8)

# countries with biggest increase/decrease
ent_countries1971 = ent[ent['reportyr'] == 1971][['total_entrepreneurship', 'economy']]
ent_countries2021 = ent[ent['reportyr'] == 2021][['total_entrepreneurship', 'economy']]

diff_countries = (np.array(ent_countries2021['total_entrepreneurship']) -
                  np.array(ent_countries1971['total_entrepreneurship']))

country_list = [i for i in ent_countries2021['economy'].unique()]

# create dictionary with values for pct change and countries
print('Change in Entrepreneurship Score by Country (1971-2021):')
pct_ent_change = {country_list[i]: diff_countries[i] for i in range(len(country_list))}
print(pct_ent_change)
print('-------' * 8)

# countries with biggest increase/decrease overall
total1971 = women_time[women_time['reportyr'] == 1971][['Total', 'economy']]
total2021 = women_time[women_time['reportyr'] == 2021][['Total', 'economy']]

diff_total_countries = ((np.array(total2021['Total']) /
                        np.array(total1971['Total'])) - 1) * 100

country_list = [i for i in women_time['economy'].unique()]

# create dictionary with values for pct change and countries
print('Change in Total Score by Country (1971-2021):')
pct_total_change = {country_list[i]: round(diff_total_countries[i], 2) for i in range(len(country_list))}
print(pct_total_change)
print('-------' * 8)

# sort dictionary
sorted_countries = {k: v for k, v in sorted(pct_total_change.items(), key=lambda item: item[1])}

pairs = []
for i in sorted_countries.items():
    pairs.append(i)

print('Biggest Increase (1971-2021):')
print(pairs[-10:])
print('-------' * 8)
print('Biggest Decrease (1971-2021):')
print(pairs[:11])
print('-------' * 8)

# sns distplot (density)
dist2021 = women_time[women_time['reportyr'] == 2021]['Total']
dist1971 = women_time[women_time['reportyr'] == 1971]['Total']
sns.distplot(dist2021, hist=False, kde=True, kde_kws={'linewidth': 3}, label='2021')
sns.distplot(dist1971, hist=False, kde=True, kde_kws={'linewidth': 3}, label='1971')
plt.legend(title='Year')
plt.title('Density Plot | Women Freedoms Distribution')
plt.xlabel("Women's Freedoms")
plt.ylabel('Density')
plt.show()

# women's rights across regions
region = women_time['Region'].unique()

for i in range(len(regions)):
    ssa_dist2021 = women_time.loc[(women_time['reportyr'] == 2021) & (women_time['Region'] == region[i])][
        'Total']
    ssa_dist1971 = women_time.loc[(women_time['reportyr'] == 1971) & (women_time['Region'] == region[i])][
        'Total']
    sns.distplot(ssa_dist2021, hist=False, kde=True, kde_kws={'linewidth': 3}, label='2021')
    sns.distplot(ssa_dist1971, hist=False, kde=True, kde_kws={'linewidth': 3}, label='1971')
    plt.legend(title='Year')
    plt.title('Density Plot | Women Freedoms Distribution {}'.format(region[i]))
    plt.xlabel("Women's Freedoms")
    plt.ylabel('Density')
    plt.show()

hio = women_time.loc[(women_time['reportyr'] == 1971) & (women_time['Region'] == 'High income: OECD')]['Total']
hio2021 = women_time.loc[(women_time['reportyr'] == 2021) & (women_time['Region'] == 'High income: OECD')]['Total']

hio = hio.tolist()
hio2021 = hio2021.tolist()

sns.distplot(hio2021, hist=True, kde=True, kde_kws={'linewidth': 1}, label='2021')
# sns.distplot(hio, hist=False, kde=True, kde_kws={'linewidth': 3}, label='1971')
plt.legend(title='Year')
plt.title('Density Plot | Women Freedoms Distribution High Income')
plt.xlabel("Women's Freedoms")
plt.ylabel('Density')
plt.show()

print(len(hio))
print(len(hio2021))

print(hio)
print(hio2021)

