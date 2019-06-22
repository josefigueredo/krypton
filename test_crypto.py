#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from crypto import Krypton
import csv
from colorama import init, Fore, Back, Style

__author__     = 'Jose Figueredo'
__copyright__  = 'Jose Figueredo 2019'
__credits__    = ['Jose Figueredo']
__license__    = 'Corporative'
__version__    = '1.0.1'
__maintainer__ = 'Jose Figueredo'
__email__      = "josefigueredo@gmail.com"
__status__     = "Production"


def test_decrypt_decrypt():
    '''  '''
    key  = '3532414233323B5E2421455239343938384F505333573231'
    iv   = '5459353441424358'
    data = '20000000001223543'
    encrypted, decrypted = None, None

    init() # Colorama
    print(Fore.GREEN + 'Inicia test_decrypt_decrypt' + Style.RESET_ALL)

    try:
        print('Data:      ' + data)
        krypton = Krypton(key, iv)
        encrypted = krypton.encrypt(data)
        print('Encrypted: ' + encrypted)
        decrypted = krypton.decrypt(encrypted)
        print('Decrypted: ' + decrypted)
    except Exception as e:
        print(Fore.RED + e + Style.RESET_ALL)

    assert data == decrypted, 'Should be equals'
    print(Fore.GREEN + 'Test passed !!' + Style.RESET_ALL)

def test_decrypt_decrypt_csv():
    '''  '''
    key  = '3532414233323B5E2421455239343938384F505333573231'
    iv   = '5459353441424358'
    encrypted, decrypted = None, None

    init() # Colorama
    print(Fore.GREEN + 'Inicia test_decrypt_decrypt_csv' + Style.RESET_ALL)

    try:
        krypton = Krypton(key, iv)

        with open('employee_file.csv', mode='w') as test_file:
            for index in range(100000):
                employee_writer = csv.writer(test_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                row = [index, krypton.encrypt(str(index))]
                employee_writer.writerow(row)

        with open('employee_file.csv', mode='r') as test_file:
            csv_reader = csv.reader(test_file, delimiter=';')
            for row in csv_reader:
                decrypted = krypton.decrypt(row[1])

    except Exception as e:
        print(Fore.RED + str(e) + Style.RESET_ALL)

    print(Fore.GREEN + 'Test passed !!' + Style.RESET_ALL)


test_decrypt_decrypt()
test_decrypt_decrypt_csv()
