# DWH Coding Challenge

## Resources

There are three tables, which are `accounts`, `cards`, and `saving_accounts`. <br>
An account can have up to one concurrent active card and one concurrent active savings_account. <br>
You are given the event logs of those tables in the respective directory name under `data` directory.

The event logs are of JSON format, and the fields definition are:

| Field | Description |
|:-----:|-------------|
| id | ID of the DB record |
| op | type of DB operation. 'c' means `create` and 'u' means `update` |
| ts | timestamp when the event happened |
| data | DB record field / value pairs. Only exists in event of type 'c' |
| set | Updated DB record field / value pairs. Only exists in event of type 'u' |

## Tasks

To do the following tasks, you probably gonna need some kinds data processing library in your own choice of programming language.
`pandas`, a data processing library in Python, is recommended due to ease of use and simplicity. However, you are free to choose
any programming language and any framework to implement the solution.

1. Visualize the complete historical table view of each tables in tabular format in stdout (hint: print your table)
2. Visualize the complete historical table view of the denormalized joined table in stdout by joining these three tables (hint: the join key lies in the `resources` section, please read carefully)
3. From result from point no 2, discuss how many transactions has been made, when did each of them occur, and how much the value of each transaction?  
   Transaction is defined as activity which change the balance of the savings account or credit used of the card
   
## Submission

To submit your tasks, simply create the necessary implementation code in given `solution` directory.
You may want make this directory a git repository and checkpoint your work periodically here.

In addition to your core logic codebase, please also include scripts to deploy your code to a Docker container.
Your code has to be deployed in **local Docker container**. Please also include the necessary files (such as `Dockerfile` and automation scripts)
to deploy and run your code inside a Docker container.

Please also include a `README.md` inside the `solution` directory to give a summary of your submitted solution,
the thinking behind your implemented solution, and how to run your solution end-to-end in a Docker container to get the desired result as stated above. 

