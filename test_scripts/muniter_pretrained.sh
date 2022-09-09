#!/bin/bash

TASK=13
MODEL=muniter
MODEL_CONFIG=ctrl_muniter_base
TASKS_CONFIG=config_test_task
PRETRAINED=../models/muniter_pretrained.bin
OUTPUT_DIR=../musti/results/muniter/pretrained

activate volta

cd ../volta
python eval_task.py \
	--config_file config/${MODEL_CONFIG}.json --from_pretrained ${PRETRAINED} \
	--tasks_config_file ../${TASKS_CONFIG}.yml --task $TASK \
	--output_dir ${OUTPUT_DIR}

conda deactivate
