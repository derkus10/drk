from web3 import Web3


infura = "https://ropsten.infura.io/v3/c8b054dcd2b7460ea734ec4fe9984d19"

web3 = Web3(Web3.HTTPProvider(infura))


account_1 = "0x3Cb16b4803754E5fe6c5eFA06b3a741Ea61AC4BB"
account_2 = ""

#Always delete private key 
private_key = "e4bc878c2b6aa03e7c4be04a4ec7d6ae4837e105c6fffb0315c842b109f3943d"

nonce = web3.eth.getTransactionCount(account_1)

tx = {
'nonce': nonce,
'to': account_2,
'value': web3.toWei(0.005, 'ether'),
'gas': 21000,
'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
