# Testing purpose

from app.ingestion.ppt_parser import PPTParser
from app.ingestion.project_extractor import ProjectExtractor
from app.metadata.extractor import MetadataExtractor
from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.chroma_store import ChromaStore
from app.retrieval.retriever import Retriever
from app.utils.retrieval_text_builder import RetrievalTextBuilder
from app.rag.rag_pipeline import RAGPipeline

# -----------------------------
# Phase 1: Parse PPT
# -----------------------------

ppt_path = "data/ppt/project_repository.pptx"

parser = PPTParser(ppt_path)

slides = parser.extract_slides()

extractor = ProjectExtractor(slides)

projects = extractor.extract_projects()

print(f"\nTotal Projects: {len(projects)}")


# -----------------------------
# Phase 2: Metadata Extraction
# -----------------------------

metadata_extractor = MetadataExtractor()

for project in projects:
    project["metadata"] = metadata_extractor.extract(project)

print("\nSample Project:\n")

print({
    "project_id": projects[0]["project_id"],
    "project_name": projects[0]["project_name"],
    "metadata": projects[0]["metadata"]
})


# -----------------------------
# Phase 3: Embedding + Chroma
# -----------------------------

embedding_model = EmbeddingModel()

vector_db = ChromaStore()

builder = RetrievalTextBuilder()

for project in projects:

    retrieval_text = builder.build(project)

    embedding = embedding_model.get_embedding(
        retrieval_text
    )

    vector_db.add_project(
        project_id=project["project_id"],
        project_name=project["project_name"],
        content=project["content"],
        metadata=project["metadata"],
        embedding=embedding
    )

print(
    f"\nProjects In Chroma: {vector_db.count()}"
)


# -----------------------------
# Phase 4: Retrieval Test
# -----------------------------

print("\n")
print("=" * 60)
print("RETRIEVAL TEST")
print("=" * 60)

retriever = Retriever()

query = "fraud detection"

results = retriever.retrieve(
    query,
    top_k=10
)

print(f"\nQuery: {query}\n")

for metadata, distance in zip(
    results["metadatas"][0],
    results["distances"][0]
):

    # Filter weak matches
    if distance < 0.70:

        print(
            f"{metadata['project_name']}  --> Distance: {distance:.4f}"
        )

print("\n")
print("=" * 60)
print("DOMAIN FILTER TEST")
print("=" * 60)

healthcare_projects = retriever.search_by_domain(
    "Healthcare"
)

print(
    f"\nHealthcare Projects Found: "
    f"{len(healthcare_projects['metadatas'])}"
)

for meta in healthcare_projects["metadatas"]:

    print(
        f"{meta['project_name']} "
        f"--> {meta['domain']}"
    )


# ----------------------------------
# DEBUG ALL DOMAINS
# ----------------------------------

print("\n")
print("=" * 60)
print("ALL AVAILABLE DOMAINS")
print("=" * 60)

all_projects = (
    retriever.vector_db.collection.get()
)

domains = set()

for meta in all_projects["metadatas"]:

    if "domain" in meta:

        domains.add(
            meta["domain"]
        )

for domain in sorted(domains):

    print(domain)


# ----------------------------------
# HEALTHCARE / PHARMA CHECK
# ----------------------------------

print("\n")
print("=" * 60)
print("HEALTHCARE-LIKE PROJECTS")
print("=" * 60)

for meta in all_projects["metadatas"]:

    domain = meta.get(
        "domain",
        ""
    )

    if (
        "health" in domain.lower()
        or
        "pharma" in domain.lower()
    ):

        print(
            f"{meta['project_name']} "
            f"--> {domain}"
        )

rag = RAGPipeline()

response = rag.answer(
    "What solution approach was used for fraud detection?"
)

print("\n")
print("=" * 60)
print("RAG ANSWER")
print("=" * 60)
print(response)