from .models.base import Base
from .api import payments

from .api import campaigns, donates, other



class KeksikAPI(Base):

    @property
    def donates(self) -> donates.DonatesCategory:
        return donates.DonatesCategory(self.token, self.group_id)
    
    @property
    def campaigns(self) -> campaigns.СampaignsCategory:
        return campaigns.СampaignsCategory(self.token, self.group_id)
    
    @property
    def payments(self) -> payments.PaymentsCategory:
        return payments.PaymentsCategory(self.token, self.group_id)
    
    @property
    def other(self) -> other.OtherCategory:
        return other.OtherCategory(self.token, self.group_id)