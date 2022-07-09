from app.models import AddToLike
from app.models.create_a_comment import CreateAComment


def main_function():
    comment = CreateAComment.new_comment(user_id=31, comment='Good goods')
    add_to_like = AddToLike(32, {"fwaf": "fwaf"})

    print(add_to_like.user_id)
    print(comment)
