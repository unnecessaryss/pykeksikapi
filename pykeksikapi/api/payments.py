from ..http_client.request import HttpClient
from ..models.base import Base

from ..models.models import PaymentsGetModel, PaymentsCreateModel


class PaymentsCategory(Base):
    async def get(self, ids: list = []):
        api_method: str = 'payments/get'
        http_method: str = 'POST'
        data: dict = {
            'group': self.group_id,
            'token': self.token,
            'v': self.v,
            'ids': ids
        }

        outcome: dict = await HttpClient.request(api_method, http_method, data=data)
        return PaymentsGetModel(**outcome)
    
    
    async def create(self, system: str, purse: str, amount: int, name: str = None):
        api_method: str = 'payments/create'
        http_method: str = 'POST'
        data: dict = {
            'group': self.group_id,
            'token': self.token,
            'v': self.v,
            'system': system,
            'purse': purse,
            'amount': amount,
            'name': name
        }

        outcome: dict = await HttpClient.request(api_method, http_method, data=data)
        return PaymentsCreateModel(**outcome)