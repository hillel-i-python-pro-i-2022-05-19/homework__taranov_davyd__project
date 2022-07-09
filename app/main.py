from modeles.create_a_comment import CreateAComment


def main_function():
    comment = CreateAComment.new_comment(user_id=31, comment='Good goods')
    print(comment)
