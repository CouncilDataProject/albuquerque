#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from typing import List

from cdp_backend.pipeline.ingestion_models import EventIngestionModel
from cdp_scrapers.legistar_utils import LegistarScraper

###############################################################################


def get_events(
    from_dt: datetime,
    to_dt: datetime,
    **kwargs,
) -> List[EventIngestionModel]:
    scraper = LegistarScraper(
        client="cabq",
        timezone="America/Denver",
        ignore_minutes_item_patterns=[
            "Please refer to the statement",
            "The Council will take a dinner break at approximately",
            "To provide virtual public comments to the Council everyone",
            "Members of the public will have the ability to view the meeting",
            "The Council will take General Public Comment on any topic",
            "Following Center for Disease Control and Prevention",
            "To provide public comments to the Council",
            "Public Comment Sign Up for",
            "we are encouraging members of the public that attend the meeting",
            "by completing this web form",
            "Attention: Following Center for Disease Control and Prevention",
            "For members of the public without internet service",
        ],
    )

    return scraper.get_events(begin=from_dt, end=to_dt)
