from dataclasses import dataclass

from app.typing import T_User_Id, T_Product_Id_And_Quantity
from app.models.checkout_like_cart.checkout import Checkout


@dataclass
class AddToCart(Checkout):
    ...
