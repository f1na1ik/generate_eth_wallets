from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
import csv
import pandas as pd

def generate_wallet(count):
    wallet_list = []
    for _ in range(count):
        mnemonic = Bip39MnemonicGenerator().FromWordsNumber(words_num=12)
        seed = Bip39SeedGenerator(mnemonic).Generate()
        """Purpose всегда равно 44' (это фиксированное значение для BIP44).
        Coin определяет тип криптовалюты (например, 60' для Ethereum).
        Account используется, если у вас есть несколько аккаунтов для одной и той же криптовалюты. В большинстве случаев это значение равно 0'.
        Change используется для разделения адресов для "сдачи" и "публичных" адресов. В случае Ethereum и большинства других криптовалют это значение равно 0
        AddressIndex определяет конкретный адрес внутри аккаунта. Первый адрес имеет индекс 0, второй - индекс 1 и т.д
        В итоге генерируем 1-ый аккаунт MetaMaska.
        """
        wallet = Bip44.FromSeed(seed, Bip44Coins.ETHEREUM).Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
        address = wallet.PublicKey().ToAddress()
        private_key = wallet.PrivateKey().Raw().ToHex()
        wallet_list.append({
            'address': address,
            'private key': private_key,
            'mnemonic': str(mnemonic)
        })
    return wallet_list

def save_to_xlsx_csv(data, file_name):
    df = pd.DataFrame(data)
    df.columns = ['Wallet', 'Private Key', 'Seed Phrases']
    df.to_csv(f'{file_name}.csv', index=False)
    df.to_excel(f'{file_name}.xlsx', index=False)

def save_to_file(data):
    with open('wallets.txt', 'w') as f:
        for wallet in data:
            print(f'{wallet["address"]}')
            f.write(f'{wallet["address"]} \n')

    with open('private_keys.txt', 'w') as f:
        for wallet in data:
            f.write(f'{wallet["private key"]} \n')

    with open('seed_phrase.txt', 'w') as f:
        for wallet in data:
            f.write(f'{wallet["mnemonic"]} \n')


if __name__ == '__main__':
    count = int(input("Введите сколько кошельков надо сгенерировать: "))
    wallet_data = generate_wallet(count)
    save_to_xlsx_csv(wallet_data, 'wallets_with_private')
    save_to_file(wallet_data)
    print(f'Вы сгенерировали {count} кошельков!')
