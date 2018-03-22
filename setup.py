import random
import traceback
import inspect
import math
from servers import StorageServer, PublicKeyServer
from crypto import Crypto
from base_client import IntegrityError
from run_part1_tests import run_part1_tests

argspec = inspect.getargspec(t)
if argspec.defaults is None:
    types = {}
else:
    types = dict(zip(argspec.args[-len(argspec.defaults):],
                     argspec.defaults))

server = types['server']() if 'server' in types else StorageServer()
pks = types['pks']() if 'pks' in types else PublicKeyServer()
crypto = types['crypto']() if 'crypto' in types else Crypto()
myclient = __import__(self.theclass, fromlist=[''])

def C(name):
    return myclient.Client(server, pks, crypto, name)

# alice = C("alice")
# bob = C("bob")
# alice.upload("k", "v")
# m = alice.share("bob", "k")
# if not isinstance(m, str):
#     return 0.0
# bob.receive_share("alice", "k", m)
# return float(bob.download("k") == "v")