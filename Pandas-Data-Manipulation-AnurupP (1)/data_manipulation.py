import pandas

''' When going through the assignment, keep in mind that to actually see these variables you need to use python's print() statement to see their values printed out in replit's console 
'''

# Step 1: Use the appropriate pandas method to read the titanic data into your python file 
titanic_data = pandas.read_csv("titanic.csv")

# Step 2(a): Use the pandas method that reads the first 25 lines of the dataset
first_25_passengers = titanic_data.head(25)

# Step 2(b): Use the pandas method thats reads the last 25 lines of the dataset
last_25_passengers = titanic_data.tail(25)

# Step 3: Use the pandas method that only tells us the number of rows and columns in our data
titanic_shape = titanic_data.shape

# Step 4: Describe the titanic data
titanic_description = titanic_data.describe

# Step 5(a): How many passengers were between the ages of 0 to 16? 
children = len(titanic_data[titanic_data["Age"] <=16 ])

# Step 5(b): How many passengers were between the ages of 17 to 25?
young_adults = len(titanic_data[(titanic_data["Age"] > 16) & (titanic_data["Age"] <= 25)])

# Step 5(c): How many passengers were between the ages of 26 to 40?
adults = len(titanic_data[(titanic_data["Age"] > 25) & (titanic_data["Age"] <=40)])

# Step 5(d): How many passengers were between the ages of 41 to 59?
mature_adults = len(titanic_data[(titanic_data["Age"] > 40) & (titanic_data["Age"] <=59)])

# Step 5(e): How many passengers were 60 or older?
seniors = len(titanic_data[titanic_data["Age"] >= 60 ])

# Step 6: How many values are missing from the "age" column
missing_ages = titanic_data["Age"].isnull().sum()

# Step 7: List out all the available passengers' ages
age_list = list(titanic_data["Age"].unique())

# Step 8: Filter the DataFrame to find all passengers who boarded the Titanic at Port Cherbourg
cherbourg_passengers = titanic_data[titanic_data['Embarked'] == 'C']

# Step 9(a): Find the average age of all female passengers
females = titanic_data[titanic_data["Sex"] == "female"]
avg_fem_age = females["Age"].mean()

# Step 9(b): Find the average age of all male passengers
males = titanic_data[titanic_data["Sex"] == "male"]
avg_male_age = males["Age"].mean()

# Step 10(a): Find the survival percentage of passengers in group "C"
cherbourg_survival = (len(cherbourg_passengers[cherbourg_passengers['Survived']== 1])/len(cherbourg_passengers)*100)

# Step 10(b): Find the survival percentage of passengers in group "Q"
queenstown_passengers = titanic_data[titanic_data['Embarked'] == 'Q']
queenstown_survival = (len(queenstown_passengers[queenstown_passengers['Survived'] == 1])/len(queenstown_passengers)*100)

# Step 10(c): Find the survival percentage of passengers in group "S"
south_passengers = titanic_data[titanic_data['Embarked'] == 'S']
south_survival = (len(south_passengers[south_passengers['Survived'] == 1])/len(south_passengers)*100)

