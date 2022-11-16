
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
    assert beat_contract.getBeat() <= 999
    assert beat_contract.getBeat() == beat_contract.getBeat(chain.time())
    assert floor(beat_contract.getBeat(1653085620)) == 977

def test_kill(beat_contract):
    tx = beat_contract.disable()
