import os
from typing import NamedTuple

from github import Auth, Github


class LabelT(NamedTuple):
    name: str
    color: str
    description: str = ""


labels: list[LabelT] = [
    LabelT(
        name="p: critical",
        description="Priority: critical - must be worked on immediately",
        color="B60205",
    ),
    LabelT(
        name="p: high",
        description="Priority: high - should be worked on as soon as reasonable",
        color="4E0000",
    ),
    LabelT(
        name="p: medium",
        description="Priority: medium - should be worked on in the near future",
        color="8B2D33",
    ),
    LabelT(
        name="p: low",
        description="Priority: low - can be worked on anytime in the future",
        color="AB494C",
    ),
    LabelT(
        name="t: bug",
        description="Type: bug - something is broken and requires fixing",
        color="F6AA17",
    ),
    LabelT(
        name="t: unconfirmed bug",
        description="Type: unconfirmed bug - needs testing to confirm if applicable",
        color="F9F871",
    ),
    LabelT(
        name="t: enhancement",
        description="Type: enhancement - a new feature or request for a feature",
        color="27E4DF",
    ),
    LabelT(
        name="t: meta",
        description="Type: meta - not covered by another type",
        color="B3CEBA",
    ),
    LabelT(
        name="t: refactor",
        description="Type: refactor - relates to changes which aren't a bug or new feature",
        color="EF6C73",
    ),
    LabelT(
        name="t: test",
        description="Type: test - relates to the test suite",
        color="2A36AB",
    ),
    LabelT(
        name="t: docs",
        description="Type: docs - relates to the project documentation",
        color="AB267B",
    ),
    LabelT(
        name="duplicate",
        description="This issue or pull request already exists",
        color="cfd3d7",
    ),
    LabelT(
        name="good first issue", description="Good/easy for newcomers", color="7057ff"
    ),
    LabelT(name="wont fix", description="This will not be worked on", color="ffffff"),
    LabelT(
        name="pending information",
        description="This issue is incomplete and requires further information",
        color="d876e3",
    ),
    LabelT(name="invalid", description="This doesn't seem right", color="e4e669"),
]

REPO_NAME: str = ""
DELETE_EXISTING: bool = True


auth = Auth.Token(os.environ["TOKEN"])
github = Github(auth=auth)
repo = github.get_user().get_repo(REPO_NAME)

if DELETE_EXISTING:
    for label in repo.get_labels():
        label.delete()

for new_label in labels:
    repo.create_label(
        name=new_label.name,
        color=new_label.color,
        description=new_label.description,
    )

print("All done")
