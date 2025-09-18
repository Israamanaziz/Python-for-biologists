from Bio.Seq import Seq
def reverse_complement(dna_sequence):
    DNA_seq = Seq(dna_sequence)
    rev_complement_seq= DNA_seq.reverse_complement()
    print(f"Reverse Complement of the DNA sequence is: {rev_complement_seq}")


dna_sequence= "ATCGTATCCGTACGTAAACGTT"
reverse_complement(dna_sequence)