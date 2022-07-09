from dataclasses import dataclass

from app.typing import T_User_Id


@dataclass
class CreateAComment:
    user_id: T_User_Id
    comment: str

    @classmethod
    def new_comment(cls, user_id: T_User_Id, comment: str) -> str:
        new_comment = {"user_id": user_id, "comment": comment}
        return f"Комментарий: \"{comment}\", от пользователя {user_id=}"
