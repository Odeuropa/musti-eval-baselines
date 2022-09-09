#!/bin/bash

TASK=13
MODEL=vilbert
MODEL_CONFIG=vilbert_base
TASKS_CONFIG=config_test_task
PRETRAINED=../models/vilbert_pretrained.bin
OUTPUT_DIR=../results/vilbert/pretrained

activate volta

cd ../volta
python eval_task.py \
	--config_file config/${MODEL_CONFIG}.json --from_pretrained ${PRETRAINED} \
	--tasks_config_file ../${TASKS_CONFIG}.yml --task $TASK \
	--output_dir ${OUTPUT_DIR} 

conda deactivate
