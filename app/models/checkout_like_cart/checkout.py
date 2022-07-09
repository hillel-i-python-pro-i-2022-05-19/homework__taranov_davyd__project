from dataclasses import dataclass

from app.typing import T_User_Id, T_Product_Id_And_Quantity


@dataclass
class Checkout:
    user_id: T_User_Id
    product_id_and_quantity: T_Product_Id_And_Quantity
