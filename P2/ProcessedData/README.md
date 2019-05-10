#Reading data
Data have been read from .txt files which were collected before
and gathered together as one long string.
<br>

#Processing data
For processing normalization and tokenizatio are needed and [hazm](http://www.sobhe.ir/hazm/) does it ver well by calling two functions:
normalize() and worde_tokenize()

##Here is what hazm does for us

> normalizer = Normalizer()<br>
> normalizer.normalize<br>
('اصلاح نويسه ها و استفاده از نیم‌فاصله پردازش را آسان مي كند')<br>
'اصلاح نویسه‌ها و استفاده از نیم‌فاصله پردازش را آسان می‌کند'

> word_tokenize<br>
('ولی برای پردازش، جدا بهتر نیست؟')<br>
['ولی', 'برای', 'پردازش', '،', 'جدا', 'بهتر', 'نیست', '؟']<br>

#Writing processed data
After processing,each data(pop and traditional) has been stored in .txt files base on its label.