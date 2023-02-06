download: data/*.json
	zip -r downloads/mft_nlp_data.zip data/	

dataset_charts: data/results/*.tsv
	python3 scripts/make_dataset_charts.py