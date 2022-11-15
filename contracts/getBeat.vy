# @version >=0.3.3
"""
@dev Swatch beat time oracle. Based on the current block timestamp. accuracy depends on block time, about 12 seconds off
@author Dr. Pixel (github: @Doc-Pixel)
"""

owner: address

@external
def __init__():
    """
    @dev set up the contract on deployment
    """
    self.owner = msg.sender

@external
# @view
def getBeat(unixTime: uint256=block.timestamp) -> decimal:
    """
    @dev get the current beat time or calculate the beat time for the provided utcTime
    @param unixTime optional parameter utcTime to convert to beat. Otherwise use block.timestamp as default
    """
    secondsPerDay: decimal = 86400.00  
    epoch: decimal = convert(unixTime + 3600, decimal)  
    epochDays: decimal = epoch / secondsPerDay
    epochWholeDays: decimal = convert(floor(epochDays), decimal)
    dayDiff: decimal = epochDays - epochWholeDays
    partialDayInSeconds: decimal = secondsPerDay * dayDiff
    beatTime : decimal =  (partialDayInSeconds / 86.4)  
    return beatTime

@external
def disable():
    """
    @dev kill function
    """

    assert msg.sender == self.owner, "Only the owner can call this function"
    selfdestruct(owner)
