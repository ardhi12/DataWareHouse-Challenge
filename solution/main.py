from pyspark.sql import SparkSession
from pyspark.sql import functions

if __name__ == "__main__":
    # Create a SparkSession # provide the cluster information unless running on local system.
    spark = SparkSession.builder.master("local[*]").appName("dwh").getOrCreate()

    # load, create and visualize views from Accounts
    accountsDF = spark.read.json('data/accounts/*.json')
    accountsDF.createOrReplaceTempView("accountsView")
    spark.sql("select * from accountsView").show()
    
    # load, create and visualize views from Cards
    cardsDF = spark.read.json('data/cards/*.json')
    cardsDF.createOrReplaceTempView("cardsView")
    spark.sql("select * from cardsView").show()
    
    # load,create and visualize views from Savings accounts
    savings_accountsDF = spark.read.json('data/savings_accounts/*.json')
    savings_accountsDF.createOrReplaceTempView("savings_accountsView")
    spark.sql("select * from savings_accountsView").show()
    
    # create denormalized joined table view
    denormalized = spark.sql(
            "SELECT A.ts as A_ts, A.id as A_id, A.op as A_op, A.data as A_data, A.set as A_set, B.ts as B_ts, B.id as B_id, B.op as B_op, B.data as B_data, B.set as B_set, C.ts as C_ts, C.id as C_id, C.op as C_op, C.data as C_data, C.set as C_set FROM accountsView A FULL JOIN cardsView B ON B.ts = A.ts FULL JOIN savings_accountsView C ON C.ts = A.ts").cache()
    denormalized.createOrReplaceTempView("denormalizedView")
    spark.sql("select * from denormalizedView").show(truncate=False)
    
    # convert millis to datetime
    denormalized = denormalized.withColumn("A_datetime", functions.to_utc_timestamp(functions.from_unixtime(functions.col("A_ts")/1000,'yyyy-MM-dd HH:mm:ss'),'UTC'))
    denormalized = denormalized.withColumn("B_datetime", functions.to_utc_timestamp(functions.from_unixtime(functions.col("B_ts")/1000,'yyyy-MM-dd HH:mm:ss'),'UTC'))
    denormalized = denormalized.withColumn("C_datetime", functions.to_utc_timestamp(functions.from_unixtime(functions.col("C_ts")/1000,'yyyy-MM-dd HH:mm:ss'),'UTC'))
    
    # get transactions
    denormalized.select("B_datetime","B_set.credit_used","C_datetime","C_set.balance").filter("B_set.credit_used is not null OR C_set.balance is not null").sort("B_datetime","C_datetime").show()