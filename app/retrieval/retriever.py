from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.chroma_store import ChromaStore


class Retriever:

    def __init__(self):

        self.embedding_model = EmbeddingModel()
        self.vector_db = ChromaStore()

    # -------------------------
    # Semantic Search
    # -------------------------

    def retrieve(self, query, top_k=10):

        query_embedding = self.embedding_model.get_embedding(
            query
        )

        results = self.vector_db.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )

        return results

    # -------------------------
    # Domain Filter
    # -------------------------

    def search_by_domain(self, domain):

        results = self.vector_db.collection.get(
            where={
                "domain": domain
            }
        )

        return results

    # -------------------------
    # Project Type Filter
    # -------------------------

    def search_by_project_type(
        self,
        project_type
    ):

        results = self.vector_db.collection.get(
            where={
                "project_type": project_type
            }
        )

        return results

    # -------------------------
    # Team Size Filter
    # -------------------------

    def search_by_team_size(
        self,
        max_size
    ):

        all_projects = (
            self.vector_db.collection.get()
        )

        filtered = []

        for meta in all_projects["metadatas"]:

            if (
                meta.get("team_size")
                and
                meta["team_size"] < max_size
            ):
                filtered.append(meta)

        return filtered