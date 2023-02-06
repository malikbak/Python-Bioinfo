import re
def genbank_to_fasta():
    file = input(r'Input the path to your file: ')
    with open(f'{file}') as f:
        gb = f.readlines()
        locus = re.search('NM_\d+\.\d+', gb[3]).group()
        defination = gb[1].replace('DEFINITION', '')
        print(locus, defination)
        sequence = ""
        for line in (gb):
            pattern = re.compile('[a,t,g,c]{10}')
            matches = pattern.finditer(line)
            for match in matches:
                sequence += match.group().upper()
        end_pattern = re.search('[a,t,g,c]{1,9}', gb[-3])
        sequence += end_pattern.group().upper()
        ofile = open(locus+'.txt', "w")
        ofile.write(">" + locus+defination+ "\n" +sequence + "\n")
        ofile.close()
        return sequence

out = genbank_to_fasta()
print(out)