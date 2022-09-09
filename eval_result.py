import pandas as pd
from scipy.special import softmax
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, recall_score, precision_score
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--test_file', type=str, default='data/test_files/musti-train-en.jsonl')
	parser.add_argument('--logit_file', type=str, default='results/vilbert/finetuned/musti-train-en-logits.txt')
	args = parser.parse_args()
	print(args.test_file)
	print(args.logit_file)
	print()

	df = pd.read_json(args.test_file, lines=True)
	logit_path = args.logit_file

	LABEL_MAP = {"contradiction": 0, "neutral": 1, "entailment": 2}

	logits_list = []
	with open(logit_path, 'r') as f:
		lines = f.readlines()
		for line in lines:
			logits = [float(v) for v in line.split(',')[:-1]]
			logits_list.append(logits)

		probs_list = softmax(logits_list, axis=1)

	y_true = [1 if LABEL_MAP[d]==2 else 0 for d in df['gold_label']]    #entailment: 1; contradiction,neutral: 0
	y_pred = [1 if probs.argmax()==2 else 0 for probs in probs_list]
	print('y_true len:', len(y_true))
	print('y_pred len:', len(y_pred))
	print()
	
	print(confusion_matrix(y_true, y_pred))
	print()

	print("accuracy: {:.4f}".format(accuracy_score(y_true, y_pred)))
	print("precision: {:.4f}".format(precision_score(y_true, y_pred)))
	print("recall: {:.4f}".format(recall_score(y_true, y_pred)))
	print("f1: {:.4f}".format(f1_score(y_true, y_pred)))
