#! /usr/bin/env python

"""
By Paul Wolf. Modified Oct 19th, 2014
paul.wolf@usu.edu
This script takes a fasta file (first argument) and a file containing a list of contigs
that you want to remove (one conig name per line)- filename is second argument.
output file (output.fasta) has contigs removed. Output file name shoule be third argument,
but will give default name if not specified

"""

from Bio import SeqIO
import sys


def remove_contigs(fasta_file, contigs_to_remove_list, out_name):
    out = open(out_name, 'w')
    for record in SeqIO.parse(fasta_file, "fasta") :
        #print record.id
        if record.id not in contigs_to_remove_list:
            newline = str(record.id) + '\n' + str(record.seq) + ('\n')
            out.write(newline)
    out.close()
            
def print_lengths_cp_contigs(handle,cp_list):
    for record in SeqIO.parse(handle, "fasta") :
        if record.id in cp_list:
            print record.id, len(record.seq)
            
def make_contig_list (list_file):
    contig_list = []
    for line in list_file:
        line = line.strip ('\n')
        contig = line
        contig_list.append(contig)
    return contig_list
    
    
            
if __name__ == "__main__":
    fasta_file = open(sys.argv[1], 'rU)')
    contig_list_file = open(sys.argv[2],'r')
    contigs_to_remove_list = make_contig_list(contig_list_file)
    #print contigs_to_remove_list
    if len(sys.argv) < 4:
        outfile_name = 'stripped_output.fasta'
    else:
        outfile_name = sys.argv[3]    
    remove_contigs(fasta_file,contigs_to_remove_list, outfile_name)
    #print_lengths_cp_contigs(handle,cp_list)
    fasta_file.close()
    contig_list_file.close()
