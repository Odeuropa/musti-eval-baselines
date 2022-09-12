#!/bib/bash

basedir=~/musti
INDIR=${basedir}/data/image_data/images/
OUTDIR=${basedir}/data/image_data/features/

mkdir -p $OUTDIR

source activate py-bottomup

python flickr30k_boxes36_h5-proposal.py \
  --root $INDIR \
  --outdir $OUTDIR \

deactivate

