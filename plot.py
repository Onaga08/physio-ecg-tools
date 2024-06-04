import os
import wfdb
import pyedflib
import matplotlib.pyplot as plt
import glob

def read_dat_file(file_path):
    record = wfdb.rdrecord(file_path)
    signals = record.p_signal
    leads = record.sig_name
    return signals, leads

def read_edf_file(file_path):
    f = pyedflib.EdfReader(file_path)
    n = f.signals_in_file
    signals = [f.readSignal(i) for i in range(n)]
    leads = f.getSignalLabels()
    f._close()
    return signals, leads

def plot_waveforms(signal_data, leads, file_path, output_dir):
    num_leads = len(leads)
    fig, axes = plt.subplots(num_leads, 1, figsize=(12, 8), sharex=True)
    
    if num_leads == 1:
        axes = [axes]
    
    for i, ax in enumerate(axes):
        ax.plot(signal_data[:, i])
        ax.set_title(leads[i])
        ax.set_ylabel('Amplitude')
        ax.grid()
    
    axes[-1].set_xlabel('Time (samples)')
    
    plt.tight_layout()
    base_name = os.path.basename(file_path)
    plot_file = os.path.join(output_dir, base_name.replace(".dat", ".png").replace(".edf", ".png"))
    plt.savefig(plot_file)
    plt.close()
    print(f"Created plot file: {plot_file}")

def process_files(local_dir):
    output_dir = os.path.join(local_dir, 'png_files')
    os.makedirs(output_dir, exist_ok=True)
    
    for file_path in glob.glob(os.path.join(local_dir, "*")):
        if file_path.endswith(".dat"):
            signals, leads = read_dat_file(file_path.replace('.dat', ''))
            plot_waveforms(signals, leads, file_path, output_dir)
        elif file_path.endswith(".edf"):
            signals, leads = read_edf_file(file_path)
            plot_waveforms(signals, leads, file_path, output_dir)

local_dir = input("Enter dir name (make sure dir exists in the same dir as this .py file): ")
#local_dir = 'slpdb'
process_files(local_dir)
