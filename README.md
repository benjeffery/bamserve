# bamserve

Small python server for reads from BAM files.

Each bam should be in a folder (optionally with it's tabix index) with the same name
eg:
  
    /data/bams/bam_1/bam_1.bam
    /data/bams/bam_2/bam_2.bam
    /data/bams/bam_3/bam_3.bam


To install:
  
    git clone git@github.com:benjeffery/bamserve.git
    cd bamserve
    pip install -r REQUIREMENTS
  
Then edit config.yaml to point to your bams, eg:

    sets:
      my_bams:
        path: /data/bams
 
 Then to run:

    ./scripts/run.sh
  
Data can then be fetched from eg:
http://localhost:8000/bam/my_bams/bam_1/chrom/0/1000

A test webpage that can be opened in chrom is included but you'll need to edit the URL in test.js to point to your bam.



