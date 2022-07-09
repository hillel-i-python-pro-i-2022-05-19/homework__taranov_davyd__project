from dataclasses import dataclass

from app.typing import T_Email, _T_Password


@dataclass
class Login:
    email: T_Email
    password: _T_Password
