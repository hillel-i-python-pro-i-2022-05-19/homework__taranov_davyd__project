from dataclasses import dataclass


@dataclass
class Register:
    user_id: int
    email: str
    password: str


@dataclass
class Login:
    email: str
    password: str


@dataclass
class AddToCart:
    user_id: int
    product_id_and_quantity: dict


@dataclass
class AddToLike:
    user_id: int
    product_id_and_quantity: dict


@dataclass
class Checkout:
    user_id: int
    product_id_and_quantity: dict


@dataclass
class EmailPostForm:
    email: str
    email_text: str


@dataclass
class CreateAComment:
    user_id: int
    comment: str
