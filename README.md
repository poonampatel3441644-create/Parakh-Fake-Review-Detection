## Model Evaluation

Models were evaluated on the same held-out test set of 8,084 reviews.

| Model | Accuracy |
|---|---:|
| A — Raw Text (TF-IDF baseline) | 93.32% |
| B — Cleaned Text | 93.32% |
| C — Formatting Features Only | 77.68% |
| D — Trailing Fragment Removed | 90.12% |
| Random Forest — Transformed Text | 87.69% |

### Cross-Validation

Model A was evaluated using 5-fold stratified cross-validation on the training data.

- Mean accuracy: 92.64%
- Standard deviation: 0.28 percentage points

The relatively small variation across folds suggests consistent performance across the evaluated splits.

### Truncation Experiment

Removing trailing text fragments reduced test accuracy from 93.32% to 90.12%. This suggests that the text transformation affects predictive performance, but it does not establish how much of the original performance came from truncation artifacts.

The transformation may remove legitimate text and leaves reviews without sentence-ending punctuation unchanged. Therefore, Model D is an exploratory stress test rather than a definitive estimate of real-world performance.

### Random Forest

The Random Forest model achieved 87.69% accuracy using TF-IDF features from the transformed reviews. It performed below the baseline models in this experiment.

Its feature-importance analysis ranked several common words and phrases highly. These rankings show which features contributed to tree impurity reductions, but do not establish causal relationships or prove that individual words identify fake reviews.

### Conclusion

The TF-IDF baseline achieved the highest test accuracy among the models evaluated so far. Further testing on independent data is needed to assess generalization and determine whether the detected patterns reflect genuine review characteristics or dataset-specific artifacts.

## Day 4: Multi-Layer Perceptron (MLP) Experiments

### Objective
The objective of Day 4 was to build a neural network using TensorFlow/Keras and investigate how different optimizers and regularization techniques affect fake-review classification performance.

### Technologies Used
- Python
- TensorFlow and Keras
- NumPy and Pandas
- Scikit-learn
- Matplotlib
- TF-IDF for text feature extraction

### Dataset and Preprocessing
The experiments used the existing review dataset after removing duplicate rows.

- Total reviews: 40,420
- Training samples: 32,336
- Testing samples: 8,084
- Input features: 5,000 TF-IDF features
- Text preprocessing: Model D transformation, which removes trailing text after the last sentence-ending punctuation mark.

The transformation was retained for comparison with the previous baseline experiments. It is exploratory and may remove legitimate review content.

### Neural Network Architecture
The MLP used the following architecture:

1. **Input layer:** 5,000 TF-IDF features
2. **Hidden layer:** 64 neurons with ReLU activation
3. **Regularization:** Dropout or L1/L2 regularization, depending on the experiment
4. **Output layer:** One neuron with sigmoid activation for binary classification

Binary cross-entropy was used as the loss function. Early stopping monitored validation loss and restored the best weights when training stopped.

### Experiments and Results

| Model | Test Accuracy |
|---|---:|
| SGD (learning rate 0.1, momentum 0.9) | 90.18% |
| Adam + Dropout (0.4) | 90.09% |
| Adam Baseline | 89.84% |
| Adam + L2 (0.001), 40 epochs | 89.51% |
| Adam + L1 (0.0001), 40 epochs | 89.29% |
| Adam + L2 (0.001), initial 12-epoch run | 89.46% |
| Adam + L1 (0.0001), initial 12-epoch run | 86.92% |
| SGD Baseline (learning rate 0.01) | 70.96% |

*Note: The 40-epoch regularization runs are separate experiments. They used the same data split and architecture, but were allowed more training time.*

### Key Observations

- **Optimizer choice matters:** SGD with a learning rate of 0.01 performed poorly, while SGD with a learning rate of 0.1 and momentum achieved 90.18% test accuracy.
- **Dropout:** Adding dropout with a rate of 0.4 achieved 90.09%, slightly above the Adam baseline of 89.84%.
- **L1 regularization:** Extending training to 40 epochs improved test accuracy from 86.92% to 89.29%.
- **L2 regularization:** Extending training to 40 epochs improved test accuracy slightly, from 89.46% to 89.51%.
- **Training duration:** The longer regularization experiments continued improving, showing why the initial 12-epoch results needed further investigation.

### Comparison with Previous Models

| Model | Test Accuracy |
|---|---:|
| Logistic Regression — Raw Text (Model A) | 93.32% |
| Logistic Regression — Transformed Text (Model D) | 90.12% |
| MLP — SGD with Momentum | 90.18% |
| MLP — Adam + Dropout | 90.09% |
| Random Forest — Transformed Text | 87.69% |

Logistic Regression on raw text achieved the highest test accuracy among these reported experiments. The MLP results show that a neural network can approach the transformed-text baseline, but these results do not establish that it generalizes better to unseen datasets.

### Conclusion
Day 4 introduced neural-network-based fake-review classification using an MLP. Different optimizers and regularization techniques were evaluated to understand their effect on model performance. SGD with momentum and Adam with dropout produced the strongest MLP results in these experiments. Longer training substantially improved the L1-regularized model and slightly improved the L2-regularized model.

Further work should include plotting training and validation loss, checking for overfitting, and evaluating the selected model on an independent dataset before drawing conclusions about real-world performance.

staticfiles/
.venv/
venv/
__pycache__/
.ipynb_checkpoints/
.env
.env.*
!.env.example
data/
outputs/feature_analysis.csv
db.sqlite3
*.py[cod]
staticfiles/

staticfiles/

## 🌐 Live Demo

Try Parakh here:

**[Open Parakh – Fake Review Detection](https://parakh-fake-review-detection.onrender.com)**