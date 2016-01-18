# pyXcodeDocs

Using Python to Get Xcode Document download links and generate an Excel file
>使用 Python 获取 Xcode 文档的下载链接，聚合到一个 Excel 表格中

The Xcode document updates from Apple are always kind of huge. And the speed is always very low...That is such a sad story.
>渣果的 Xcode 文档更新总特别大。然后速度还很狗。。。太扯淡了。


Then I find out a way to download them with p2p softwares. We can find the link to the dmg files from [this link](https://developer.apple.com/library/downloads/docset-index.dvtdownloadableindex).
>然后我找到了个办法，用下载工具来下载。可以从[这个链接里面](https://developer.apple.com/library/downloads/docset-index.dvtdownloadableindex)找到 dmg 文件的链接。


After downloading the dmg files , we need to copy the components to the dir below:
>下载之后把内部的文件安装到如下目录即可：


```Bash
/Applications/Xcode.app/Contents/Developer/Documentation/DocSets
````

You can also use Dash.
>或者你用 Dash 来管理也可以了。


But there should always be something easier than opening the link in a browser and copying links one by one into a download tool.
>不过呢，浏览器中打开链接然后一个个复制多麻烦呢，理应更简单点。


So I just wrote a little Python script that gathers the links of Xcode Documents and puts all items into a single Excel file. You need to install pandas to run this script.
>所以我就写了一个 Python 脚本，收集链接中 Xcode 文档的下载链接，然后生成到一个 Excel 表格里面。你需要安装 Pandas 来运行这个脚本以实现生成 Excel 的功能。

```Bash
pip install pandas
```




It is really very very easy... I just wanna make a boring stuff easier.
>这个超级简单的。。。我就想省个时间，免得手动操作那么恶心了。