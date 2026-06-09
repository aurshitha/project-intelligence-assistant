class FilterExtractor:

    DOMAINS = [
        "healthcare",
        "pharma",
        "telecom",
        "fintech",
        "banking",
        "retail",
        "manufacturing",
        "logistics",
        "cybersecurity",
        "edtech"
    ]

    def extract_domain(
        self,
        query
    ):

        query = query.lower()

        for domain in self.DOMAINS:

            if domain in query:
                return domain

        return None