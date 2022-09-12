# musti-eval-baselines

This repository relies on [volta](https://github.com/e-bug/volta). There are some additions and modifications to run specific models on Musti data.

## Setup

Follow the steps in Repository Setup in [volta](https://github.com/e-bug/volta#repository-setup) except cloning original volta repository use `git clone git@github.com:kiymetakdemir/musti-eval-baselines.git`.

## Test Data Preparation and Downloading Images

```bash
python download_images.py --split True --lang en --filepath musti_data/musti-train.json
```

To include all languages in test data set split parameter to False.

## Feature Extraction

```bash
conda activate py-bottomup
cd /musti-eval-baselines/volta/features_extraction/datasets/flickr30k
python flickr30k_boxes36_h5-proposal.py --root /musti-eval-baselines/data/image_data/images --outdir /musti-eval-baselines/data/image_data/features

cd /musti-eval-baselines/volta/features_extraction
python h5_to_lmdb.py --h5 /musti-eval-baselines/data/image_data/features/musti_boxes36.h5 --lmdb /musti-eval-baselines/data/image_data/features/lmdb
conda deactivate
```

## Evaluate data

```bash
cd /musti-eval-baselines/test_scripts
bash test_vilbert_finetuned.sh

cd /musti-eval-baselines
python eval_result.py --test_file data/test_files/musti-train-en.jsonl --logit_file results/vilbert/pretrained/musti-train-en-logits.txt
```








