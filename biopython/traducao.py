from Bio.Seq import Seq

my_seq = Seq("ATG")

# Transcrição
my_rna = my_seq.transcribe()
my_dna = my_rna.back_transcribe()
print(my_rna)
print(my_dna)

# Tradução
my_protein = my_rna.translate()
my_protein_dna = my_dna.translate()
print(my_protein)
print(my_protein_dna)

