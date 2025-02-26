from anarci import number

# Example nanobody sequence (VHH domain)
sequence = "QVQLQESGGGLVQAGGSLRLSCAASGRTFSNYGMGWFRQAPGKEREFVAAISSWGGTYYADSVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCAAAGTYYYGGSYDYWGQGTQVTVSS"

# Run ANARCI with the IMGT numbering scheme (recommended for nanobodies)
results, alignment_details = number(sequence, scheme='imgt')

# Extract numbered sequence
numbering = results[0][0]

# Get CDR regions
cdrs = {region: ''.join([res[1] for res in numbering if res[0] in positions])
        for region, positions in alignment_details['regions'].items() if 'CDR' in region}

print("Nanobody CDR Annotations:")
for cdr, seq in cdrs.items():
    print(f"{cdr}: {seq}")