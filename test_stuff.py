from lib.openfood_env import EXPLORER_URL
from lib.openfood_env import THIS_NODE_RADDRESS
from lib.openfood_env import THIS_NODE_WIF

from lib.openfood_env import TEST_GEN_WALLET_PASSPHRASE
from lib.openfood_env import TEST_GEN_WALLET_ADDRESS
from lib.openfood_env import TEST_GEN_WALLET_WIF
from lib.openfood_env import TEST_GEN_WALLET_PUBKEY
from lib.openfood_env import REPORTING_API_BASE_URL
from lib import openfood
from dotenv import load_dotenv
import json
import pytest
load_dotenv(verbose=True)
SCRIPT_VERSION = 0.00010001

RPC = ""

openfood.connect_node()


@pytest.mark.skip
def test_check_sync():
    pass


@pytest.mark.skip
def test_check_peers():
    pass


@pytest.mark.skip
def test_check_recent_transactions():
    pass


@pytest.mark.skip
def test_send_r2r():
    pass


@pytest.mark.skip
def test_send_r2id():
    pass


@pytest.mark.skip
def test_send_id2r():
    pass


@pytest.mark.skip
def test_send_id2id():
    pass


@pytest.mark.skip
def test_send_r2z():
    pass


@pytest.mark.skip
def test_send_z2z():
    pass


@pytest.mark.skip
def test_send_z2r():
    pass


@pytest.mark.skip
def test_send_id2z():
    pass


@pytest.mark.skip
def test_send_z2id():
    pass


@pytest.mark.skip
def test_send_sendtoaddress():
    pass


@pytest.mark.skip
def test_send_z_sendmany():
    pass


@pytest.mark.skip
def test_send_currency():
    pass

