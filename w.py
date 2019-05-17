"""
 Hello 

"""
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

backgroud_Image = plt.imread('timg.jpg')
wc = WordCloud(background_color='white',  # 设置背景颜色
               scale=32,  # 该值越大,生成的图片越清楚
               margin=1,  # 词间间距
               mask=backgroud_Image,  # 设置背景图片
               font_path='STZHONGS.TTF',  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
               max_font_size=150,  # 设置字体最大值
               random_state=30  # 设置有多少种随机生成状态，即有多少种配色方案
               )
text = open(r'111.txt', encoding='utf-8').read()
wc.generate(text)
# 改变字体颜色
img_colors = ImageColorGenerator(backgroud_Image)
# 字体颜色为背景图片的颜色
wc.recolor(color_func=img_colors)
wc.to_file('wc.png')
