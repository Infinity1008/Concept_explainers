import sys
import pandas as pd
import matplotlib.pyplot as plt


### Define a function to validate the column names and number

# This function takes a dataframe as an input and returns true is all the columns in the dataframe are in the list or not. 
def validate_table_names(df):
    col_names = ['default','amount','grade','years','ownership','income','age']
    num_cols = len(col_names)

    # Setting the flag to be true by default
    flag = True

    # Step 1
    # Checking if column names are correct or not.
    for name in df.columns:
        if name not in col_names:
            # If column name not found, then setting the flag to be false.
            # If columns name found. Leaving it as it is.
            flag = False
            break

    # Step 2, is checking if there are 7 columns or not.
    # Checking if share of data is right
    if num_cols!=df.shape[1]:
        flag = False

    return flag




### Define a function to validate the categorical levels    
def validate_levels_cat(df):
    grade_validation = ['A','B','C','D','E','F','G']
    ownership_validation = ['MORTGAGE','OTHER','OWN','RENT']
    g_val = False
    o_val = False
    
    # Checking if there is something out of our expected categories
    if set(df['grade'].unique()).issubset(set(grade_validation)):
        g_val = True
    
    if set(df['ownership'].unique()).issubset(set(ownership_validation)):
        o_val = True
        
    # Checking if both are true or not
    if g_val and o_val:
        return True
    else:
        return False
    
#### Function to create exploration plots
def create_deciles(df):
    df['amount_deciles'] = pd.qcut(df['amount'],10,labels=False)
    df['income_deciles'] = pd.qcut(df['income'],10,labels=False)
    df['age_deciles'] = pd.qcut(df['age'],10,labels=False)
    return df


def create_exploration_plots(df):
    cols = ['amount_deciles','income_deciles','age_deciles','grade','ownership']
    for col in cols:
        df.groupby(col)['default'].mean().plot()
        plt.savefig(f'./plots/{col}.pdf')
        plt.show()



# Reading my csv
df = pd.read_csv(sys.argv[1])


if validate_table_names(df) and validate_levels_cat(df): 
    print("The columns and categories of my dataframe are correct and in order")

    # Creating/Appending the deciles column
    df = create_deciles(df)

    # Let's save some plots
    create_exploration_plots(df)
else:
    print("There is something wrong with your dataset")






