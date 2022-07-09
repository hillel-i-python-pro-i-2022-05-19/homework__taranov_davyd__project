from dataclasses import dataclass

from app.typing import T_User_Id, T_Email, _T_Password


@dataclass
class Register:
    user_id: T_User_Id
    email: T_Email
    password: _T_Password
