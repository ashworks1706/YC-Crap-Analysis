# Utility script for data download/processing

import kagglehub
from kagglehub import KaggleDatasetAdapter


def download_yc_data():
    # Set the path to the file you'd like to load
    file_path = "ycombinator_all_companies.csv"

    # Load the latest version
    df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "sashakorovkina/ycombinator-all-funded-companies-dataset",
    file_path,
    # Provide any additional arguments like 
    # sql_query or pandas_kwargs. See the 
    # documenation for more information:
    # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
    )

    print("First 5 records:", df.head())
    for index, row in df.iterrows():
        print(f"Record {index}: {row.to_dict()}")

if __name__ == "__main__":
    download_yc_data()
