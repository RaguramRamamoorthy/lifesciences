from deepchem.molnet import load_tox21
import deepchem as dc
import numpy as np

# Load the data.

tox21_tasks, tox21_datasets, transformers = load_tox21()

train_dataset, valid_dataset, test_dataset = tox21_datasets

print(train_dataset.X.shape)
print(train_dataset.X[0].shape)
print(train_dataset.y[0])
print(valid_dataset.X.shape)
print(test_dataset.X.shape)

print(np.shape(train_dataset.y))
print(np.shape(valid_dataset.y))
print(np.shape(test_dataset.y))

print(train_dataset.w.shape)
print(np.count_nonzero(train_dataset.w))
print(np.count_nonzero(train_dataset.w == 0))

model = dc.models.MultitaskClassifier(n_tasks=12,
                                      n_features=1024,
                                      layer_sizes=[1000])

model.fit(train_dataset, nb_epoch=10)

metric = dc.metrics.Metric(dc.metrics.roc_auc_score, np.mean)
train_scores = model.evaluate(train_dataset, [metric], transformers)
test_scores = model.evaluate(test_dataset, [metric], transformers)
print(train_scores)
print(test_scores)