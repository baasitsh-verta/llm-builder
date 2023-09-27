from prompts.base import Prompt
import os
from dataset.base import Dataset
import json
import itertools
from computation import load
import pandas as pd

def load_config():
    return json.load(open("../data/app_config.json"))

def load_data():
    # Load datasets from yaml files
    datasets = []
    # Loop over all the files in the dataset folder
    if os.path.exists("../data/datasets"):
        for filename in os.listdir("../data/datasets"):
            # Open the file
            with open("../data/datasets/{}".format(filename), "r") as f:
                # Load the dataset from the file
                dataset = json.load(f)
                dataset = Dataset.from_dict(dataset)
                # Add the dataset to the list of datasets
                datasets.append(dataset)

    # Load prompts from yaml files
    prompts = []
    # Loop over all the files in the prompt folder
    if os.path.exists("../data/prompts"):
        for filename in os.listdir("../data/prompts"):
            # Open the file
            with open("../data/prompts/{}".format(filename), "r") as f:
                # Load the prompt from the file
                prompt = json.load(f)
                prompt = Prompt.from_dict(prompt)
                # Add the prompt to the list of prompts
                prompts.append(prompt)

    return (datasets, prompts)


def create_table(datasets, models, prompts, cached=True):
    data = {
        'model': [],
        'prompt content': [],
        'dataset': [],
        'record id': [],
        'record input': [],
        'ground truth': [],
        'prediction': [],
    }

    for dataset in datasets:
        for (model, prompt, record) in itertools.product(models, prompts, dataset.records):
            if cached:
                prediction = load(model, prompt, dataset, record)
            else:
                prediction = model.predict(prompt, record.input_data)
            data['model'].append(model.get_name())
            data['prompt content'].append(prompt.prompt)
            data['dataset'].append(dataset.name)
            data['record id'].append(record.id)
            data['record input'].append(record.input_data)
            data['ground truth'].append(record.ground_truth)
            data['prediction'].append(prediction)

    df = pd.DataFrame(data)

    return df
