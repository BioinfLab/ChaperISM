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
- -qt_cutoff , --qt_cutoff: cutoff for quantitative mode predictions (default is 2.7)
- -ql_cutoff , --ql_cutoff: cutoff for qualitative mode predictions (default is 0.2)
- --version: show program's version number and exit

## Output
After running, a message will be shown in the Terminal with the name of the sequence (optional, defined by the user inside the fasta file) and a table, which include the following columns:
- Position: position of the heptamer in the sequence provided.
- Heptamer: heptamer sequence
- Score: binding score
- Binder: this column will be filled with an asterisk if the sequence is predicted as binder. For quantitative mode prediction (-qt) the cutoff is 2.7. For qualitative mode prediction (-ql) the cutoff is 0.2.

An output example is given in Figure 1 and Figure 2
![image](https://user-images.githubusercontent.com/43217682/51554466-893fe000-1e5c-11e9-83d2-d962255fe124.png)
***Figure 1***. Results after ChaperISM prediction using quantitative mode prediction (-qt)

![image](https://user-images.githubusercontent.com/43217682/51554627-d7ed7a00-1e5c-11e9-9f39-5a1e629771d0.png)
***Figure 2***. Results after ChaperISM prediction using qualitative mode prediction (-ql)


## Files list

## Contact information
For more details, please contact Mauricio Menegatti Rigo,PhD (mauricio.rigo@pucrs.br) or Matheus de Bastos Balbé e Gutierres, BSc (matheusbgutierres@gmail.com).


