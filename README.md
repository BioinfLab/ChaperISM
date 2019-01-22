# ChaperISM

## Name
ChaperISM

## Version
v 1.0

## Description
ChaperISM is an algorithm to identify Hsp70 binding sequences in proteins. It uses a position-independent scoring matrix which was trained on either qualitative or quantitative chemiluminescence data previously published, obtained from interaction between DnaK and different ligands. Both versions of ChaperISM, qualitative or quantitative, resulted in an improved performance in comparison to other state-of-the-art chaperone binding predictors.

## System requirements
The user must have Python 3 installed to run ChaperISM.

## Installation
ChaperISM does not require any type of installation. Just download the files into a working directory, unzip/untar (if necessary, and run according to "Usage" below.

## Usage
After downloading the files, open a Terminal window and run the following:
```
python ChaperISM.py fasta_file [-h] [-qt] [-ql] [-qt_cutoff] [-ql_cutoff] [--version] 
```

The "fasta_file" and "qt" or "ql" arguments are mandatory. All arguments are defined below: 

- fasta_file                    Text file containing protein sequences in fasta format.
- -h, --help                    Show this help message and exit
- -qt                           Quantitative prediction mode.
- -ql                           Qualitative prediction mode.
- -qt_cutoff , --qt_cutoff      Cutoff for quantitative mode predictions.
- -ql_cutoff , --ql_cutoff      Cutoff for qualitative mode predictions.
- --version                     Show program's version number and exit


## Files list

## Contact information


