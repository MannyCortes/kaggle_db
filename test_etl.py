import pytest 
import pandas as pd 
import data_pipeline
import db_sub


def test_regex_cleaning():
    mock_data = {
        'user_id': ['U123456', 'U12', 'X999999'],        # Row 2 is too short, Row 3 has wrong letter
        'price': ['25.50', '25.50', 'FREE'],             # Row 3 is a word, not a number
        'delivery_status': ['Delayed', 'FakeStatus', 'Delayed'] # Row 2 is an unauthorized enum
    }
    df = pd.DataFrame(mock_data).astype(str)
    clean_df = data_pipeline.regex_cleaning(df)
    assert len(clean_df) == 1
    assert clean_df.iloc[0]['user_id'] == 'U123456'