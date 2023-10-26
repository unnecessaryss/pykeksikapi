from pydantic import BaseModel
from typing import List


class RewardItem(BaseModel):
    id: int
    title: str
    status: str

class DonateItem(BaseModel):
    id: int
    user: int
    date: int
    amount: int
    total: int = None
    msg: str = None
    anonym: bool
    answer: str = None
    vkpay: bool
    status: str
    reward: List['RewardItem'] = None
    op: int = None

class GetDonateModel(BaseModel):
    success: bool
    error: int = None
    msg: str = None
    list: List['DonateItem'] = []

class ChangeStatusModel(BaseModel):
    success: bool
    error: int = None
    msg: str = None

class AnswerModel(BaseModel):
    success: bool
    error: int = None
    msg: str = None

class ChangeRewardStatusModel(BaseModel):
    success: bool
    error: int = None
    msg: str = None

class BalanceModel(BaseModel):
    success: bool
    error: int = None
    msg: str = None
    balance: int = None

class PaymentItem(BaseModel):
    id: int
    status: str
    processed: int
    system: str
    purse: str
    amount: int
    user: int

class PaymentsGetModel(BaseModel):
    success: bool
    error: int = None
    msg: str = None
    list: List['PaymentItem'] = []

class PaymentsCreateModel(BaseModel):
    success: bool
    error: int = None
    msg: str = None
    id: int


_locals = locals().copy()
_locals_values = _locals.values()

for item in _locals_values:
    if not (isinstance(item, type) and issubclass(item, BaseModel)):
        continue
    item.update_forward_refs(**_locals)
    for parent in item.__bases__:
        if parent.__name__ == item.__name__:
            parent.__fields__.update(item.__fields__) 
            parent.update_forward_refs(**_locals)