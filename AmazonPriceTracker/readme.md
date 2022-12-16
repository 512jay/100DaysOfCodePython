The product.

Well lets track a [rasbery pi](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TD42S27/?_encoding=UTF8&pd_rd_w=RKzk5&content-id=amzn1.sym.a5eaa569-8a45-4530-84d2-2dcf8023272a&pf_rd_p=a5eaa569-8a45-4530-84d2-2dcf8023272a&pf_rd_r=C45FNT3RWW3P8XDF7ZRT&pd_rd_wg=nsOlL&pd_rd_r=204c1e86-019b-45c3-996c-384051fb1518&ref_=pd_gw_ci_mcx_mi&th=1).

browser headers.
[get headers](http://myhttpheader.com/)

https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TD42S27/?
_encoding=UTF8
&pd_rd_w=RKzk5&content-id=amzn1.sym.a5eaa569-8a45-4530-84d2-2dcf8023272a
&pf_rd_p=a5eaa569-8a45-4530-84d2-2dcf8023272a
&pf_rd_r=C45FNT3RWW3P8XDF7ZRT
&pd_rd_wg=nsOlL&pd_rd_r=204c1e86-019b-45c3-996c-384051fb1518
&ref_=pd_gw_ci_mcx_mi&th=1

[Beautiful Soup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Realized that a lot of the link info after the '?' was not needed. New link:
https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X/
Oh, you caught that I changed the product, yeah I did that.

Apparently lxml just needs to be installed in the environment for BeautifulSoup
to be able to use it. I removed the import after PyCharm complained about it
not being used and the parser still works.

While working on this project I had to brush up on [environmental variables](https://www.geeksforgeeks.org/python-os-environ-object/) again.
