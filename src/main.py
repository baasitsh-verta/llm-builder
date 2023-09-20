from models.abc import Model
from typing import List
from models.nop import Nop
import streamlit as st
from prompts.base import Prompt
import os
from dataset.base import Dataset, Sample
import pandas as pd
import dataclasses
import json
import itertools
from testing import generate_data
from table import load_data

models: List[Model] = [
    Nop(0),
]

# generate_data()
(datasets, prompts) = load_data()

# Create cache folder
if not os.path.exists("../cache"):
    os.makedirs("../cache")

data = {
    'model': [],
    'prompt name': [],
    'prompt content': [],
    'dataset': [],
    'sample id': [],
    'sample input': [],
    'sample output': [],
    'prediction': [],
}

for dataset in datasets:
    for (model, prompt, sample) in itertools.product(models, prompts, dataset.samples):
        data['model'].append(model.get_name())
        data['prompt name'].append(prompt.name)
        data['prompt content'].append(prompt.prompt)
        data['dataset'].append(dataset.name)
        data['sample id'].append(sample.id)
        data['sample input'].append(sample.input_data)
        data['sample output'].append(sample.output_data)
        data['prediction'].append(model.predict(prompt, sample.input_data))


# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Create a Streamlit app
st.title('Streamlit Table Example')
st.write('This is a simple table created using Streamlit.')

# Display the table using st.table()
st.table(df)
