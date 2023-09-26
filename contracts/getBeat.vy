# @version >=0.3.6
"""
@dev Swatch beat time oracle. Based on the current block timestamp. accuracy depends on block time, about 12 seconds off
@author Dr. Pixel (github: @Doc-Pixel)
"""

owner: address
status: public(bool)

SECONDS_PER_DAY: constant(decimal) = 86400.00  
NUMBER_OF_UNITS: immutable(decimal)
DIVISION_KEY: immutable(decimal)
SYSTEM_NAME: immutable(String[64])

@external
def __init__(units: uint256, system_name: String[64]):
    """
    @dev set up the contract on deployment
    """
    self.owner = msg.sender
    NUMBER_OF_UNITS  = convert(units, decimal)
    DIVISION_KEY = SECONDS_PER_DAY / NUMBER_OF_UNITS
    SYSTEM_NAME = system_name

@internal
@view
def _calculateBeat(unixTime: uint256) -> decimal:
    """
    @dev get the current beat time or calculate the beat time for the provided utcTime
    @param unixTime optional parameter utcTime to convert to beat. Otherwise use block.timestamp as default
    """
    assert not self.status
    
    epoch: decimal = convert(unixTime + 3600, decimal)  
    epochDays: decimal = epoch / SECONDS_PER_DAY
    epochWholeDays: decimal = convert(floor(epochDays), decimal)
    dayDiff: decimal = epochDays - epochWholeDays
    partialDayInSeconds: decimal = SECONDS_PER_DAY * dayDiff
    beatTime : decimal =  (partialDayInSeconds / DIVISION_KEY)  
    return beatTime

@external
@view
def getBeat(unixTime: uint256=block.timestamp) -> uint256:
    return convert(floor(self._calculateBeat(unixTime)), uint256)

@external
@view
def getBeatDecimals(decimals: uint256, unixTime: uint256=block.timestamp) -> (uint256, uint256):
    decimals_dec: decimal = convert(decimals, decimal)
    beats: uint256 = convert(floor(self._calculateBeat(unixTime) * decimals_dec), uint256)
    return beats, decimals

@external
def withDraw():
    send(self.owner, self.balance)

@external
def setStatus(status:bool) -> bool:
    self.status = status
    return self.status

@external
def disable():
    """
    @dev kill function
    """

    assert msg.sender == self.owner, "Only the owner can call this function"
    selfdestruct(self.owner)
