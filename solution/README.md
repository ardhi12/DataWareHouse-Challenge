# DWH Coding Challenge

## The Solution

1. Visualize the complete historical table view of each tables
>First, load all json files. then create a view based on the loaded table. Finally, visualize the complete historical table view of each tables.

2. Visualize the complete historical table view of the denormalized joined table
> First, join all view tables with full outer join based on timestamp column, then create a view based on the joined table. Finally, Visualize the complete historical table view of the denormalized joined table.

3. The Discussion
> Transactions that occur:  
• Credit card usage  
12000 at 2020-01-06 19:30:00  
19000 at 2020-01-08 01:00:00  
0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;at 2020-01-10 18:00:00  
37000 at 2020-01-18 22:30:00  
• Balance Changes  
15000 at 2020-01-02 16:00:00  
40000 at 2020-01-10 16:30:00  
21000 at 2020-01-10 18:00:00  
33000 at 2020-01-20 14:30:00  
Number of transactions made : **8 transactions**

## How To Use
>run command `sh Script.sh` on your terminal  
The program will run automatically in a Docker container with the container name is dwh-pyspark