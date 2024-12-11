import pandas as pd
import pytest


# Load the source and target CSV files into DataFrames
def test_empDataTocsv():
    df_empsrc1 = pd.read_csv('H:\pythonprojects\myProj\Data1\empsrc1.csv')
    df_emptgt1 = pd.read_csv('H:\pythonprojects\myProj\Data1\emptgt1.csv')

    # Find rows in empsrc that are not in emptgt
    not_in_tgt = df_empsrc1.merge(df_emptgt1, indicator=True, how='outer').query('_merge == "left_only"').drop('_merge', axis=1)

    # Find rows in emptgt that are not in empsrc
    not_in_src = df_empsrc1.merge(df_emptgt1, indicator=True, how='outer').query('_merge == "right_only"').drop('_merge', axis=1)

    # Combine the results
    non_matching_records = pd.concat([not_in_tgt, not_in_src])

    print(non_matching_records)

    output_file = 'H:/pythonprojects/myProj/TestResult_Output/non_matching_records.csv'

    # Write non-matching records to an Excel file
    non_matching_records.to_csv(output_file, index=False)

    assert non_matching_records.empty, "DataFrames are not matching. Differences saved to file."

#print("Non-matching records have been written to 'non_matching_records.xlsx'.")
