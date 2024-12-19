import pandas as pd

# Load the source and target CSV files into DataFrames
empsrc = pd.read_csv('../Data1/empsrc.csv')
emptgt = pd.read_csv('../Data1/emptgt.csv')

# Find rows in empsrc that are not in emptgt
not_in_tgt = empsrc.merge(emptgt, indicator=True, how='outer').query('_merge == "left_only"').drop('_merge', axis=1)

# Find rows in emptgt that are not in empsrc
not_in_src = empsrc.merge(emptgt, indicator=True, how='outer').query('_merge == "right_only"').drop('_merge', axis=1)

# Combine the results
non_matching_records = pd.concat([not_in_tgt, not_in_src])

print(non_matching_records)

# Write non-matching records to an Excel file
#non_matching_records.to_excel('non_matching_records.xlsx', index=False)



#print("Non-matching records have been written to 'non_matching_records.xlsx'.")