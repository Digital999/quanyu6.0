import pypinyin
def word(dizhi):
    s = ''
    for i in pypinyin.pinyin(dizhi, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s