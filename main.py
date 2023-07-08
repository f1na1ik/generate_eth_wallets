from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
import csv
import pandas as pd

def generate_wallet():
    wallet_list = []
    #for _ in range(count):
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

    return {
        'address': address,
        'private key': private_key,
        'mnemonic': str(mnemonic)
    }
    #print(wallet_list)




    # with open('wallets.csv', 'w') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([address, private_key, mnemonic])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    wallet_data = generate_wallet()
    print(wallet_data)
    df = pd.DataFrame([wallet_data], columns=['address', 'private key', 'mnemonic'])
    df.columns = ['Wallets', 'Private Key', 'Seed Phrases']
    df.to_csv('wallets.csv', index=False)
    df.to_excel('wallets.xlsx', index=True)