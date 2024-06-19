import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.tokenize.treebank import TreebankWordDetokenizer

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample FAQs
faq = {
    "What features does SmartGadget have?": "SmartGadget includes Bluetooth connectivity, a high-resolution touchscreen, and voice-command functionality.",
    "How do I reset SmartGadget?": "To reset SmartGadget, press and hold the power button for 10 seconds until it restarts.",
    "Where can I buy SmartGadget?": "SmartGadget is available for purchase on our official website and selected retail stores."
}

# Preprocess the FAQs
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    return TreebankWordDetokenizer().detokenize(filtered_tokens)

processed_faqs = {preprocess_text(question): answer for question, answer in faq.items()}

# Vectorize FAQ questions
vectorizer = TfidfVectorizer()
faq_questions = list(processed_faqs.keys())
X = vectorizer.fit_transform(faq_questions)

def get_response(user_query):
    # Preprocess user query
    preprocessed_query = preprocess_text(user_query)
    
    # Vectorize user query
    query_vector = vectorizer.transform([preprocessed_query])
    
    # Calculate cosine similarity between query and FAQ questions
    similarities = cosine_similarity(query_vector, X).flatten()
    
    # Get the index of the most similar FAQ question
    most_similar_idx = similarities.argmax()
    
    # Return corresponding FAQ answer
    return faq[faq_questions[most_similar_idx]]

# Example usage:
user_query = "What are the features of SmartGadget?"
response = get_response(user_query)
print(response)
