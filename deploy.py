import json
from solcx import compile_standard, install_solc
from web3 import Web3, web3

# In the video, we forget to `install_solc`
# from solcx import compile_standard


with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# We add these two lines that we forgot from the video!
print("Installing...")
install_solc("0.6.0")

# Solidity source code
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

w3 = Web3(Web3.HTTPProvider("http://0.0.0.0:7545"))
chain_id = 1337
my_address = "0xc898Bb4fb6d0Bd5269F5915927A513c3131D10d0"
private_key = "0x8f4158f0b9e1aa376877a8092a93ec28768c8fc8895c545a8a76cdc77c4d284b"

SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
nonxw = w3.eth.getTranscationCount(my_address)
