import os

#Reading user inut file
fasta = input("Enter fasta file of DNA sequence: ")

def get_filehandle(infile):
    seqs = []
    headers = []
    with open(infile) as f:
        sequence = ""
        header = None
        for line in f:
            if line.startswith('>'):
                headers.append(line[1:-1])
                if header:
                    seqs.append([sequence])
                sequence = ""
                header = line[1:]
            else:
                sequence += line.rstrip()
        seqs.append(sequence)
    return headers, seqs
def get_fasta_lists():
    get_fasta_lists.headers, get_fasta_lists.seqs = get_filehandle(fasta)
    

get_fasta_lists()
headers = get_fasta_lists.headers
seqs = get_fasta_lists.seqs
seqss = [seqs]
flat_seqs = [item for sublist in seqss for item in sublist]
sequence_flat = ''.join(flat_seqs)
def DNA_com(instring):
    # will count upper and lower case sequences, if do not want lower case remove .upper()
    g = instring.count('G') 
    c = instring.count('C')
    a = instring.count('A')
    t = instring.count('T')
    n = instring.count('N')
    #fline = '''Accession     A's   G's    C's    T's   N's '''
    #print(fline)
    print('A: ', a, 'T: ',t, 'G: ',g, 'C: ', c, 'N: ',n)

def AT_con(instring):
    # will count upper and lower case sequences, if do not want lower case remove .upper()
    a = instring.count('A')
    t = instring.count('T')
    length = len(instring)
    AT = a+t
    at = (AT/length)*100
    fline = '''AT percentage '''
    print(fline)
    print(at)

def GC_con(instring):
    # will count upper and lower case sequences, if do not want lower case remove .upper()
    g = instring.count('G') 
    c = instring.count('C')
    length = len(instring)
    per = g+c
    gc = (per/length)*100
    fline = '''GC percentage '''
    print(fline)
    print(gc)
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
seq = ''.join(seqs)
complementss = "".join(complement.get(base, base) for base in seq)
reverse_complement = "".join(complement.get(base, base) for base in reversed(seq))

options = ['Calculate_DNA_composition', 'Calculate AT content', 'Calculate GC content','Compliment DNA', 'Reverse Compliment']

user_input = ''

input_message = "Pick an option:\n"

for index, item in enumerate(options):
    input_message += f'{index+1}) {item}\n'

input_message += 'Your choice: '
#print(DNA_com(sequence_flat))
while user_input not in map(str, range(1, len(options) + 1)):
    user_input = input(input_message)
    if int(user_input) == 1:
        DNA_com(sequence_flat)
    elif int(user_input) == 2:
        AT_con(sequence_flat)
    elif int(user_input) == 3:
        GC_con(sequence_flat)
    elif int(user_input) == 4:
        print(complementss)
    elif int(user_input) == 5:
        print(reverse_complement)
    else:
        print("Select number")
    