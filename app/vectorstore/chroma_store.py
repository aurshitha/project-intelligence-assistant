import chromadb


class ChromaStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="project_repository"
        )

    def add_project(
        self,
        project_id,
        project_name,
        content,
        metadata,
        embedding
    ):

        self.collection.add(
            ids=[project_id],

            documents=[content],

            metadatas=[
                {
                    "project_name": project_name,
                    **metadata
                }
            ],

            embeddings=[embedding]
        )

    def count(self):

        return self.collection.count()