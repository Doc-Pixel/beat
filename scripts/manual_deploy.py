import json
from web3 import Web3
from web3.middleware import geth_poa_middleware, attrdict_middleware

# rpcUrl = 'http://5.9.54.235:8545'
# rpcUrl = 'https://rpc.shibrpc.com'
# rpcUrl = 'https://polygon-mainnet.g.alchemy.com/v2/kQdjvW7omb3vqrKU_vdTYyXgLIomw-lZ'
rpcUrl = 'https://shib.nownodes.io/930f09fd-bd28-49e3-bb33-9bdcba825afc'

w3 = Web3()
web3 = Web3(Web3.HTTPProvider(rpcUrl))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

print(web3.eth.get_block_number())

account = web3.eth.account.from_key('340b13fd7ede49f7ba4bf62e137fdb968ec6408f50a0fce2d233bceff320e098')

with open(".build/getBeat.json","r") as file:
    buildFile = json.load(file)

print(type(buildFile))
print(buildFile.keys())

# After compiling the contract, initialize the contract factory:
init_bytecode = buildFile['deploymentBytecode']['bytecode']
abi = buildFile['abi']
myContract = web3.eth.contract(bytecode=init_bytecode, abi=abi)


# def functiontransaction(tx):

#     signed_tx = w3.eth.account.signTransaction(tx, privatekey)
#     tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
#     return w3.eth.waitForTransactionReceipt(tx_hash)
#     tx = contract.functions.setRewardsDuration(1).buildTransaction(
#             {
#                 "from" : wal_address,
#             }
#         )
#     tx_receipt = functiontransaction(tx)


# Deploy a contract using `transact` + the signer middleware:
tx_hash = myContract.constructor(500,'bricktime').transact({"from": account.address})
receipt = web3.eth.get_transaction_receipt(tx_hash)
deployed_addr = receipt["contractAddress"]

