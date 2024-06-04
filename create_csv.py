import os
import wfdb
import pyedflib
import pandas as pd
import glob

def read_dat_file(file_path):
    signals, fields = wfdb.rdsamp(file_path)
    leads = fields['sig_name']
    return signals, leads

def read_edf_file(file_path):
    f = pyedflib.EdfReader(file_path)
    n = f.signals_in_file
    signals = [f.readSignal(i) for i in range(n)]
    leads = f.getSignalLabels()
    f._close()
    return signals, leads

def create_csv(signal_data, leads, file_path, output_dir):
    data_dict = {lead: signal_data[:, i] for i, lead in enumerate(leads)}
    df = pd.DataFrame(data_dict)
    base_name = os.path.basename(file_path)
    csv_file = os.path.join(output_dir, base_name.replace(".dat", ".csv").replace(".edf", ".csv"))
    df.to_csv(csv_file, index=False)
    print(f"Created CSV file: {csv_file}")

def process_files(local_dir):
    output_dir = os.path.join(local_dir, 'csv_files')
    os.makedirs(output_dir, exist_ok=True)
    
    for file_path in glob.glob(os.path.join(local_dir, "*")):
        if file_path.endswith(".dat"):
            signals, leads = read_dat_file(file_path.replace('.dat', ''))
            create_csv(signals, leads, file_path, output_dir)
        elif file_path.endswith(".edf"):
            signals, leads = read_edf_file(file_path)
            create_csv(signals, leads, file_path, output_dir)

local_dir = input("Enter Directory name as input (Make sure dir is same as of this file): ")
#local_dir = 'slpdb'
process_files(local_dir)
