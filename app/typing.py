from typing import TypeAlias

T_User_Id: TypeAlias = int
T_Email: TypeAlias = str
_T_Password: TypeAlias = str

T_Product_Id: TypeAlias = int
T_Quantity: TypeAlias = int

T_Product_Id_And_Quantity: TypeAlias = {T_Product_Id: T_Quantity}
