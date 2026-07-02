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
        #optimize memory usage by converting object types to category types
        
         
        df = df.where(pd.notnull(df), None)
        logging.info(f"Dataframe created with shape: {df.shape}")
        return df