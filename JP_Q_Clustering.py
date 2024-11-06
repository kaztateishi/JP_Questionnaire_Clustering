import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from janome.tokenizer import Tokenizer
import re

# Step 1: Load Data
data = pd.read_csv("data.csv")  # Replace with your actual file path
data.columns = ['ID', 'Answer']  # Adjust column names if necessary

# Step 2: Define Helper Functions
# Detect nonsensical entries (e.g., repetitive characters)
def is_nonsensical(text):
    nonsensical_patterns = [
        r'^[あ-んア-ン]{3,}$',  # Repetitive kana
        r'^[a-zA-Z]{3,}$',     # Repetitive alphabetic
        r'^\W+$'               # Only symbols
    ]
    return any(re.match(pattern, text) for pattern in nonsensical_patterns)

# Extract keywords using Janome for Japanese noun extraction
tokenizer = Tokenizer()

def extract_keywords(text):
    tokens = tokenizer.tokenize(text)
    keywords = [token.surface for token in tokens if token.part_of_speech.startswith('名詞')]
    return ' '.join(keywords)

# Step 3: Preprocess Data
# Identify nonsensical entries
data['Nonsensical'] = data['Answer'].apply(is_nonsensical)
nonsensical_data = data[data['Nonsensical'] == True]
data = data[data['Nonsensical'] == False]  # Keep only sensible entries

# Apply keyword extraction to remaining entries
data['Keywords'] = data['Answer'].apply(extract_keywords)

# Step 4: Vectorize Text and Apply Clustering
# Convert keywords to TF-IDF features
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data['Keywords'])

# Apply KMeans clustering
num_clusters = 35  # Adjust number of clusters as desired
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
data['Cluster'] = kmeans.fit_predict(tfidf_matrix)

# Step 5: Assign Initial Labels to Each Cluster
# Create generic labels, which can be refined based on cluster analysis
cluster_labels = {i: f"Topic_{i+1}" for i in range(num_clusters)}
data['Tag'] = data['Cluster'].map(cluster_labels)

# Step 6: Save to CSV
data[['ID', 'Answer', 'Tag']].to_csv("categorized_answers_with_tags.csv", index=False)

# Optional: Preview clusters to refine labels if needed
for cluster_num in range(num_clusters):
    print(f"Cluster {cluster_num}:")
    print(data[data['Cluster'] == cluster_num]['Answer'].head(5))  # View sample entries per cluster
    print("\n")
