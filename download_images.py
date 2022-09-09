import argparse
import pandas as pd
import requests, json
import os.path

dataroot = "data/"
def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("--lang", default='en', type=str)
	parser.add_argument("--split", type=bool)
	parser.add_argument("--filepath", default=dataroot+'musti_data/musti-train.json', type=str)
	return parser.parse_args()

def main():
	args = parse_args()
	f = open(args.filepath)
	df = pd.DataFrame(json.load(f)["pairs"])
	
	for image_url in df['image']:
		if not os.path.isfile(dataroot+'image_data/images/'+image_url.split('/')[-1]):
			img_data = requests.get(image_url).content
			with open(dataroot+'image_data/images/'+image_url.split('/')[-1], 'wb') as handler:
				handler.write(img_data)
	
	data = []
	pos = 0
	total = 0
	for i in range(len(df)):
		d = dict()
		record = df.loc[i]
		if args.split and record['language']!=args.lang:
			pass
		else:
			d['Flikr30kID'] = record['image'].split('/')[-1]
			d['sentence2'] = record['text']
			#d["annotator_labels"] = ["entailment"] if record['subtask1_label'] == 'YES' else ["contradiction"]
			d["gold_label"] = "entailment" if record['subtask1_label'] == 'YES' else "contradiction"
			if record['subtask1_label'] == 'YES':
				pos += 1
			total += 1
			data.append(d)
	
	print("pos {}, neg {}, total {}".format(pos, total-pos, total))
	print("positive ratio: ",round((pos/total)*100,2))

	if args.split:
		with open(dataroot+"test_files/{}-{}.jsonl".format(args.filepath.split('/')[-1].split('.')[0], args.lang), 'w', encoding='utf-8') as f:
			print("File saved to {}test_files/{}-{}.jsonl".format(dataroot,args.filepath.split('/')[-1].split('.')[0], args.lang))
			for d in data:
				json.dump(d, f, ensure_ascii=False)
				f.write('\n')
	else:
		with open(dataroot+"test_files/{}.jsonl".format(args.filepath.split('/')[-1].split('.')[0]), 'w', encoding='utf-8') as f:
                        print("File saved to {}test_files/{}.jsonl".format(dataroot,args.file_path.split('/')[-1].split('.')[0]))
                        for d in data:
                                json.dump(d, f, ensure_ascii=False)
                                f.write('\n')

if __name__ == "__main__":
	main()
