from Bio.Seq import Seq

my_seq = Seq("ATG")

# Sequência complementar
seq_complementar = my_seq.complement()
print(seq_complementar)

# Sequência reversa complementar
seq_complementar_reversa = my_seq.reverse_complement()
print(seq_complementar_reversa)