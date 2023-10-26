from ..http_client.request import HttpClient
from ..models.base import Base

from ..models.models import BalanceModel


class OtherCategory(Base):
    async def balance(self) -> BalanceModel:
        api_method: str = 'balance'
        http_method: str = 'POST'
        data: dict = {
            'group': self.group_id,
            'token': self.token,
            'v': self.v
        }

        outcome: dict = await HttpClient.request(api_method, http_method, data=data)
        return BalanceModel(**outcome)