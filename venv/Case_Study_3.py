# Approach to Solve
# You have to use fundamentals of Python taught in module3
# 1.Read file bank-data.csv
# 2.Build a set of unique jobs
# 3.Read the input from command line –profession
# 4.Check if professionis in list
# 5.Print whether client is eligible


# 1.Read file bank-data.csv

import pandas as pd

df = pd.read_csv(r"C:\Users\linki\Downloads\az892obnyi\651_m3_datasets_v1.0\bank-data.csv")

# 2. Build a set of unique jobs

job_set = set(list(df.job)) # convert to a list from a series/dataframe to get a set

print(job_set)

# 3. Read the input from command line –profession
x = input("Enter the profession: ")

# 4.Check if professionis in list

for var in list(job_set):#make this iterable
    if x == var:
        ans = x
    else:
        ans = 0

# 5.Print whether client is eligible
if ans == 0:
    print("Profession not eligible")
else:
    print("Profession is eligible")
