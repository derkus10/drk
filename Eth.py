import time
import requests
from web3 import Web3


infura = "https://mainnet.infura.io/v3/c8b054dcd2b7460ea734ec4fe9984d19"
account_1 = "0xE53eCbbD6Ce77D222E37Cf65C905FbF14245Ab7E"
account_2 = "0x3Cb16b4803754E5fe6c5eFA06b3a741Ea61AC4BB"

# Always delete private key
private_key = "e4bc878c2b6aa03e7c4be04a4ec7d6ae4837e105c6fffb0315c842b109f3943d"

web3 = Web3(Web3.HTTPProvider(infura))

def check_and_send():

    nonce = web3.eth.getTransactionCount(account_1)

    resp = requests.get("https://ethgasstation.info/json/ethgasAPI.json")
    data = resp.json()
    gas_price = data["fast"]/10
    balance = web3.eth.get_balance(account_1)
    gas = 21000
    gas_price_wei = web3.toWei(gas_price, 'gwei')
    value_to_send = balance - (gas_price_wei * gas)
    tx = {
        'nonce': nonce,
        'to': account_2,
        'value':value_to_send,
        'gas': gas,
        'gasPrice': gas_price_wei
    }
    #diff_check = balance-(value_to_send+gas_price_wei*gas)
    #print(""+diff_check)
    try:
        signed_tx = web3.eth.account.signTransaction(tx, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(web3.toHex(tx_hash))
    except Exception as e:
        print(e)


def main_loop():
    while True:
        check_and_send()
        time.sleep(10)  # time in seconds


main_loop()
