import os 
import logging
import pandas as pd
def pandas_df(folder_path):
    folder = os.listdir(folder_path)
    #returns a list of directories in the local folder
    for file_name in folder:
        #grab file names from folder
        if file_name.endswith(".csv"):
            cols = ["user_id", "product_id", "category", "subcategory", 
                    "brand", "price", "discount", "final_price", 
                    "rating", "review_count", "stock", "seller_id", 
                    "seller_rating", "purchase_date", "shipping_time_days", "location", 
                    "device", "payment_method", "is_returned", "delivery_status"]
        #create new file path joining folder+file
        final_path = os.path.join(folder_path, file_name)
        #read the csv file into a pandas dataframe using the specified columns
        df = pd.read_csv(final_path, usecols=cols)
        #where keeps whatever returns true and replaces false with None
        df = df.where(pd.notnull(df), None)
        logging.info(f"Dataframe created with shape: {df.shape}")
        return df
    
def optimize_memory(df):
    #pandas defaults to 64bit/8byte data types, its best to downsize for optimization
    # int/bit 8 = 256 or -128 to 127. every bit doubles from the previous one 
    #example 4 bits goes 1, 2, 4, 8 and can represent 0-15 meaning 16 total
    try:
        columns = df.columns.tolist()
        for col in columns:
            d_type = str(df[col].dtype).lower()
            #strings/object data types use 64 bit pointers to point to the string in memory
            #if unique/total row is around 50% using 'category' creates a look up table,
            # the with an integer-key, the integer is storedon the table rather than a pointer  
            if d_type == "object":
                #counts unique strings
                unique_str = df[col].nunique()
                #how many rows foreach column
                total_rows = len(df[col])
                if unique_str/total_rows < 0.5:
                    df[col] = df[col].astype('category')
            #pandas has several int tpes
            elif "int" in d_type:
                df_min = df[col].min()
                # if no negatives in the column we can use 
                if df_min >= 0:
                    #pandas calculates the needed int size
                    # to_numeric creates a replica column with adjusted downcast, the headers(pointers) points to the new column
                    #since pandas likes to group all the same data types together, it will move the new column to the front of mathing "blocks"
                    df[col] = pd.to_numeric(df[col], downcast='unsigned')
                else: df[col] = pd.to_numeric(df[col], downcast='integer')
            elif "float" in d_type:
                df[col]= pd.to_numeric(df[col], downcast='float')
        return df
    except Exception as e:
        logging.error(f"An error occurred during memory optimization: {e}")


def regex_cleaning(df):
    #returns a list of all column names
    columns = df.columns.tolist()
    for col in columns:
        #using pandas&regex allows for column by column checking rather than python looping through every row
        invalid = df[col].str.contains

