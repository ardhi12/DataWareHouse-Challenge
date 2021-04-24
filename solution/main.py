# import packages
from IPython.display import display
import pandas as pd
import glob
import json
import os

# functions
def extract_json(source):
    """
    This function is used to get data from the event log
    """
    # retrieve all json files by source folder
    source = glob.glob("data/"+source+"/*.json")    
    combined_results = []
    for file in source:
        # open the json file
        f = open(file, "r")
        # append the data to list
        combined_results.append(json.load(f))    
    # convert combined_results list to DataFrame and return it
    return pd.DataFrame(combined_results)

def complete_historical():
    """
    This function is used to get the list of source directories and 
    display the complete history of the table
    """
    df_list = []
    # get directories
    my_dir = os.listdir("data")
    for dir in my_dir:
        # get the dataframe of table
        df_dir = extract_json(dir)
        # display the visualization        
        print(f"Visualization of {dir} table")        
        display(df_dir)
        print("")
        # append each dataframe to list
        df_list.append(df_dir)
    return df_list

def main():
    # Visualize the complete historical table view of each tables
    historical_each_tables = complete_historical()
    

if __name__ == "__main__":
    main()