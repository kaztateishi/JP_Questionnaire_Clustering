Japanese Questionnaire Categorization and Clustering
This project categorizes free-form Japanese questionnaire responses into thematic clusters and identifies nonsensical answers. It uses NLP tools to tokenize text, extract keywords, and cluster responses into 30-40 topics for better analysis and insights.

Table of Contents
Overview
Requirements
Installation
Usage
Customization
Output
Overview
The script processes responses by:

Filtering nonsensical entries (like repetitive characters).
Extracting keywords for each response.
Clustering responses into thematic groups.
Assigning and exporting tags for each response to a new CSV file.
Requirements
The script requires the following Python libraries:

pandas: For data manipulation
scikit-learn: For TF-IDF vectorization and KMeans clustering
janome: A tokenizer for Japanese text
Installation
Clone or download the project.

Install the required packages:

bash
Copy code
pip install pandas scikit-learn janome
Place your input CSV file (e.g., your_file.csv) in the project directory. Ensure it has two columns:

ID: Unique identifier for each response
Answer: The free-form response in Japanese
Usage
Open the script and update the file path in the data loading step to match your input file:

python
Copy code
data = pd.read_csv("your_file.csv")
Run the script:

bash
Copy code
python categorize_responses.py
Detailed Steps
Load Data: Reads the input CSV containing questionnaire responses.
Define Helper Functions:
is_nonsensical: Identifies nonsensical responses based on patterns.
extract_keywords: Tokenizes responses and extracts key nouns.
Preprocess Data: Filters out nonsensical responses and extracts keywords.
TF-IDF Transformation and Clustering: Transforms keywords into numerical vectors for clustering and applies KMeans with a specified number of clusters.
Assign Labels: Assigns a generic label to each cluster, which can later be refined for clarity.
Save Output: Exports the processed data to a new CSV file with added tags for each response.
Customization
Adjust Number of Clusters: You can change num_clusters in the KMeans clustering step to increase or decrease the number of categories.
Refine Cluster Labels: After running the script, review the responses in each cluster to create meaningful labels for each category.
Output
The script outputs a file named categorized_answers_with_tags.csv with the following columns:

ID: Original unique ID of the response.
Answer: Original free-form response text.
Tag: Assigned topic label based on clustering.
Optional: View Clusters
To examine the responses in each cluster and adjust tags, you can use the print statements in the code to see sample entries for each cluster.

Example
ID	Answer	Tag
001	自分の健康についての不安	Topic_1
002	家族の関係に関する悩み	Topic_2
003	あああああ	Nonsensical
