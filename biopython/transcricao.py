from Bio.Seq import Seq

my_seq = Seq("ATG")

# DNA Codificante -> RNA Mensageiro
seq_rna = my_seq.transcribe()
print(seq_rna)

# RNA Mensageiro -> DNA Codificante
seq_dna = seq_rna.back_transcribe()
print(seq_dna)