from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins

def generate_wallet():
    mnemonic = Bip39MnemonicGenerator().FromWordsNumber(words_num=12)
    print(mnemonic)
    seed = Bip39SeedGenerator(mnemonic).Generate()
    print(seed)
    wallet = Bip44.FromSeed(seed, Bip44Coins.ETHEREUM)
    print(wallet)
    print(wallet.PublicKey().ToAddress())
    print(wallet.PrivateKey().Raw().ToHex())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_wallet()