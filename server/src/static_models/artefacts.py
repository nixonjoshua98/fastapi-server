from __future__ import annotations

from typing import NewType

from pydantic import Field

from src.pymodels import BaseModel

ArtefactID = NewType("ArtefactID", int)


class StaticArtefact(BaseModel):
    id: ArtefactID = Field(..., alias="artefactId")
    bonus_type: int = Field(..., alias="bonusType")
    max_level: int = Field(1_000, alias="maxLevel")
    cost_expo: float = Field(..., alias="costExpo")
    cost_coeff: float = Field(..., alias="costCoeff")
    base_effect: float = Field(..., alias="baseEffect")
    level_effect: float = Field(..., alias="levelEffect")
