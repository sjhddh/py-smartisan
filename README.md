# 啪锤库 (py-smartisan)

##### *A kindergarten-level python implementation of b\*s functions in smartisan TNT*

###### *转载本代码库内任何内容，请注明出处*

###### *对这个项目表达喜欢或者姿词，请点击右上角的小星星*

###### *Please Star this project if you like it*

这是一个使用幼儿园级别python语言实现某锤科技在[2018年发布会](https://www.bilibili.com/video/av23492564/)上吹\*的各种语音识别交互office功能的项目。

我们欢迎全球各地的锤黑、锤粉、路人等等加入到这个项目的共享开发中来。

项目没有错，代码共享本身是无辜的，请各路立场的开发者Keep Real的同时，也要尊重世界和平，PEACE～

### Development Spec：

#### Development Language

这是一个python3项目。拘泥于python2的朋友们，可以考虑一下走进新时代了。

#### File Structure

```
|--
  |-- Model: 存放所有的office套件功能模型
  |-- Interface: 存放所有人机交互模型，比如语音交互等等
  |-- Controller: 模型控制器，保证与控制interface和model之间的交流
  |-- Examples: 前期准备的一些for fun的小案例
```

#### Specification

##### Interface

这部分非常直观，

第一步，Receiver: 我们就使用谷歌语音识别或者科大讯飞的类似产品，把人类语音转化为文字

第二步，Parser: 把用户的问话转化为行动处理的意图，并分发给相应的`model`们

第三步，Responser: 我们需要对话库来回复人类用户的request。初期，我们可以直接手写在代码中。如果量大，我建议使用[DialogFlow](https://dialogflow.com/)。其实包括Parser的部分，也是可以借用DialogFlow的功能来解决多种样态文本的意图统一问题。

##### Model

按照MSOffice的各个套件逐步展开：

* 文档编辑 Docx：
我们使用[python-docx](https://python-docx.readthedocs.io/en/latest/)进行调用和修改，
实现功能：创建文档，修改字体，修改字体大小，全选，等等。
全程很貌似李开复博士在1992年展示的[casper](https://www.youtube.com/watch?v=8De_KxYt1pQ)。Salute！

* 幻灯片 PPTx：
哈哈，我最爱这部分了，依旧调用库[python-pptx](https://python-pptx.readthedocs.io/en/latest/)对文件进行修改。
怎么修改？
那当然是得用到`闪念胶囊`了！我们让用户提供一串关键词（类似于用户的闪念们），然后我们根据关键词（可能需要中文分词一下），构建一份儿PPT，default的设计就是老罗酷爱的渐变黑底+白色粗体关键词居中。接下来，我们调用谷歌的[Custom Search API](https://developers.google.com/custom-search/json-api/v1/overview)把所有的关键词都搜索一遍，并把图片罗列在侧边栏（或某个更酷的展示区）。至此，按照老罗所说，我们就已经提升了1400%的工作效率了（喵呜）。

* 表格文件 xlsx:
没救，这功能我觉得想法已经够屎了。当今世界，python和excel的交集圈充满了各个公司的data analysts，也是拥有最多[python第三方库](http://www.python-excel.org/)的一个软件了。链接中提供的都很不错。欢迎大家开脑洞各种适合于此的功能设计。

* 等等等等

### 以上

如有问题，欢迎Github站内/邮件联系，或者联系我微博：[@翻滚吧_加号](https://www.weibo.com/4u2go)
