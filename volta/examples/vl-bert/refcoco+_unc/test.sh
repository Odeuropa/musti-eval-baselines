#!/bin/bash

TASK=10
MODEL=vl-bert
MODEL_CONFIG=vl-bert_base
TASKS_CONFIG=vl-bert_test_tasks
PRETRAINED=checkpoints/refcoco+_unc/${MODEL}/refcoco+_${MODEL_CONFIG}/pytorch_model_12.bin
OUTPUT_DIR=results/refcoco+_unc/${MODEL}

source activate volta

cd ../../..
python eval_task.py \
	--config_file config/${MODEL_CONFIG}.json --from_pretrained ${PRETRAINED} \
	--tasks_config_file config_tasks/${TASKS_CONFIG}.yml --task $TASK \
	--output_dir ${OUTPUT_DIR}

conda deactivate
