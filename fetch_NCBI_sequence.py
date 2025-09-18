from Bio import Entrez

def fetch_sequence(accession_id):
 Entrez.email = "isra.aman20@gmail.com"
 info = Entrez.efetch(db= "nucleotide", id= accession_id, rettype="gb" ,retmode="text" )
 sequence_data = info.read()
 print(sequence_data)

accession_id= "AH002844.2"
fetch_sequence(accession_id)

