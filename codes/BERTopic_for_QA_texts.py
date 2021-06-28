
"""
Some modules & models should be installed in advance.
BERTopic general: !pip install bertopic[all]
BERTopic vsiual tools: !pip install bertopic[visualization]
BERTopic flair: c!pip install bertopic[flair]

"""

from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
# you can choose to use other embeddingmodels, such as KoElectra
#koelectra = TransformerDocumentEmbeddings('kykim/electra-kor-base')
sentence_model = SentenceTransformer("distiluse-base-multilingual-cased-v1")


###############################################################################
if __name__ == '__main__':
    import pickle
    with open(r'.\keyword_results.txt', 'rb') as f:
        results = pickle.load(f)
    with open(r'./keyword_checks.txt', 'rb') as f:
        checks = pickle.load(f)
    
    Sen_model = BERTopic(embedding_model=sentence_model, nr_topics='auto',
                           calculate_probabilities=True, top_n_words = 15, min_topic_size=50)
    Sen_topics, Sen_probs = Sen_model.fit_transform(checks)

    Sen_fig = Sen_model.visualize_topics()
    Sen_fig.write_html("Sen_keyword.html")

    Sen_model.get_topic_info()

    dates = [x for x in results['date']]
    timestamps = [x.replace('.', '-') for x in dates]

    topics_over_time_a = Sen_model.topics_over_time(checks, Sen_topics, timestamps)
    fig_topics_over_time = Sen_model.visualize_topics_over_time(topics_over_time_a, top_n=20)
    fig_topics_over_time.write_html("r./Sen_fig_topics_over_time_all.html")


