
# brownie test
from math import floor
import pytest
import brownie
from brownie import ZERO_ADDRESS, accounts, chain, history
from web3.exceptions import ValidationError

# swatch Beat time oracle
# @author Dr. Pixel (github: @Doc-Pixel)

##### test fixtures #####
@pytest.fixture
def beat_contract(getBeat, accounts, scope="module", autouse=True):
    yield accounts[0].deploy(getBeat)

##### tests #####

def test_initial_state(beat_contract):
    # check if it handles current time
    tx = beat_contract.getBeat()
    beatTime = tx.return_value
    assert beatTime <= 999

    # check if it returns a correct value for a passed unixTime (epoch)
    tx = beat_contract.getBeat(1653085620)
    beatTime = tx.return_value
    assert floor(beatTime) == 977

def test_kill(beat_contract):
    tx = beat_contract.disable()
