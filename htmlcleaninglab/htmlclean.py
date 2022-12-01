from bs4 import BeautifulSoup as bs

dirtyArr = []
cleanArr = []


with open('60000512.html', encoding="utf8") as file1, open('60000512_clean.html', encoding="utf8") as file2:
    for file1Line, file2Line in zip(file1, file2):
        if file1Line != file2Line:
            dirtyArr.append(file1Line)
            cleanArr.append(file2Line)

dirtyTest = set(dirtyArr)
temp3 = [x for x in cleanArr if x not in dirtyTest]
print(temp3)

with open('60000512.html', 'rb') as html:
    dirtySoup = bs(html,'html.parser')

with open('60000512_clean.html', 'rb') as html:
    cleanSoup = bs(html,'html.parser')

# print(dirtySoup)