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
After downloading the files, open Terminal and run the following:
```
python ChaperISM.py fasta_file [-h] [-qt] [-ql] [-qt_cutoff] [-ql_cutoff] [--version] 
```

The "fasta_file" and "qt" or "ql" arguments are mandatory. All arguments are defined below: 

- fasta_file: text file containing protein sequences in fasta format.
- -h, --help: show a help message and exit.
- -qt: quantitative prediction mode.
- -ql: qualitative prediction mode.
- -qt_cutoff , --qt_cutoff: cutoff for quantitative mode predictions.
- -ql_cutoff , --ql_cutoff: cutoff for qualitative mode predictions.
- --version: show program's version number and exit

## Output
In case 


--------------------------------------------
Sequence: name (optional)
--------------------------------------------
POSITION    HEPTAMER      SCORE     BINDER
--------------------------------------------
    0        KIYRLAI      3.330171     *    
    1        IYRLAIR      3.365994     *    
    2        YRLAIRT      3.239968     *    
--------------------------------------------



## Files list

## Contact information
For more details, please contact Mauricio Menegatti Rigo,PhD (mauricio.rigo@pucrs.br) or Matheus de Bastos Balbé e Gutierres, BSc (matheusbgutierres@gmail.com).


