from typing import Optional, Any, List

from tests.api_tests.data.config_class import BaseModel


class Prepared(BaseModel):
    closevalue: str
    change: str
    value1: str
    value2: str
    maxDealDate: str


class Item(BaseModel):
    id: str
    ticker: str
    ticker_id: str
    name: str
    subname: Optional[str]
    hide_subname: bool
    arrows: bool
    change: Optional[float]
    data_type: str
    url: str
    border_after: bool
    popup_window: Optional[str]
    color: str
    closevalue: Optional[float]
    value1: Optional[float]
    value2: Optional[float]
    prepared: Prepared


class SharedKeyIndicatorsUnderToplineItem(BaseModel):
    position: int
    flag: str
    flag2: Any
    integer: int
    item: Item


class Prepared1(BaseModel):
    closevalue: str
    change: str
    value1: str
    value2: str
    maxDealDate: str


class Item1(BaseModel):
    id: str
    ticker: str
    ticker_id: str
    name: str
    subname: Optional[str]
    hide_subname: bool
    arrows: bool
    change: Optional[float]
    data_type: str
    url: str
    border_after: bool
    popup_window: Optional[str]
    color: str
    closevalue: Optional[float]
    value1: Optional[float]
    value2: Optional[float]
    prepared: Prepared1


class SharedKeyIndicator(BaseModel):
    position: int
    flag: str
    flag2: Any
    integer: int
    item: Item1


class Tickers(BaseModel):
    shared_key_indicators_under_topline: List[SharedKeyIndicatorsUnderToplineItem]
    shared_key_indicators: List[SharedKeyIndicator]
