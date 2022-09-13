# musti-eval-baselines

This repository relies on [volta](https://github.com/e-bug/volta). There are some additional scripts and modifications to run specific models on [Musti](https://multimediaeval.github.io/editions/2022/tasks/musti/) data.

## Setup

Follow the steps in Repository Setup in [volta](https://github.com/Odeuropa/musti-eval-baselines/tree/main/volta#repository-setup). Except cloning original volta repository, use `git clone git@github.com:Odeuropa/musti-eval-baselines.git`.

## Test Data Preparation and Downloading Images

To prepare test file on a specific language use:
```bash
python download_images.py --split --lang en --filepath data/musti_data/musti-train.json
```

To include all languages in test file, use:
```bash
python download_images.py --no-split
```

## Feature Extraction
To install Feature Extractor follow the steps in [here](https://github.com/Odeuropa/musti-eval-baselines/tree/main/volta/features_extraction#install-feature-extractor).

```bash
conda activate py-bottomup

cd volta/features_extraction/datasets/flickr30k
python flickr30k_boxes36_h5-proposal.py --root /musti-eval-baselines/data/image_data/images --outdir /musti-eval-baselines/data/image_data/features

cd ../..
python h5_to_lmdb.py --h5 /musti-eval-baselines/data/image_data/features/musti_boxes36.h5 --lmdb /musti-eval-baselines/data/image_data/features/lmdb

conda deactivate
```

## Models
For those who have access to the Odeuropa Google Drive folder can find the models ViLBERT and mUNITER pretrained and finetuned (on SNLI-VE), under the folder [MUSTI-organization/baselines](https://drive.google.com/drive/folders/1TJNMwY3QbHMcrd71Ybh-9CK_SPHWyWPW?usp=sharing) or find links to download pretrained models from this [link](https://github.com/Odeuropa/musti-eval-baselines/blob/main/volta/MODELS.md). Place <em>baselines</em> folder that contains models under <em>musti-eval-baselines</em>. Model configuration files are stored in volta/config/.

## Evaluate data

Make sure that [config_test_task.yml](https://github.com/Odeuropa/musti-eval-baselines/blob/main/config_test_task.yml) has the right test file path as <em>val_annotations_jsonpath</em>.

```bash
conda activate volta

cd test_scripts
bash test_vilbert_finetuned.sh

cd ..
python eval_result.py --test_file data/test_files/musti-train-en.jsonl --logit_file results/vilbert/pretrained/musti-train-en-logits.txt

conda deactivate
```








