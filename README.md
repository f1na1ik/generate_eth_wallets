# generate_eth_wallets
Программа генерирует кошельки для Ethereum с использованием мнемонических фраз и сохраняет информацию о них в различных файлах. Сгенерированные кошельки соответствуют стандарту BIP-44 для Ethereum.

```wallets.txt``` - файл только с **кошельками**        
```private_keys.txt``` - файл только с **приватными ключами**       
```seed_phrase.txt``` - файл только с **сид фразами**       

```wallets_with_private.csv``` - csv файл с данными **кошелек - приватник - сид фраза**  
```wallets_with_private.xlsx``` - xlsx (excel) файл с даннами **кошелек - приватник - сид фраза**


# Установка
Для работы программы необходимо установить следующие библиотеки:

```pip install bip_utils``` - библиотека, содержащая утилиты для работы с BIP (Bitcoin Improvement Proposal) и генерации кошельков.    
```pip install pandas``` - библиотека для анализа и обработки данных.

**или** 

```pip install -r requirements.txt``` (установит автоматически из requirements.txt)

Так же для библиотеки bip_utils необходимо будет установить [Visual Studio Build Tootls](https://visualstudio.microsoft.com/ru/visual-cpp-build-tools/) выбрать **разработка классических приложений на C++**
