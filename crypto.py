#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
from Crypto.Cipher import DES3

__author__     = 'Jose Figueredo'
__copyright__  = 'Jose Figueredo 2019'
__credits__    = ['Jose Figueredo']
__license__    = 'Corporative'
__version__    = '1.0.1'
__maintainer__ = 'Jose Figueredo'
__email__      = "josefigueredo@gmail.com"
__status__     = "Production"


class Krypton(object):
    '''  '''

    def __init__(self, key, iv):
        '''  '''
        self.key_hex = bytes.fromhex(key)
        self.iv_hex  = bytes.fromhex(iv)

    def encrypt(self, raw):
        '''  '''
        padded    = self._pad(raw)
        cipher    = DES3.new(self.key_hex, DES3.MODE_CBC, self.iv_hex)
        encrypted = cipher.encrypt(padded)
        base64d   = base64.b64encode(encrypted); 
        utf8d     = base64d.decode('utf-8')
        return utf8d

    def decrypt(self, data):
        '''  '''
        debase64d = base64.b64decode(data)
        cipher    = DES3.new(self.key_hex, DES3.MODE_CBC, self.iv_hex)
        decrypted = cipher.decrypt(debase64d)
        unpadded  = self._unpad(decrypted)
        utf8d     = unpadded.decode('utf-8')
        return utf8d

    @staticmethod
    def _pad(data):
        '''  '''
        pad_len = DES3.block_size - len(data) % DES3.block_size
        padding = chr(pad_len) * pad_len
        padded  = data + padding
        return padded

    @staticmethod
    def _unpad(data):
        '''  '''
        cnt_char = data[len(data)-1:]
        pad_len  = ord(cnt_char)
        unpadded = data[:-pad_len]
        return unpadded