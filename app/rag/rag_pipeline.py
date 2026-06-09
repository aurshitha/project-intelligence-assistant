from app.retrieval.retriever import Retriever
from app.retrieval.reranker import Reranker
from app.llm.groq_client import GroqClient
from app.prompts.rag_prompt import build_prompt
from app.router.query_router import QueryRouter
from app.router.filter_extractor import FilterExtractor


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()

        self.reranker = Reranker()

        self.router = QueryRouter()

        self.filter_extractor = FilterExtractor()

        self.llm = GroqClient()

    def answer(
        self,
        question
    ):

        route = self.router.route(
            question
        )

        print(
            f"\nRoute Selected: {route}"
        )

        # ====================================
        # METADATA QUERIES
        # ====================================

        if route == "metadata":

            domain = (
                self.filter_extractor.extract_domain(
                    question
                )
            )

            # --------------------------------
            # Domain Based Filtering
            # --------------------------------

            if domain:

                all_projects = (
                    self.retriever.vector_db
                    .collection
                    .get()
                )

                context = ""

                for meta in all_projects["metadatas"]:

                    project_domain = (
                        meta.get(
                            "domain",
                            ""
                        ).lower()
                    )

                    if domain in project_domain:

                        context += (
                            str(meta)
                            + "\n\n"
                        )

            # --------------------------------
            # Fallback Semantic Retrieval
            # --------------------------------

            else:

                results = (
                    self.retriever.retrieve(
                        question,
                        top_k=10
                    )
                )

                context = ""

                for doc in results["documents"][0]:

                    context += (
                        doc + "\n\n"
                    )

        # ====================================
        # SEMANTIC QUERIES
        # ====================================

        else:

            results = (
                self.retriever.retrieve(
                    question,
                    top_k=10
                )
            )

            documents = (
                results["documents"][0]
            )

            reranked = (
                self.reranker.rerank(
                    question,
                    documents
                )
            )

            top_docs = []

            for doc, score in reranked[:3]:

                if score > 3:
                    top_docs.append(doc)

                if len(top_docs) >= 5:
                    break

            context = "\n\n".join(
                top_docs
            )

        # ====================================
        # LLM ANSWER GENERATION
        # ====================================

        prompt = build_prompt(
            context,
            question
        )

        return self.llm.generate(
            prompt
        )