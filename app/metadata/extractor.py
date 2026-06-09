import re


class MetadataExtractor:

    def extract(self, project):

        text = project["content"]

        metadata = {}

        # Domain
        domain_match = re.search(
            r"Domain\s*\n(.*?)\n",
            text,
            re.IGNORECASE
        )

        # Team Size
        team_match = re.search(
            r"Team Size\s*\n(\d+)",
            text,
            re.IGNORECASE
        )

        # Duration
        duration_match = re.search(
            r"Duration\s*\n(.*?)\n",
            text,
            re.IGNORECASE
        )

        # Project Type
        type_match = re.search(
            r"Type\s*\n(.*?)\n",
            text,
            re.IGNORECASE
        )

        # Technology Stack
        tech_match = re.search(
            r"TECHNOLOGY STACK\s*\n(.*?)\n\n",
            text,
            re.DOTALL | re.IGNORECASE
        )

        technologies = []

        if tech_match:

            tech_string = tech_match.group(1)

            technologies = [
                tech.strip()
                for tech in tech_string.split("·")
                if tech.strip()
            ]

        metadata["domain"] = (
            domain_match.group(1).strip()
            if domain_match else ""
        )

        metadata["team_size"] = (
            int(team_match.group(1))
            if team_match else None
        )

        metadata["duration"] = (
            duration_match.group(1).strip()
            if duration_match else ""
        )

        metadata["project_type"] = (
            type_match.group(1).strip()
            if type_match else ""
        )

        metadata["technology_stack"] = technologies

        return metadata