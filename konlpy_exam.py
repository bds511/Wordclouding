#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from konlpy.tag import Kkma, Twitter
from konlpy.utils import pprint
kkma = Twitter()


doc_ko = open("chosun_snr.txt", 'r')
save_doc=open("chosun_snr_tokenized.txt", 'w')

for i in doc_ko:
    for j in kkma.nouns(i):
        save_doc.write(j+" ")
save_doc.close()
doc_ko.close()
