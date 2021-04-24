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

def denormalized_table(historical_each_table):
    """
    This function is used to denormalize joined table
    """
    # joining tables using concat, sort values by timestamp and DB operation
    # and set column 'id' as index
    data_frames = pd.concat(historical_each_table, axis=0).sort_values(by=['ts','op']).set_index('id')
    # display the visualization
    print(f"Visualization of the denormalized joined table")        
    display(data_frames)
    print("")
    return data_frames

def get_transactions(data_frames):
    """
    This function is used to filter the DataFrame to get a list of transactions
    """
    filter_trx = []
    # get list of unique values from column 'id' / index
    list_unique_id = data_frames.index.unique().tolist()
    # remove first index of list
    list_unique_id.pop(0)    
    for unique_id in list_unique_id:
        # set the key
        key = 'balance'
        if 'c' in unique_id:
            key = 'credit_used'
        # filter based on unique id and key column that is not null
        trx = data_frames[(data_frames.index.str.contains(unique_id)) & (data_frames['set'].apply(pd.Series)[key].notnull())]
        # append each transaction
        filter_trx.append(trx)
    return filter_trx

def main():
    # Visualize the complete historical table view of each tables
    historical_each_tables = complete_historical()
    
    # Visualize the complete historical table view of the denormalized joined table
    data_frames = denormalized_table(historical_each_tables)    

    # get transactions
    get_transactions(data_frames)

if __name__ == "__main__":
    main()