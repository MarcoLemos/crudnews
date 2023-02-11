from datetime import datetime
from typing import Optional

from odmantic import Field, Model


class Articles(Model):
    title: str
    content: str
    created: datetime = Field(default_factory=datetime.now)
    modified: Optional[datetime]
