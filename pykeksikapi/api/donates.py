from ..http_client.request import HttpClient
from ..models.base import Base

from ..models.models import (
    GetDonateModel,
    ChangeStatusModel,
    AnswerModel,
    ChangeRewardStatusModel
)

import json


class DonatesCategory(Base):
    async def get(
        self,
        len: int = None,
        offset: int = None,
        start_date: int = None,
        end_date: int = None,
        sort: str = 'date',
        reverse: bool = False,
    ) -> GetDonateModel:
        
        api_method: str = 'donates/get'
        http_method: str = 'POST'
        data: dict = json.dumps(
            {
            "token": self.token,
            "group": self.group_id,
            "v": self.v,
            "len": len,
            "offset": offset,
            "start_date": start_date,
            "end_date": end_date,
            "sort": sort,
            "reverse": reverse
            }
        )

        outcome: dict = await HttpClient.request(api_method, http_method, data=data)
        return GetDonateModel(**outcome)

    async def get_last(self, last_id: int) -> GetDonateModel:

        api_method: str = 'donates/get-last'
        http_method: str = 'POST'
        data: dict = json.dumps(
            {
            'group': self.group_id,
            'token': self.token,
            'v': self.v,
            'last_id': last_id
            }
        )

        outcome: dict = await HttpClient.request(api_method, http_method, data=data)
        return GetDonateModel(**outcome)
    
    async def change_status(self, id: int, status: str) -> ChangeStatusModel:

        api_method: str = 'donates/change-status'
        http_method: str = 'POST'
        data: dict = json.dumps(
            {
            'group': self.group_id,
            'token': self.token,
            'v': self.v,
            'id': id,
            'status': status
            }
        )

        outcome: dict = await HttpClient.request(api_method, http_method, data=data)
        return ChangeStatusModel(**outcome)
    
    async def answer(self, id: int, answer: str):

        api_method: str = 'donates/answer'
        http_method: str = 'POST'
        data: dict = json.dumps(
            {
            'group': self.group_id,
            'token': self.token,
            'v': self.v,
            'id': id,
            'answer': answer
            }
        )

        outcome: dict = await HttpClient.request(api_method, http_method, data=data)
        return AnswerModel(**outcome)

    async def change_reward_status(self, id: int, status: str):

        api_method: str = 'donates/change-reward-status'
        http_method: str = 'POST'
        data: dict = json.dumps(
            {
            'group': self.group_id,
            'token': self.token,
            'v': self.v,
            'id': id,
            'status': status
            }
        )

        outcome: dict = await HttpClient.request(api_method, http_method, data=data)
        return ChangeRewardStatusModel(**outcome)