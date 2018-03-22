import random
import traceback
import inspect
import math
import client
from servers import StorageServer, PublicKeyServer
from crypto import Crypto
from base_client import IntegrityError
from run_part1_tests import run_part1_tests

server = StorageServer()
pks = PublicKeyServer()
crypto = Crypto()

def C(name):
    return client.Client(server, pks, crypto, name)

# example test1:

# alice = C("alice")
# bob = C("bob")
# alice.upload("k", "v")
# m = alice.share("bob", "k")
# if not isinstance(m, str):
#     return 0.0
# bob.receive_share("alice", "k", m)
# return float(bob.download("k") == "v")