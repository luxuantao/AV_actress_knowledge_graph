# AV_actress_knowledge_graph
> 这个项目中不含任何黄色内容！这个项目中不含任何黄色内容！这个项目中不含任何黄色内容！

出于对知识图谱（以及一点点对AV女优）的兴趣，也为了锻炼自己的“动手能力”，我构建了这个AV女优知识图谱，这个图谱很小，目前只包含几百个实体和单一的关系，不过后面会逐步扩充，并做一个系统出来。

现在仓库中已经包含了爬虫的代码和爬取到的数据，图数据库使用neo4j。

### 安装

 `pip install requests-html tqdm` 即可

### 数据导入neo4j

我使用的neo4j版本是neo4j-community-4.0.1

导入指令在data目录下的 `数据导入指令.txt` 中，按要求导入即可。（要注意的是导入时需要把 `actressinfo.csv` 和 `actressworks.csv` 放在neo4j的import目录下）

### 数据可视化

目前只是在neo4j中查看数据，不过等系统开发出来，就可以在系统上看了。

![](https://github.com/luxuantao/AV_actress_knowledge_graph/blob/master/img/neo4j.png)