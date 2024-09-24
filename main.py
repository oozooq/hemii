from web3 import Web3
import config
import time
import random
from abi import gnosis_abi, swap_abi, erc20_abi

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Підключення до тестової мережі через RPC
web3 = Web3(Web3.HTTPProvider(config.rpc_url))

# Перевірка підключення до мережі
if not web3.is_connected():
    print(f"{RED}Не вдалося підключитися до мережі. Ліміт RPC. Почекай 2-3хв{RESET}")
    exit()

# Отримуємо адресу з приватного ключа
private_key = None
account = None
creator_address = None

def set_account(wallet):
    global account, creator_address, private_key
    private_key = wallet
    account = web3.eth.account.from_key(wallet)
    creator_address = account.address

# Адреса контракту Gnosis Safe Proxy Factory
gnosis_contract_address = web3.to_checksum_address('0xa6B71E26C5e0845f74c812102Ca7114b6a896AB2')
gnosis_contract = web3.eth.contract(address=gnosis_contract_address, abi=gnosis_abi)

# Адреса контракту USDC
usdc_address = web3.to_checksum_address("0xD47971C7F5B1067d25cd45d30b2c9eb60de96443")

# Адреса контракту WETH
weth_address = web3.to_checksum_address("0x0C8aFD1b58aa2A5bAd2414B861D8A7fF898eDC3A")

# Адреса контракту для депозиту
capsule_contract_address = web3.to_checksum_address('0x0C8aFD1b58aa2A5bAd2414B861D8A7fF898eDC3A')

# Адреса вашого смарт-контракту на свап
swap_contract_address = web3.to_checksum_address('0xA18019E62f266C2E17e33398448e4105324e0d0F')
swap_contract = web3.eth.contract(address=swap_contract_address, abi=swap_abi)

# Функція для створення Gnosis Safe
def create_gnosis_safe():
    global private_key
    try:
        singleton_address = web3.to_checksum_address("0x3e5c63644e683549055b9be8653de26e0b4cd36e")
        gnosis_address = str(creator_address).lower()[2:]
        print(gnosis_address)
        intializer = f'b63e800d0000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000000000000000f48f2b2d2a534e402487b3ee7c18c33aec0fe5e40000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000{gnosis_address}0000000000000000000000000000000000000000000000000000000000000000'
        initializer = web3.to_bytes(hexstr=intializer)
        print(initializer)
        #initializer = bytes.fromhex(intializer)
        transaction = gnosis_contract.functions.createProxyWithNonce(
            singleton_address, initializer, web3.eth.get_transaction_count(creator_address)
        ).build_transaction({
            'from': creator_address,
            'gas': config.gas_limit,
            'gasPrice': web3.to_wei(config.gas_price, 'gwei'),
            'nonce': web3.eth.get_transaction_count(creator_address)
        })

        signed_tx = web3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        if tx_receipt['status'] == 1:
            print(f"{GREEN}Сейф створено успішно! Хеш: {tx_receipt['transactionHash'].hex()}{RESET}")
        else:
            print(f"{RED}Транзакцію не вдалося створити.{RESET}")
    except Exception as e:
        print(f"{RED}Сталася помилка при створенні Gnosis Safe: {e}{RESET}")

weth_address = "0x0C8aFD1b58aa2A5bAd2414B861D8A7fF898eDC3A"


def swap_weth_to_usdc():
    global private_key
    try:
        amount_in_weth = 0.005  # Фіксована сума для свапу
        amount_in = web3.to_wei(amount_in_weth, 'ether')
        amount_out_min = web3.to_wei(100, 'mwei')  # Мінімум 100 USDC

        # Параметри для свапу
        commands = bytes.fromhex("0b010c")  # Команди для свапу

        # Статичні інпутси
        inputs = [
            "0x00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000fceb78656306",
            "0x00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000e4e1c00000000000000000000000000000000000000000000000000000fceb7865630600000000000000000000000000000000000000000000000000000000000000a00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002bd47971c7f5b1067d25cd45d30b2c9eb60de964430000640c8afd1b58aa2a5bad2414b861d8a7ff898edc3a000000000000000000000000000000000000000000",
            "0x00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000"
        ]

        deadline = int(time.time()) + 17268145  # Встанови дедлайн

        # Створити параметри для свапу
        transaction = swap_contract.functions.execute(
            commands,
            inputs,
            deadline
        ).build_transaction({
            'from': creator_address,
            'gas': 200000,
            'gasPrice': web3.to_wei('0.00015', 'gwei'),
            'nonce': web3.eth.get_transaction_count(creator_address)
        })

        signed_tx = web3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

        print(f"{GREEN}Свап WETH на USDC відправлено: {tx_hash.hex()}{RESET}")
    except Exception as e:
        print(f"{RED}Сталася помилка при свапі WETH на USDC: {e}{RESET}")

def main(wallet):
    set_account(wallet)
    actions = [swap_weth_to_usdc]

    for action in actions:
        action()
        delay = random.randint(60, 70)  # Затримка від 1 до 3 хвилин
        print(f"Затримка на {delay} секунд...")
        time.sleep(delay)

if __name__ == '__main__':
    DELAY = 1
    with open('./wallets.txt', 'r') as file:
        wallets = [line.strip() for line in file]

    for wallet in wallets:
        main(wallet)
        print(f'Sleep for {DELAY} seconds')
        time.sleep(DELAY)