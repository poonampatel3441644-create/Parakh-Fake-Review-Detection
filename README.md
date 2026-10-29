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