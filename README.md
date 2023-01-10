# musti-eval-baselines

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
Find links to download pretrained models from this [link](https://github.com/Odeuropa/musti-eval-baselines/blob/main/volta/MODELS.md). Place <em>baselines</em> folder that contains models under <em>musti-eval-baselines</em> folder. Model configuration files are stored in volta/config/.

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

| | Positive pairs (Train) | Total pairs (Train) | Positive pairs (Test) | Total pairs (Test) |
| :---  | :---:  | :---:  | :---:  | :---:  |
| English  | 198 (24.90%) | 795 | - | 200 |
| German | 95 (19.79%) | 480 | - | 213 |
| French | 102 (34.00%) | 300 | - | 200  |
| Italian | 198 (24.78%) | 799 | - | 201 |

Table 1: MUSTI train and test set data statistics. The class distribution of the test data is kept confidential.

## Results

Majority of data in each language is the negative class. Therefore we present the dummy baseline results where the baseline classifies all pairs as negative. The Overall score is the F1-macro on all predictions on all test data.

| | English | German | French | Italian | Overall | 
| :---  | :---:  | :---:  | :---:  | :---:  | :---:  |
| dummy-baseline |  .4285 | .4289 | .3333 | .4273 | .4075 |
| mUNITER | .4269 | .4289 | .3551 | .4398 | .4177 |
| mUNITER-SNLI | .4474 | .4644 | .3605 | .5020 | .4473 |
| mUNITER-MUSTI | .6965 | .4579 | .5022 | .6535 | .6011 |
| mUNITER-SNLI-MUSTI | .7482 | **.5014** | **.5053** | .6850 | **.6176** |
| Shao et al. | .7867 | .4568 | .3743 | **.7501** | .6033 |
| ViLBERT-SNLI-MUSTI | **.8024** | - | - | - | - |

Table 2: Multilingual models and ViLBERT-SNLI-MUSTI results on the MUSTI test set, given as F1-macro score.
Best performing monolingual model Vilbert-SNLI-MUSTI added for reference.

---

| ViLBERT | ViLBERT-SNLI | ViLBERT-MUSTI | ViLBERT-SNLI-MUSTI | Shao et al. (multilingual) | 
| :---:  | :---:  | :---:  | :---:  | :---:  |
| .4609 | .4373 | .7834 | **.8024** | .7867 |

Table 3: ViLBERT results on the MUSTI English test set, given as F1-macro score.
Best performing multilingual model on English Shao et al. added for reference.


## Acknowledgement
This code is modified from [volta](https://github.com/e-bug/volta) which in turn relies on [vilbert-multi-task](https://github.com/facebookresearch/vilbert-multi-task) and [other repositories](https://github.com/e-bug/volta#acknowledgement).

