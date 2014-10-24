import numpy as np
import pysam


def fetch(bam_file, start, end):
    print bam_file
    with pysam.Samfile(bam_file, "rb") as samfile:
        return (
            ('TEST', np.zeros(512, dtype=np.int16)),
        )
