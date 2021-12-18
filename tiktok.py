from TikTokApi import TikTokApi as tiktok
import json
import pandas as pd
from helpers import process_results
import sys



def get_data(hashtag):

# Get cookie data
    verifyFp = "verify_kx709c39_8EDXhF4K_avtS_4pOi_B3Du_Uq8eTJyLPRVN"

    # setup instnace
    api = tiktok.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

    # Get data by hastag
    trending = api.by_hashtag(hashtag)
    # Process data
    flattened_data = process_results(trending)

    # Conver preprocess data to a dataframe
    df = pd.DataFrame.from_dict(flattened_data, orient='index')
    df.to_csv('tiktokdata.csv', index=False)

if __name__ == '__main__':
    get_data(sys.argv[1])