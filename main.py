import kagglehub
import logging 
import os
from dotenv import load_dotenv
import kagglehub
import data_pipeline
#loads local env fille into local disk/memory OS
load_dotenv()
logging.basicConfig(filename="pipeline.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
# recourse https://github.com/Kaggle/kagglehub/blob/main/README.md#download-dataset
#look for datasetAdapter
#downloads dataset, if no download needed returns the local folder path
def main():
    try:
        path = kagglehub.dataset_download("sharmajicoder/amazon-e-commerce")
        #return a pandas df
        df = data_pipeline.pandas_df(path)
        print(df)
    except Exception as e:
        logging.
if __name__ == "__main__":
    main()