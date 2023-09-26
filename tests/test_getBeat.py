# brownie test
from math import floor
from unicodedata import decimal
import pytest
import ape
from ape import accounts, chain
from web3.exceptions import ValidationError

# swatch Beat time oracle
# @author Dr. Pixel (github: @Doc-Pixel)

system_name = 'beat'
units = 1000

##### test fixtures #####
@pytest.fixture
def owner(accounts):
    return accounts[0]

@pytest.fixture
def not_owner(accounts):
    return accounts[1]
# @pytest.fixture
# def beat_contract(getBeat, accounts, scope="module", autouse=True):
#     yield accounts[0].deploy(getBeat)


@pytest.fixture
def beat_contract(project, owner):
   return owner.deploy(project.getBeat, units, system_name)
##### tests #####

def test_initial_state(beat_contract):
    # check if it handles current time
    assert beat_contract.getBeat() <= 999
    assert beat_contract.getBeat() == beat_contract.getBeat(chain.pending_timestamp)
    assert floor(beat_contract.getBeat(1653085620)) == 977

def test_kill(beat_contract, owner, not_owner):
    with ape.reverts():
        beat_contract.disable(sender=not_owner)
    beat_contract.disable(sender=owner)