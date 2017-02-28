import sys
import os

if len(sys.argv) < 3:
    sys.exit('Usage: %s <input SNP file> <input TFBS file>' % sys.argv[0])

if not os.path.exists(sys.argv[1]):
    sys.exit('ERROR: %s does not exist' % sys.argv[1])

if not os.path.exists(sys.argv[2]):
    sys.exit('ERROR: %s does not exist' % sys.argv[2])


# input file format: chr3\t170676134
input_file = open(sys.argv[1])
variant_pos = []
for record in input_file:
    splitted_record = record.rstrip().split("\t")
    if len(splitted_record) > 1:
        variant_pos.append(int(splitted_record[1]))
input_file.close()

tfbs_file = open(sys.argv[2])
for record in tfbs_file:
    record = record.rstrip()
    splitted_record = record.split("\t")
    if not len(splitted_record) > 5:
        continue
    start = int(splitted_record[1])
    end = int(splitted_record[2])
    matched_pos = []
    for pos in variant_pos:
        if start <= pos <= end:
            matched_pos.append(pos)
    if len(matched_pos) > 0:
        print(record, end="")
        for pos in matched_pos:
            print('\t%s' % str(pos))
tfbs_file.close()
