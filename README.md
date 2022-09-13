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

## Data

| | Positive number of pairs | Total number of pairs |
| ------------- | ------------- | ------------- |
| English | 201 (25.12%) | 800 |
| Italian | 202 (25.12%) | 804 |
| French | 103 (33.88%) | 304 |
| German | 95 (19.71) | 482 |

Table 1: Number and proportion of Musti training data for each language

## Results

Majority of data in each language is the negative class. Therefore we present the dummy baseline results where the baseline classifies all pairs as negative. 

| | ViLBERT pretrained | ViLBERT finetuned | mUNITER pretrained | mUNITER finetuned | dummy baseline | 
| :---  | :---:  | :---:  | :---:  | :---:  | :---:  |
| accuracy | 0.67 | 0.74 | 0.73 | 0.75 | 0.75 |
| precision | 0.19 | 0.37 | 0.00 | 0.47 | 0.00 |
| recall | 0.10 | 0.07 | 0.00 | 0.04 | 0.00 |
| f1 | 0.14 | 0.12 | 0.00 | 0.08 | 0.00 |

Table 2: ViLBERT and mUNITER results on English data

---

| | mUNITER pretrained | mUNITER finetuned | dummy baseline | 
| :--- | :---:  | :---:  | :---:  |
| accuracy | 0.73 | 0.75 | 0.75 |
| precision | 0.20 | 0.50 | 0.00 |
| recall | 0.02 | 0.06 | 0.00 |
| f1 | 0.04 | 0.11 | 0.00 |

Table 3: mUNITER results on Italian data

---

| | mUNITER pretrained | mUNITER finetuned | dummy baseline | 
| :---  | :---:  | :---:  | :---:  |
| accuracy | 0.65 | 0.65 | 0.66 |
| precision | 0.00 | 0.43 | 0.00 |
| recall | 0.00 | 0.06 | 0.00 |
| f1 | 0.00 | 0.10 | 0.00 |

Table 4: mUNITER results on French data

---

| | mUNITER pretrained | mUNITER finetuned | dummy baseline | 
| :---  | :---:  | :---:  | :---:  |
| accuracy | 0.80 | 0.77 | 0.80 |
| precision | 0.50 | 0.25 | 0.00 |
| recall | 0.01 | 0.08 | 0.00 |
| f1 | 0.02 | 0.13 | 0.00 |

Table 5: mUNITER results on German data








