## Testing the repository by extracting and downloading ANSI/AAMI EC13 Test Waveforms dataset

#### Main.py and Datapoints.py are generalized to create a csv of all ecg datasets, thus are excluded from this test.

## download_db.py 
### argument given - aami-ec13
### output - //Created a dir named "aami-ec13" containing all the files hosted on this database on Phyionet.org

## plot.py
### argument given - aami-ec13
### output - //Created a subdir named "png_files" containing .png files of all the .dat/.enf files present in the database

## create_csv.py
### argument given - aami-ec13
### output - //Created a subdir named "csv_files" containg .csv files of all the .dat/.enf files present in the database