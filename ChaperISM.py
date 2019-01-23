#!/usr/bin/env python3

def runMat(pep,mat,offset):
	ret = 0.0
	for aa in pep:
		for x in range(7):
			ret += mat[aa][x]
	return ret+offset

def Predict_Quantitative_Mode(dict_seq, cutoff):
	Quantitative_offset = 0.718675619345
	Quantitative_PISM = {'A': [ 0.14567794,  0.04818767,  0.00665627,  0.03211395, -0.03437073,
		0.01161968,  0.04473559], 'C': [-0.27159421, -0.0557392 ,  0.06694989,  0.08702948,  0.17277077,
		0.02670373,  0.11699927], 'E': [ 0.02432079, -0.19143726,  0.09043395, -0.00547146,  0.08613284,
		0.08931813, -0.01525396], 'D': [ 0.09261986, -0.20611353,  0.18241395,  0.23323361,  0.0322968 ,
	       -0.1602488 , -0.07734232], 'G': [ 0.18166801,  0.0677326 ,  0.08549923, -0.11143995,  0.02749219,
	       -0.01828263, -0.05495244], 'F': [-0.08476179,  0.01291043, -0.14470299,  0.03835858,  0.19123185,
		0.25543387,  0.1412575 ], 'I': [ 0.09966293,  0.04018111,  0.08091449,  0.18619379, -0.06136536,
	       -0.01562306,  0.00960857], 'H': [ 0.00316637,  0.00750568,  0.19636926,  0.31979451, -0.24088565,
	       -0.03876962,  0.04646512], 'K': [-0.23378948,  0.2867628 ,  0.18598707,  0.33846578, -0.10755751,
	       -0.07887614,  0.00537582], 'M': [-0.01943432, -0.35576367,  0.01043346,  0.26776317,  0.01824333,
	       -0.0335918 ,  0.19372862], 'L': [ 0.01698865, -0.00245294,  0.07489881, -0.02496723,  0.09667284,
		0.15280091,  0.06608233], 'N': [ 0.0287688 , -0.07050698, -0.03589367,  0.06284256,  0.29931243,
	       -0.35191582,  0.18299936], 'Q': [ 0.2429028 ,  0.05286953, -0.07631991,  0.38173389, -0.25212546,
	       -0.06763125, -0.06460735], 'P': [-0.05989859, -0.02136846,  0.35385948,  0.05360025, -0.40683524,
		0.07202069,  0.13091775], 'S': [ 0.07414246,  0.1579762 ,  0.1366677 , -0.0164196 , -0.01573084,
	       -0.02185597, -0.13289645], 'R': [-0.23890815,  0.01013346,  0.18307768, -0.11263621,  0.07725322,
		0.00154875,  0.51172313], 'T': [ 0.14647671,  0.15445086, -0.17685725,  0.13509232,  0.04916194,
	       -0.16912927,  0.07435063], 'W': [-0.06549715, -0.02080303, -0.0776952 ,  0.19539848, -0.05207484,
		0.13122955,  0.17026478], 'V': [-0.06888999, -0.00099641,  0.17202196,  0.12998881, -0.00490603,
	       -0.03911565,  0.16087556], 'Y': [ 0.05127709, -0.14511197,  0.22904897,  0.06417733,  0.30099858,
	       -0.29971149,  0.26846789]}
	for key in dict_seq:
		print ("--------------------------------------------")
		print ('Sequence: '+key[1:])
		print ("--------------------------------------------")
		print ('{:^10s}{:^14s}{:^12s}{:^8s}'.format('POSITION','HEPTAMER','SCORE','BINDER'))
		print ("--------------------------------------------")
		if len(dict_seq[key])>=7:
			for x in range(0,len(dict_seq[key])-6,1):
				heptamer = dict_seq[key][x:x+7]
				pred = runMat(heptamer, Quantitative_PISM, Quantitative_offset)
				if pred >= cutoff:
					print('{:^10s}{:^14s}{:^12f}{:^8s}'.format(str(x),heptamer,pred,'*'))
				else:
					print('{:^10s}{:^14s}{:^12f}{:^8s}'.format(str(x),heptamer,pred,' '))
		else:
			print ("Error: sequences must have at least 7 residues.")
		print ("............................................")


def Predict_Qualitative_Mode(dict_seq, cutoff):
	Qualitative_offset = 0.338948385187
	Qualitative_PISM = {'A': [ 0.02772892,  0.03356412, -0.02744794,  0.0080969 ,  0.02334192,
		0.01645188, -0.13455583], 'C': [-0.24235566, -0.01903083, -0.09021362,  0.04371711, -0.04020911,
		0.31587864, -0.15347501], 'E': [-0.35465806,  0.0237687 , -0.00436671,  0.01545498, -0.07661303,
		0.13557834,  0.13511838], 'D': [ 0.0767015 , -0.06191465, -0.00559435, -0.06172027, -0.06450202,
	       -0.01409912, -0.00461297], 'G': [-0.1504576 ,  0.24528891,  0.07361844, -0.00875046, -0.05624849,
	       -0.25068289,  0.0293025 ], 'F': [ 0.12160976,  0.00636235,  0.04975532,  0.14426455,  0.02620517,
	       -0.31180097,  0.01742275], 'I': [ 0.07188344,  0.20029367, -0.12232473, -0.05398928, -0.05112162,
		0.00709132, -0.00024804], 'H': [-0.00268762,  0.19977328, -0.12452675,  0.13262339,  0.02067887,
	       -0.21479675, -0.03232428], 'K': [-0.0571738 , -0.06999147, -0.07328753, -0.08291864,  0.29446825,
	       -0.04887253,  0.05478155], 'M': [-0.21811674,  0.01953522,  0.10066954,  0.02882645,  0.00856765,
	       -0.02182938, -0.01243941], 'L': [-0.14063142, -0.15101234,  0.07858373, -0.16538822,  0.01463639,
		0.24639886,  0.16340288], 'N': [ 0.04451703, -0.00365936,  0.0359383 ,  0.08069534,  0.07544078,
		0.03416336, -0.3420097 ], 'Q': [-0.15124991,  0.19934364, -0.25529933,  0.22905532, -0.01351096,
	       -0.1447299 ,  0.08011651], 'P': [-0.04639463,  0.07141876, -0.07508624, -0.15279673, -0.02282322,
	       -0.00040518,  0.16872326], 'S': [ 0.06522657, -0.0322716 ,  0.11654486,  0.04817205,  0.01227283,
	       -0.1620065 , -0.12222886], 'R': [ 0.08174114,  0.17448505,  0.13144211,  0.08108816,  0.09652098,
	       -0.34829205, -0.15009949], 'T': [-0.02624565,  0.03703667, -0.23490104,  0.25541162, -0.02152624,
		0.00726724, -0.08737065], 'W': [-0.00556008, -0.02658188,  0.10839476,  0.043646  , -0.03391185,
	       -0.01360189,  0.07059761], 'V': [ 0.20890139,  0.17162778, -0.08398686, -0.05902733, -0.0153962 ,
		0.00423243, -0.20616401], 'Y': [-0.09355195,  0.01138308, -0.09335642,  0.08862024, -0.03539316,
		0.0206736 ,  0.22008913]}
	for key in dict_seq:
		print ("--------------------------------------------")
		print ('Sequence: '+key[1:])
		print ("--------------------------------------------")
		print ('{:^10s}{:^14s}{:^12s}{:^8s}'.format('POSITION','HEPTAMER','SCORE','BINDER'))
		print ("--------------------------------------------")
		if len(dict_seq[key])>=7:
			for x in range(0,len(dict_seq[key])-6,1):
				heptamer = dict_seq[key][x:x+7]
				pred = runMat(heptamer, Qualitative_PISM, Qualitative_offset)
				if pred >= cutoff:
					print('{:^10s}{:^14s}{:^12f}{:^8s}'.format(str(x),heptamer,pred,'*'))
				else:
					print('{:^10s}{:^14s}{:^12f}{:^8s}'.format(str(x),heptamer,pred,' '))
		else:
			print ("Error: sequences must have at least 7 residues.")
		print ("............................................")

def check_seq(string):
	allowed = ('A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y','\t',' ','\n')
	string = string.upper()
	for char in string:
		if char in allowed:
			pass
		else:
			return 1
	return 0

def check_fasta_consistence(string):
	# Return 0 or 1
	with open(string,'r') as F:
		txt = F.read()
	txtsplt = txt.split('>')
	for elem in txtsplt:
		elemsplt = elem.split('\n')
		for x in range(1,len(elemsplt),1):
			if check_seq(elemsplt[x]) == 0:
				pass
			else:
				print ("ChaperISM could not process the following line:")
				print (elemsplt[x])
				return 1
	return 0

def check_consistence(Args):
	fasta_flag = check_fasta_consistence(Args.fasta_file)
	return fasta_flag


def process_header(string):
	return '>'+string

def extract_sequences(string):
	dictRet = {}
	cont_rename = 1
	with open(string,'r') as F:
		txt = F.read()
	txtsplt = txt.split('>')
	index_to_remove = []
	for x in range(len(txtsplt)):
		aux = txtsplt[x].strip(' ')
		aux = aux.strip('\t')
		aux = aux.strip('\n')
		if len(aux) == 0:
			index_to_remove.append(x)
	cont_aux = 0
	for el in index_to_remove:
		del txtsplt[el-cont_aux]
		cont_aux+=1
	for elem in txtsplt:
		elemsplt = elem.split('\n')
		if len(elemsplt) > 0: 
			Key = process_header(elemsplt[0])
			Value = ""
			for x in range(1,len(elemsplt),1):
				seq = elemsplt[x].upper()
				seq = seq.replace(' ','')
				seq = seq.replace('\t','')
				seq = seq.replace('\n','')
				Value = Value + seq
			if Key not in dictRet:
				dictRet.update({Key:Value})
			else:
				print ('ChaperISM renamed sequences with the same header.')
				dictRet.update({Key+'_'+str(cont_rename):Value})
				cont_rename+=1
	return dictRet
	
def Main():

	# Arguments Processing
	import argparse
	parser = argparse.ArgumentParser(description="ChaperISM: A position-independent scoring matrix for chaperone binding prediction.")
	parser.add_argument('fasta_file', metavar="fasta_file", help='Text file containing protein sequences in fasta format.')
	parser.add_argument('-qt',action='store_true', help='Quantitative prediction mode.')
	parser.add_argument('-ql',action='store_true',  help='Qualitative prediction mode.')
	parser.add_argument('-qt_cutoff','--qt_cutoff', type=float, metavar='', default=2.7, help='Cutoff for quantitative mode predictions.')
	parser.add_argument('-ql_cutoff','--ql_cutoff', type=float, metavar='', default=0.2, help='Cutoff for qualitative mode predictions.')
	parser.add_argument('--version', action='version', version='1.0')
	args = parser.parse_args()
	string_inform = "\n\n############################################\n"
	string_inform = string_inform + "#                                          #\n"
	string_inform = string_inform + "#                ChaperISM                 #\n"
	string_inform = string_inform + "#                                          #\n"
	string_inform = string_inform + "############################################\n"
	print (string_inform)	
	print ('Processing input file')
	if check_consistence(args) == 1:
		pass # Inform error
	else:
		pass # Run Prediction
		dict_seq = extract_sequences(args.fasta_file)
		print ('Running predictions')
		print ("............................................")
		if args.qt == True:
			string_inform = "############################################\n"
			string_inform = string_inform + "#                                          #\n"
			string_inform = string_inform + "#        Quantitative mode prediction      #\n"
			string_inform = string_inform + "#                                          #\n"
			string_inform = string_inform + "############################################\n"
			print (string_inform)
			Predict_Quantitative_Mode(dict_seq,args.qt_cutoff)
		if args.ql == True:
			string_inform = "############################################\n"
			string_inform = string_inform + "#                                          #\n"
			string_inform = string_inform + "#        Qualitative mode prediction       #\n"
			string_inform = string_inform + "#                                          #\n"
			string_inform = string_inform + "############################################\n"
			print (string_inform)
			Predict_Qualitative_Mode(dict_seq,args.ql_cutoff)
		if args.ql == False and  args.qt == False:
			print ('Missing argument: select a prediction mode with -qt or -ql flag.')

# Main program

if __name__ == "__main__":
	Main()


