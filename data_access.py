import pandas as pd

def get_age(df):
    return df["Age"]

def get_third_name(df):
    return df.iloc[2]

def get_carol_deets(df):
    return df.loc["Carol"]

def get_salary_and_occupation(df):
    return df.loc[:,["Salary", "Occupation"]]

def get_age_salary_of_first_two(df):
    return df.loc["Alice":"Bob", ["Age","Salary"]]

def get_occupation_bob_eve(df):
    return df.loc[["Bob", "Eve"], "Occupation"]


    

def main():
    df = pd.read_csv("data.csv", index_col = 0)
    print(df)
    
    print("****************")
    print(get_age(df))
    
    print("****************")
    print(get_third_name(df))
    
    print("****************")
    print(get_carol_deets(df))
    
    print("****************")
    print(get_salary_and_occupation(df))
    
    print("****************")
    print(get_age_salary_of_first_two(df))
    
    print("****************")
    print(get_occupation_bob_eve(df))
    
    
    
    
    

if __name__ == "__main__":
    main()