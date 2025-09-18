from Bio import SeqIO

fasta_file = input("Enter FASTA file path: ")

record = next(SeqIO.parse(fasta_file, "fasta"))

print("Header:", record.id)
print("Sequence length:", len(record.seq))
