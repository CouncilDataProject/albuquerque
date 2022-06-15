#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cdp_backend.infrastructure import CDPStack
from pulumi import export

###############################################################################

cdp_stack = CDPStack(
    gcp_project_id="cdp-albuquerque-4009e905",
    municipality_name="Albuquerque",
    firestore_location="us-central",
    hosting_github_url="https://github.com/CouncilDataProject/albuquerque",
    hosting_web_app_address="https://councildataproject.github.io/albuquerque",
    governing_body="city council",
)

export("firestore_address", cdp_stack.firestore_app.app_id)
export("gcp_bucket_name", cdp_stack.firestore_app.default_bucket)
