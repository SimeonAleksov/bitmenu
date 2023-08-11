import enum
from typing import List

from attrs import define


class Feature(enum.Enum):
    BASIC_SCAN = 1000
    PRO_SCAN = 10000
    BUSINESS_SCAN = 1000000


@define
class ProductMetadata:
    """
    Metadata for a Stripe product.
    """

    stripe_id: str
    name: str
    features: List[str]
    description: str = ''
    is_default: bool = False


BASIC = ProductMetadata(
    stripe_id='prod_OP2FvpWy87JJv3',
    name='Basic',
    description='For small businesses and teams',
    is_default=False,
    features=[
        Feature.BASIC_SCAN,
    ],
)

PRO = ProductMetadata(
    stripe_id='prod_OP2GRl0phm47Z0',
    name='Basic',
    description='For small businesses and teams',
    is_default=False,
    features=[
        Feature.PRO_SCAN,
    ],
)

BUSINESS = ProductMetadata(
    stripe_id='prod_OP2H47tRKbgfXo',
    name='Basic',
    description='For huge businesses and corporations',
    is_default=False,
    features=[
        Feature.BUSINESS_SCAN,
    ],
)
