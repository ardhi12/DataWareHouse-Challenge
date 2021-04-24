# DWH Coding Challenge

## The Solution

1. Visualize the complete historical table view of each tables
>The first thing to do is check and retrieve all directory names, then extract the data of all json files located in each directory. After that the extract results are converted into the dataframe. Display the results of each table in tabular format.

2. Visualize the complete historical table view of the denormalized joined table
>The dataframe of each table generated in the above step is merged using concat, sort values by timestamp and DB operation and set column 'id' as index. The merge is done in order to denormalize and get the sequence of events that occurred. Result of denormalization displayed in tabular format.

3. Filter dataframe
> Filter based on unique id and key column that is not null to get rows containing transactions such as balance changes or credit usage

4. Transform transactions
> A few steps are performed:     
• Merge list transactions using concat by giving keys to see which rows are coming from which dataframe. then reset index.  
• Add `datetime` column by converting timestamps to datetime format  
• Add `value` column and fill row with balance and credit_used  
• Drop id, data, op, ts, and set columns  
• Rename `level_0` column (key column) to `source`

5. The Information
> • How many transactions has been made?  
Transactions has been made : 8 Transactions  
• when did each of them occur?  
Displayed in the table  
• how much the value of each transaction?  
Displayed in the table