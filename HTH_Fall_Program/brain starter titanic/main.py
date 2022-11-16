import pandas
import seaborn
import matplotlib.pyplot as plt

titanic = pandas.read_csv("titanic.csv")
''' 
The best way to complete this activity is to copy the code in this file into a jupyter notebook file you create. This will also you to see your visualizations easier. Once you have finished creating your visuals copy your code back into this file and submit it to Replit. Don't forget to also upload your new code to Github! 
'''
sex = []
for _,row in titanic.iterrows():
    if row["Sex"] == "male":
        sex.append(1)
    else:
        sex.append(0)
        
titanic["Sex"] = sex
# Step 1: Create a heatmap showing the correlation between the following features: survival, pclass, sex, age, and fare 
titanic_features = titanic[["Survived", "Pclass", "Sex", "Age", "Fare"]]
corr_heatmap = seaborn.heatmap(titanic_features.corr(), annot = True, cmap = "crest")

# Step 2: Create a bar graph that illustrates how many passengers fell into each of these age ranges: 0 - 16, 17 - 25, 26 -40, 41 - 59, 60 or older
age_group_chart = {
    "groups": ["16 and younger", 
               "17 to 25",
               "26 to 40",
               "41 to 59",
               "60 and above"],
    "count":[
         len(titanic[titanic["Age"] <=16 ]),
         len(titanic[(titanic["Age"] > 16) & (titanic["Age"] <= 25)]),
         len(titanic[(titanic["Age"] > 25) & (titanic["Age"] <= 40)]),
         len(titanic[(titanic["Age"] > 40) & (titanic["Age"] <= 59)]),
         len(titanic[titanic["Age"] >=60 ])]
}
visual_df = pandas.DataFrame(age_group_chart)
seaborn.barplot(data = visual_df, x = "groups", y = "count", ci = None, palette = "magma")

# Step 3: Create a line graph showing the average survival percentage of each of the previous age groups
below_16_passengers = titanic[titanic['Age'] <= 16]
survival_16 = (len(below_16_passengers[below_16_passengers['Survived'] == 1])/ len(below_16_passengers)*100)
youth = titanic[(titanic['Age'] > 16) & (titanic['Age'] <= 25)]
survival_youth = (len(youth[youth['Survived'] == 1])/ len(youth)*100)
adults = titanic[(titanic['Age'] > 25) & (titanic['Age'] <= 40)]
survival_adults = (len(adults[adults['Survived'] == 1])/ len(adults)*100)
mature_adults = titanic[(titanic['Age'] > 41) & (titanic['Age'] <= 59)]
survival_mature_adults = (len(mature_adults[mature_adults['Survived'] == 1])/ len(mature_adults)*100)
seniors = titanic[titanic['Age'] >= 60]
survival_seniors = (len(seniors[seniors['Survived'] == 1])/ len(seniors)*100)

age_group_survived = {
    "groups": ["16 and younger", 
               "17 to 25",
               "26 to 40",
               "41 to 59",
               "60 and above"],
    "survival":[survival_16,
                survival_youth,
                survival_adults,
                survival_mature_adults,
                survival_seniors]
}
visualized_df = pandas.DataFrame(age_group_survived) 
line_graph = visualized_df.plot.line(x = "groups", y = "survival")


# Step 4: Create a pie chart that shows the percentage of survivors that were male and the percentage of survivors that were female
males = titanic[titanic['Sex'] == 1]
males_survived = (len(males[males['Survived'] == 1])/ len(males)*100)
females = titanic[titanic['Sex'] == 0]
females_survived = (len(females[females['Survived'] == 1])/ len(females)*100)

survival_gender = {
    'survival': [males_survived, females_survived],
    'gender':[1 , 0]
    }

pie_df = pandas.DataFrame(survival_gender)
pie_df.plot.pie(y = 'survival', autopct = '%0.1f%%', figsize = (7,7), title ='Percentage of male and female survivors')

# Step 5: Create a histogram that shows the distribution of passengers between the three embarking locations: C (Cherbourg), Q (Queenstown), S (Southampton)
embark_num = [0,0]

for index, row in titanic.iterrows():
    if row["Embarked"] == "Q":
        embark_num.append(1)
    if row["Embarked"] == "C":
        embark_num.append(2)
    if row["Embarked"] == "S":
        embark_num.append(3)

titanic.dropna(subset=["Embarked"])
titanic["embarked"] = embark_num

titanic.hist(column="embarked")