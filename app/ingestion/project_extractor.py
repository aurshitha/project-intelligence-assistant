import re


class ProjectExtractor:

    def __init__(self, slides):
        self.slides = slides

    def extract_projects(self):

        projects = []

        # Skip cover slide
        project_slides = self.slides[1:]

        for i in range(0, len(project_slides), 2):

            try:

                slide1 = project_slides[i]
                slide2 = project_slides[i + 1]

                combined_text = (
                    slide1["content"] + "\n" +
                    slide2["content"]
                )

                project_id_match = re.search(
                    r"(P\d{3})",
                    slide1["content"]
                )

                project_name_match = re.search(
                    r"P\d{3}\s*\n(.*?)\n",
                    slide1["content"]
                )

                project_id = (
                    project_id_match.group(1)
                    if project_id_match
                    else "UNKNOWN"
                )

                project_name = (
                    project_name_match.group(1).strip()
                    if project_name_match
                    else "UNKNOWN"
                )

                project = {
                    "project_id": project_id,
                    "project_name": project_name,
                    "slides": [
                        slide1["slide_number"],
                        slide2["slide_number"]
                    ],
                    "content": combined_text
                }

                projects.append(project)

            except Exception:
                continue

        return projects