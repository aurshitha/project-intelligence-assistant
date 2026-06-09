class QueryRouter:

    def route(self, query):

        query = query.lower()

        metadata_keywords = [

            "all projects",
            "list projects",
            "show projects",

            "team size",
            "duration",

            "domain",

            "technology stack",
            "tech stack",
            "technology",

            "aws",
            "azure",
            "gcp",
            "python",


            "healthcare",
            "pharma",
            "telecom",
            "fintech",
            "retail",
            "manufacturing",

            "under",
            "less than",

            "large language model",
            "llm",
            "nlp"
        ]

        for keyword in metadata_keywords:

            if keyword in query:
                return "metadata"

        return "semantic"