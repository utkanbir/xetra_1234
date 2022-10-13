"""
File to store constants
"""

from enum import Enum


class S3FileTypes(Enum):
    """
    Supported file types for ...
    """
    CSV ='csv'
    PARQUET='parquet'
    