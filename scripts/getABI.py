import json
from pprint import pprint as pp

with open(".build/getBeat.json","r") as file:
    buildFile = json.load(file)

print(type(buildFile))
print(buildFile.keys())

# After compiling the contract, initialize the contract factory:
init_bytecode = buildFile['deploymentBytecode']['bytecode']
abi = buildFile['abi']

pp(abi)