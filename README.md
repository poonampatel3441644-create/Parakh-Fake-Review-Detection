## Baseline Model Evaluation

Three baseline approaches were evaluated for fake-review detection.

| Model | Accuracy |
|---|---:|
| Model A — Raw Text | 93.32% |
| Model B — Cleaned Text | 93.32% |
| Model C — Formatting Only | 77.68% |

### Error Analysis

Model A was evaluated on 8,084 test reviews and achieved **93.32% accuracy**, with 540 incorrect predictions (6.68% error rate).

The errors were distributed as follows:

- **CG predicted as OR:** 324 reviews.
- **OR predicted as CG:** 216 reviews.

Models A and B produced identical predictions on the test set, although the cleaning process modified 18,564 training reviews (57.41%). This indicates that the current cleaning process did not change Model B's predictions compared with Model A on this test set.

### Conclusion

The baseline experiments provide a starting point for further model development. Distinguishing computer-generated reviews from original reviews remains an area for improvement. Further experiments are needed to investigate misclassified reviews and evaluate possible improvements.

### Cleaning Analysis

The cleaning function normalizes whitespace, replaces line breaks with spaces, and inserts missing spaces after punctuation. It changed 18,564 training reviews (57.41%) and 4,721 test reviews (58.40%).

Despite these text changes, Model A (raw text) and Model B (cleaned text) achieved the same test accuracy of 93.32%. Their predictions were identical, and the TF-IDF feature matrices showed no differences on the test set.

This suggests that the current formatting-focused preprocessing did not change the features used by the baseline model on this test set. Further experiments are needed to determine whether alternative preprocessing methods improve classification performance.