Here's a `README.md` to accompany the project, explaining each part of the code and how to use it.

---

# Japanese Questionnaire Categorization and Clustering

This project categorizes free-form Japanese questionnaire responses into thematic clusters and identifies nonsensical answers. It uses NLP tools to tokenize text, extract keywords, and cluster responses into 30-40 topics for better analysis and insights.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Output](#output)

## Overview

The script processes responses by:
1. Filtering nonsensical entries (like repetitive characters).
2. Extracting keywords for each response.
3. Clustering responses into thematic groups.
4. Assigning and exporting tags for each response to a new CSV file.

## Requirements

The script requires the following Python libraries:
- `pandas`: For data manipulation
- `scikit-learn`: For TF-IDF vectorization and KMeans clustering
- `janome`: A tokenizer for Japanese text

## Installation

1. Clone or download the project.
2. Install the required packages:
   ```bash
   pip install pandas scikit-learn janome
   ```

3. Place your input CSV file (e.g., `your_file.csv`) in the project directory. Ensure it has two columns:
   - **ID**: Unique identifier for each response
   - **Answer**: The free-form response in Japanese

## Usage

1. Open the script and update the file path in the `data` loading step to match your input file:
   ```python
   data = pd.read_csv("your_file.csv")
   ```
   
2. Run the script:
   ```bash
   python categorize_responses.py
   ```

### Detailed Steps

1. **Load Data**: Reads the input CSV containing questionnaire responses.
2. **Define Helper Functions**:
   - `is_nonsensical`: Identifies nonsensical responses based on patterns.
   - `extract_keywords`: Tokenizes responses and extracts key nouns.
3. **Preprocess Data**: Filters out nonsensical responses and extracts keywords.
4. **TF-IDF Transformation and Clustering**: Transforms keywords into numerical vectors for clustering and applies KMeans with a specified number of clusters.
5. **Assign Labels**: Assigns a generic label to each cluster, which can later be refined for clarity.
6. **Save Output**: Exports the processed data to a new CSV file with added tags for each response.

## Customization

- **Adjust Number of Clusters**: You can change `num_clusters` in the KMeans clustering step to increase or decrease the number of categories.
- **Refine Cluster Labels**: After running the script, review the responses in each cluster to create meaningful labels for each category.

## Output

The script outputs a file named `categorized_answers_with_tags.csv` with the following columns:
- **ID**: Original unique ID of the response.
- **Answer**: Original free-form response text.
- **Tag**: Assigned topic label based on clustering.

### Optional: View Clusters
To examine the responses in each cluster and adjust tags, you can use the print statements in the code to see sample entries for each cluster.

## Example

| ID        | Answer                  | Tag        |
|-----------|--------------------------|------------|
| 001       | 自分の健康についての不安 | Topic_1    |
| 002       | 家族の関係に関する悩み    | Topic_2    |
| 003       | あああああ                | Nonsensical|

