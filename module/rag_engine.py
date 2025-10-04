# modules/rag_engine.py

from sentence_transformers import SentenceTransformer, util
import pandas as pd

model = SentenceTransformer("all-MiniLM-L6-v2")
faq_df = pd.read_csv("data/health_faq.csv")

def retrieve_answer(query):
    query_embedding = model.encode(query, convert_to_tensor=True)
    faq_df["score"] = faq_df["question"].apply(
        lambda q: util.cos_sim(query_embedding, model.encode(q, convert_to_tensor=True)).item()
    )
    best_match = faq_df.sort_values("score", ascending=False).iloc[0]
    return best_match["answer"]
