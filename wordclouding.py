from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# Read the whole text.
text = open('chosun_minju_tokenized.txt', 'r', encoding='utf8')

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = np.array(Image.open(path.join(d, "moon1.png")))

wc = WordCloud(background_color="white", mask=alice_mask, font_path="NGULIM.TTF")
# generate word cloud


wc.generate(text.readline())

# store to file
wc.to_file(path.join(d, "chosun_minju.png"))

# show
plt.imshow(wc)
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray)
plt.axis("off")
plt.show()