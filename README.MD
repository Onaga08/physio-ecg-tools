## Project Title
ECG Database curation through Physionet Repository

## Project Description
[Physionet](https://physionet.org) is a repository of freely-available medical research data, managed by the MIT Laboratory for Computational Physiology. 
The aim of this repository is to allow access for ECG related research and applications in various institutions by easy access, retrieval, and conversion of all ECG databases available on Physionet.
Through the use of [WFDB](https://wfdb.readthedocs.io/en/latest/) package, we were able to access the Physionet Repository and extract all the databases containing any type of ECG data. 
Different files in this repository are created for different functions, which are explained further.

## Installation

Put the following command in your terminal/cmd after traversing to the designated folder
```bash
git clone 
```
This repository uses several Python libraries and dependencies. Install all requirements through the command below.
```bash
pip install -r requirements.txt
```
Now we are ready to run the code!

## Usage

### [main.py](main.py)
Used for extracting the ECG related databases from the Physionet Repository. 
Works my opening the urls of each dataset, extracting the first paragraph of the description or abstract (in case the description is not found) and looks for the term 'ECG' or 'Electrocardiogram'. 

Returns a csv file containing the name and description of the databases of interest.

### [Datapoints.py](Datapoints.py)
Traverses through the csv created by [main](main.py) to access the records of each databases. 
Useful in appending the number of datapoints recorded in each database of interest.

### [download_db.py](download_db.py)
Used to download the dataset required. 
#### Note - Requires dataset code as input in terminal

### [plot.py](plot.py)
Used to plot every .dat or .edf included in the directory given as argument. Creates a subfolder of .png files.
#### Note - Requires Directory name as input in terminal

### [create_csv.py](create_csv.py)
Final Runnable. 
Useful in extracting signal amplitudes of all the signals present in each .dat or .edf file in the database. 
Creates a subdirectory of the .csv files. 
#### Note - Requires Directory name as input in terminal

## Example Usage 
### For example usage, go to [Tests](Tests/trial.txt)

## Contributions
Pull Requests are welcome. 
For major changes, please discuss in issues first. 

## Made specially for ECG related research at Biomedical Department of NIT Rourkela

