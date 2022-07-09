from dataclasses import dataclass

from app.typing import T_Email


@dataclass
class EmailPostForm:
    email: T_Email
    email_text: str
