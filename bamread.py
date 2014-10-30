import operator
import numpy as np
import pysam


def fetch(bam_file, chrom, start, end):
    with pysam.Samfile(bam_file, "rb") as samfile:
        #TODO - Seems a shame to make a python list - must be a way to stream
        reads = samfile.fetch(chrom, start, end)
        positions = []
        lengths = []
        seqs = ''
        cigars = []
        for read in reads:
            positions.append(read.pos)
            lengths.append(read.rlen)
            seqs += read.seq
            cigars += [val for step in read.cigar for val in step] + [-1, -1]
        return {
            'pos': np.asarray(positions, dtype=np.uint32),
            'len': np.asarray(lengths, dtype=np.uint16),
            'seq': np.asarray([seqs], dtype='S'+str(len(seqs))),
            'cigar': np.asarray(cigars, dtype=np.int16),
        }.items()