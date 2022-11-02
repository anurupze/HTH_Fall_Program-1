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
survival_age_pers = 

# Step 4: Create a pie chart that shows the percentage of survivors that were male and the percentage of survivors that were female
survivors = 

# Step 5: Create a histogram that shows the distribution of passengers between the three embarking locations: C (Cherbourg), Q (Queenstown), S (Southampton)
titanic_description = 