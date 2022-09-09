#!/bin/bash

TASK=13
MODEL=muniter
MODEL_CONFIG=ctrl_muniter_base
TASKS_CONFIG=config_test_task
PRETRAINED=../models/muniter_finetuned.bin
OUTPUT_DIR=../results/muniter/finetuned

activate volta

cd ../volta
python eval_task.py \
	--config_file config/${MODEL_CONFIG}.json --from_pretrained ${PRETRAINED} \
	--tasks_config_file ../${TASKS_CONFIG}.yml --task $TASK \
	--output_dir ${OUTPUT_DIR}

conda deactivate
