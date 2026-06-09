class RetrievalTextBuilder:

    def build(self, project):

        metadata = project.get(
            "metadata",
            {}
        )

        text = f"""
Project Name:
{project['project_name']}

Project Type:
{metadata.get('project_type', '')}

Domain:
{metadata.get('domain', '')}

Content:
{project['content']}
"""

        return text