from ape import accounts, project

account = accounts.load("bricktime")

# Assume your project has a contract named 'MyContract' with constructor that accepts argument '123'.
contract = project.getBeat.deploy(500, "BRICKTIME", sender=account)
project.track_deployment(contract)
