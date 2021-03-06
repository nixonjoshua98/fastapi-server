from fastapi import Depends

from src.handlers import UpgradeArmouryItemHandler, UpgradeItemResponse
from src.handlers.auth_handler import (AuthenticatedRequestContext,
                                       get_authenticated_context)
from src.response import ServerResponse
from src.router import APIRouter
from src.shared_models import BaseModel
from src.static_models.armoury import ArmouryItemID


class ArmouryItemActionModel(BaseModel):
    item_id: ArmouryItemID


router = APIRouter()


@router.post("/upgrade")
async def upgrade(
    data: ArmouryItemActionModel,
    user: AuthenticatedRequestContext = Depends(get_authenticated_context),
    handler: UpgradeArmouryItemHandler = Depends(),
):
    resp: UpgradeItemResponse = await handler.handle(user, data.item_id)

    return ServerResponse({
        "item": resp.item,
        "upgradeCost": resp.upgrade_cost,
        "currencyItems": resp.currencies,
    })
