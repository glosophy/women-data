# Women's Rights Around the World

## :octocat: Repo Content
This repo includes:
* `WBL50.xlsx`: raw data
* `WomenTotal.csv`: clean data with selected indicators
* `read_data.py`: script for data analysis
* `FinalPoster.png`, `SecondaryCharts.png`: final dataviz with some other secondary charts ready for publication
* `SocialMedia-02.png`: promo image for sharing on social media
* `FinalPoster3May-01.png`: final data viz (big poster)
* `FinalPosterRegions-04.png`: break-down of gender inequality by region, 1971 vs. 2021
* `FinalPosterWorld-04.png`: gender inequality worldwide

## :memo: Project Description
This project aims at understanding the state of women's rights around the world. The data comes from the [*Women, Business
and the Law 2021 Report*](https://openknowledge.worldbank.org/bitstream/handle/10986/35094/9781464816529.pdf) produced by the [World Bank (WB)](https://wbl.worldbank.org/en/wbl).
It evaluates 190 countries across 40 distinct indicators related to mobility, workplace, pay, marriage, parenthood, entrepreneurship, assets, and pension. The data ranges from 1971 to 2021.

From the WB's website:
>The indicators are used to build evidence of the relationship between legal gender equality and women’s entrepreneurship and employment.
>By examining the economic decisions women make as they go through different stages of their working lives, as well as the pace of reform over the past two years, *Women, Business and the Law* makes a contribution to policy discussions about the state of women’s economic opportunities.

## :computer: Data Description
For the purpose of this analysis, I worked with the following 19 indicators that better reflect the equality of men and women before the law: 
* Can a woman apply for a passport in the same way as a man?
* Can a woman travel outside the country in the same way as a man?
* Can a woman travel outside her home in the same way as a man?
* Can a woman choose where to live in the same way as a man?
* Can a woman get a job in the same way as a man?
* Can a woman work at night in the same way as a man?
* Can a woman work in a job deemed dangerous in the same way as a man?
* Can a woman work in an industrial job in the same way as a man?
* Is there no legal provision that requires a married woman to obey her husband?
* Can a woman be head of household in the same way as a man?
* Can a woman obtain a judgment of divorce in the same way as a man?
* Does a woman have the same rights to remarry as a man?
* Can a woman sign a contract in the same way as a man?
* Can a woman register a business in the same way as a man?
* Can a woman open a bank account in the same way as a man?
* Do men and women have equal ownership rights to immovable property?
* Do sons and daughters have equal rights to inherit assets from their parents?
* Do male and female surviving spouses have equal rights to inherit assets?
* Does the law grant spouses equal administrative authority over assets during marriage?

All these are binary indicators (`Yes = 1` and `No = 0`). In countries with higher scores (out of 19 points), women have the same rights as men before the law. 
Countries are also classfied according to four different income groups (`High income`, `Upper middle income`, `Lower middle income`, and `Low income`) and seven regions
(`East Asia & Pacific`, `Europe & Central Asia`, `High income: OECD`, `Latin America & Caribbean`, `Middle East & North Africa`, `South Asia`, and `Sub-Saharan Africa`).

## :eyeglasses: Some Findings...
#### :ok_woman: Top 5:
1. Australia (19)
2. Austria (19)
3. Belgium (19)
4. Canada (19)
5. Czech Republic (19)

#### :no_good: Bottom 5:
186. Egypt, Arab Rep. (7)
187. Iran, Islamic Rep. (7)
188. West Bank and Gaza (7)
189. Yemen, Rep. (7)
190. Sudan (5)

#### :earth_americas: Women's Rights by Region
1. High income: OECD (18.62)
2. Europe & Central Asia (17.83)
3. Latin America & Caribbean (17.75)
4. East Asia & Pacific (16.72)
5. Sub-Saharan Africa (14.81)
6. South Asia (14.75)
7. Middle East & North Africa (10.45)

#### :moneybag: Women's Rights by Income Group
1. High income (17.52)
2. Upper middle income (16.40)
3. Lower middle income (15.44)
4. Low income (13.96)

#### :arrow_up: Change in Score: Biggest Increase in Score (in %, 1971-2021)
1. Spain (216.67%)
2. Togo (200%)
3. São Tomé and Príncipe (200%)
4. United Arab Emirates (200%)   
5. Congo, Dem. Rep. (180%)
6. Indonesia (180%)

#### :arrow_down: Change in Score: Biggest Decrease in Score (in %, 1971-2021)
1. Bhutan (-5.56%)
2. Albania (0%)
3. Antigua and Barbuda (0%)
4. Azerbaijan (0%)
5. Belize (0%)


## :bar_chart: Data Visualization
It all started with a bar chart. It ended with a Sankey plot. 

Once my data was already cleaned and ready to plot, I worked on Adobe Illustrator to design the main visualization as well as the smaller charts that accompanied the blog post.

I borrowed the color palette from a beautiful sunset in Curaçao. :ocean: :sunny:

## :two_hearts: Thank you!
JH, SSS, and IV for their feedback while preparing the viz.

Viz inspo: Diana Estefania Rubio.
