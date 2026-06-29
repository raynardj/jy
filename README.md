# BPE Tokenizers on classical romance master pieces
# 四大名著 + 金庸 定制BPE 词元 / 分词器

[![pages-build-deployment](https://github.com/raynardj/ciyuan/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/raynardj/ciyuan/actions/workflows/pages/pages-build-deployment)

We trainend tokenizers out of corpus of [four great classic romance](./four) and Jinyong [corpus](./corpus) with [notebook here](./notebooks). This is an exercise toward understanding of BPE tokenizer, a popular tokenizer for many of the large language model. Thanks great deals to [this Andrej Karpathy video: Let's build a GPT tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE), I have more intuitive sense about it now.

Many of the visualization aimed to have more intuitive 1 glance grasp of the idea. 
<table>
  <tr>
    <td><img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/d1eca549-ccf3-48ae-8594-c485894dfcdb" /></td>
    <td><img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/c240a898-ced8-4b42-8b7c-494ef913079b" /></td>
    <td><img width="400" height="280" alt="image" src="https://github.com/user-attachments/assets/f3f3f231-08d4-4767-8ca0-77975d9a896b" /></td>
  </tr>
</table>

用这里的[笔记](./notebooks)训练了几个分词器, 分别根据[四大名著](./four)+[金庸](./corpus)全文.

## 分词器 / Tokenizer
I implemented the very basic version of `Bytes Pair Encoding`, the original corpus was turned into bytes encoded utf8, all tokens' ancestry can be traced up to pairs of bytes.

采用了比较基础款的Bytes Pair Encoding, 原文按utf8转成bytes, 所有词元上游都可以追溯到一对基础bytes 单元的组合.

For the entire try, the combination is to combine `pairs` of tokens into new tokens.

整个树的组合方式是每一层能用2个词元(Pair)组合出一个新词元.

You can try this [tokenizing tree interface](https://raynardj.github.io/ciyuan/), it will display its ancestry and for each token, their possible descendants.

可以试玩这个[词元树的界面](https://raynardj.github.io/ciyuan/), 会显示上下游的词元.

可以选择分词器的语料典籍来源, 输入一句话(最好是文章里的原话) 
<img width="773" height="75" alt="image" src="https://github.com/user-attachments/assets/d4218a97-8b54-4af4-91ef-0c765d4c6c42" />

我们可以看见中间有具体的token分词效果, 以及上游(上方)和下游(下方)的词元
<img width="1502" height="839" alt="image" src="https://github.com/user-attachments/assets/c240a898-ced8-4b42-8b7c-494ef913079b" />

每个词元节点的卡片里, 左下角的数字是token id, 右下角是出现频次:
<img width="1595" height="588" alt="image" src="https://github.com/user-attachments/assets/5d402da3-2ce0-410d-912e-4a25bf5523a7" />

不同的分词器, 上下游的树图的当量是不一样的, 比如同样`刀`这个字分别在水浒 红楼 三国中的关系树:
<img width="1301" height="986" alt="image" src="https://github.com/user-attachments/assets/280d06b9-825a-45c7-a1b8-aebd189b2bdc" />
<table>
  <tr>
    <td>
      <img width="204" height="502" alt="image" src="https://github.com/user-attachments/assets/53974fd9-4836-4d1c-9105-58fd3a8c9d4b" />
    </td>
    <td>
        <img width="1295" height="737" alt="image" src="https://github.com/user-attachments/assets/6ff6ac01-a82a-4156-82ec-717a2788035d" />
    </td>
  </tr>
</table>

## 分词原文 / Tokenizing Corpus

我们可以观察在完整的著作中, 词元是以什么粒度存在的:

[四大名著](https://raynardj.github.io/ciyuan/four.html), [金庸](https://raynardj.github.io/ciyuan/four.html)可以典籍右上角齿轮选择著作和章节
<img width="1626" height="962" alt="image" src="https://github.com/user-attachments/assets/f3f3f231-08d4-4767-8ca0-77975d9a896b" />
<img width="852" height="615" alt="image" src="https://github.com/user-attachments/assets/65360e17-5673-40fc-84c9-0b3a91d5030e" />

## 统计分析 / Stats & Dashboard
[分词器统计页面](https://raynardj.github.io/ciyuan/stats.html)
<img width="1091" height="784" alt="image" src="https://github.com/user-attachments/assets/2fe2dec1-77e6-42ff-a25a-859e4531e42a" />






