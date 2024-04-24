# ChaosRegion_CHS

这是[Skyfish](http://www.sky-fish.jp/html/sf-main.html)社[ 鋼炎のソレイユ－ChaosRegion-]() 的ai翻译补丁，使用[Sakura](https://github.com/SakuraLLM/Sakura-13B-Galgame) v0.10进行翻译。

此补丁未经过校对，之后也不打算再进行人工对文本进行修改，错译较多。（但基本上能看懂大意）

卡牌系统、卡牌游戏说明等也未进行汉化。（打牌能跳过）

解、封包的代码都是本人手搓的，本人编程、逆向水平有限，目前存在一些bug，可能会影响游戏体验：

* 人名框显示东西时会闪退，所以把人名挪到了文本框中。
* 选项出现乱码。

T. S. WORKS汉化组已在2021年开坑本作的汉化，此补丁只是本人等不及想玩所以制作的，如果期待更佳的体验可以期待大佬的人工汉化：

[【图片】【T.S.WORKS】汉化目标公示&amp;招人一起做汉化【galgame吧】_百度贴吧 (baidu.com)](https://tieba.baidu.com/p/7338266179)

本项目以交流AI翻译为目的，仅供交流学习。请在购买了[游戏本体](https://www.getchu.com/soft.phtml?id=488385)的基础上使用。


本补丁发布于[https://github.com/jyxjyx1234/ChaosRegion_CHS](https://github.com/jyxjyx1234/ChaosRegion_CHS)。

### 游戏信息

摘自Getchu

|     ブランド： | [SkyFish](http://www.sky-fish.jp/ "このブランドの公式サイトを開く")[（このブランドの作品一覧）](https://www.getchu.com/php/search.phtml?search_brand_id=25375)                                                                                                              |
| -------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|         定価： | ￥8,800 (税込￥9,680)                                                                                                                                                                                                                                              |
|       発売日： | [2008/04/25](https://www.getchu.com/php/search.phtml?start_date=2008/04/25&end_date=2008/04/25&genre=pc_soft "同じ発売日の同ジャンル商品を開く")                                                                                                                         |
|     メディア： | DVD-ROM                                                                                                                                                                                                                                                            |
|     ジャンル： | ヴァルキリー・サーガ・ADV with Card Battle                                                                                                                                                                                                                         |
|    JANコード： | 4520424250035                                                                                                                                                                                                                                                      |
|         原画： | [蔓木鋼音](https://www.getchu.com/php/search.phtml?person=%CC%A2%CC%DA%B9%DD%B2%BB)、[さえき北都](https://www.getchu.com/php/search.phtml?person=%A4%B5%A4%A8%A4%AD%CB%CC%C5%D4)                                                                                         |
|     シナリオ： | [素浪人](https://www.getchu.com/php/search.phtml?person=%C1%C7%CF%B2%BF%CD)、他                                                                                                                                                                                       |
|         音楽： | LittleWing、まにょっ                                                                                                                                                                                                                                               |
| アーティスト： | Rita                                                                                                                                                                                                                                                               |
|         監督： | ひろもりさかな                                                                                                                                                                                                                                                     |
| 商品同梱特典： | 初回特典：オリジナルサウンドトラック                                                                                                                                                                                                                               |
| サブジャンル： | [麻雀・テーブルゲーム](https://www.getchu.com/all/genre.html?sub_genre_id=313)、[アドベンチャー](https://www.getchu.com/all/genre.html?sub_genre_id=308) [[一覧]](https://www.getchu.com/php/sub_genre.phtml)                                                               |
|     カテゴリ： | 異世界、[戦うヒロイン](https://www.getchu.com/php/search.phtml?category[0]=C3_B046)、[伝奇](https://www.getchu.com/php/search.phtml?category[0]=C3_F008)、[バトル](https://www.getchu.com/php/search.phtml?category[0]=C3_F026) [[一覧]](https://www.getchu.com/pc/genre.html) |

简介\购买正版：[https://www.getchu.com/soft.phtml?id=488385](https://www.getchu.com/soft.phtml?id=488385)

### 使用说明

从release中下载ChaosRegion_CHS.rar，将其中的内容放到游戏安装目录中，替换rld文件夹中的文件。

### 重新封包

汉化文本在译文文件夹中，可自行修改。运行 ` 封包\封包.py`进行封包，即可更新ChaosRegion_CHS中的文件。将ChaosRegion_CHS中的文件复制到安装目录中即可。

### 致谢

本补丁使用了以下开源项目：

* [Sakura-13B-Galgame](https://github.com/SakuraLLM/Sakura-13B-Galgame) : 适配轻小说/Galgame的日中翻译大模型
* [UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework)：对汉化后的文本进行修正以正常显示
* [GalTransl](https://github.com/xd2333/GalTransl) ：自动化翻译工具
