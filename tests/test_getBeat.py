
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

# @pytest.fixture(autouse=True)
# def isolation(fn_isolation):
#     pass


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

    # tx = beat_contract.getBeat(1653085620)
    # assert type(tx.return_value) == class 'NoneType'
    
# def test_killed(beat_contract):
#     tx = beat_contract.getBeat()
#     # assert tx.block_number != 2349805423905
#     assert len(history[0].subcalls) == 12312321
#     # assert tx.selfdestruct