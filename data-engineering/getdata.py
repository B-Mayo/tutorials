import os
import io
import pandas as pd

# Extract the data and save to file
def df_to_pickle (s):
    orig_data=pd.read_csv(io.StringIO(s.decode('utf-8')))
    orig_data.columns = ['age','workclass','fnlwgt','education_level','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','income']
    base_data_dir = os.path.join(os.getcwd(), 'data')
    os.makedirs(base_data_dir, exist_ok=True)
    censusdata_dir = os.path.join(base_data_dir, 'Adult.data')
    orig_data.to_pickle(censusdata_dir)
    
