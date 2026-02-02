# git 的介绍
git是什么？
git是一个版本分布式管理系统
# git的使用
## git的仓库创建

    git init
    
## git的分支管理
    *最NB的技能*


### 创建分支
* 创建新分支并切换到该分支：
    git checkout -b <branchname>#这是一种老式的创建分支的方法
例如：

    git checkout -b feature-xyz

* 切换分支命令:

    git checkout (branchname)

例如：

    git checkout main

当你切换分支的时候，Git 会用该分支的最后提交的快照替换你的工作目录的内容， 所以多个分支不需要多个目录。#什么意思，我没看懂

如果我们要手动创建一个分支。执行 git branch (branchname) 即可。

    $ git branch testing
    $ git branch
    * master

### 查看分支
查看所有分支：

    git branch

查看远程分支：

    git branch -r

查看所有本地和远程分支：

    git branch -a

### 合并分支

将其他分支合并到当前分支：

    git merge <branchname>
例如，切换到 main 分支并合并 feature-xyz 分支：

    git checkout main
    git merge feature-xyz

### 解决合并冲突
当合并过程中出现冲突时，Git 会标记冲突文件，你需要手动解决冲突。解决合并冲突没有想象的那么简单
打开冲突文件，按照标记解决冲突。
标记冲突解决完成：

    git add <conflict-file>
提交合并结果：

    git commit

### 删除分支
删除本地分支：

    git branch -d <branchname>
强制删除未合并的分支：

    git branch -D <branchname>
删除远程分支：

    git push origin --delete <branchname>
### 远程仓库

1. git remote 命令
    git remote 列出当前仓库中配置的远程仓库
    git remote -v 查看所有绑定的远程仓库，并显示它们的url
    git remote add <remote_name> <remote_url>绑定一个远程仓库
    git remote rename <old_name> <new_name> 重命名远程仓库
    git remote remove <remote_name>
    git remote set-url <remote_name> <new_url> 修改
    git remote show <remote_name> 展示远程仓库信息，含有url和跟踪分支

2. git push 命令
git push 用于将本地的提交（commits）推送到远程仓库。它会将本地分支的更新同步到远程分支。

常用语法：

    git push <远程仓库名> <分支名>
示例：

    git push origin main
将本地的 main 分支推送到远程仓库 origin。

注意：
如果远程分支不存在，可能需要加上 -u 参数来设置跟踪关系：

    git push -u origin main
3. git pull 命令
git pull 用于从远程仓库拉取最新的更改并合并到当前分支。它实际上是 git fetch 和 git merge 的组合。

常用语法：
    git pull <远程仓库名> <分支名>
示例：
    git pull origin main
从远程仓库 origin 的 main 分支拉取最新的更改并合并到当前分支。
注意：
如果远程分支有更新，而本地分支有冲突，可能需要手动解决冲突。
如果只想拉取更改而不合并，可以使用 git fetch。

## 分支工作流

Git Flow 是一种常用的分支工作流，分为以下几种分支类型：
1. 开发软件工作流
主分支（main/master）：存储生产代码。
开发分支（develop）：存储即将发布的代码。
功能分支（feature）：从 develop 分支创建，用于开发新功能。
发布分支（release）：从 develop 分支创建，用于准备发布。
热修复分支（hotfix）：从 main 分支创建，用于紧急修复生产问题。
    1. 创建功能分支：

        git checkout develop
        git checkout -b feature/xyz
    2. 完成功能开发并合并：

        git checkout develop
        git merge feature/xyz
        git branch -d feature/xyz
    3. 创建发布分支：

        git checkout develop
        git checkout -b release/1.0.0
    4.  发布并合并到主分支和开发分支：

        git checkout main
        git merge release/1.0.0
        git tag -a 1.0.0 -m "Release 1.0.0"
        git checkout develop
        git merge release/1.0.0
        git branch -d release/1.0.0
    5. 创建热修复分支：

        git checkout main
        git checkout -b hotfix/1.0.1
    6.  完成修复并合并：

        git checkout main
        git merge hotfix/1.0.1
        git tag -a 1.0.1 -m "Hotfix 1.0.1"
        git checkout develop
        git merge hotfix/1.0.1
        git branch -d hotfix/1.0.1
    7.  实例
    以下是一个综合示例，演示分支创建、切换、合并和删除。

    创建和切换分支：

        git checkout -b feature-abc
        
    开发并提交更改：

    编辑文件并提交
        git add .
        git commit -m "Develop feature ABC"

    合并到主分支：

        git checkout main
        git merge feature-abc
    删除本地分支：

        git branch -d feature-abc

2. 个人学习git流
main 主分支

    2.1 学习记录保存
        git add '学习内容的文件名'
        git commit -m '写好备注，比如这次保存的主要内容主题是什么'
        git push "远程分支名"
    2.2 为修改知识框架

    
## 关于git使用，我所遇到过的问题和心得记录
* 将文件推送到github失败
Q1：网络问题：GitHub不支持国内网络访问 A:1、要想推送成功，要么挂梯子，要么挂加速器
Q2:github推送设置问题：GitHub关于推送文件有相关设置。A:将报错发给ai，根据ai给的步骤走。
* 慎用#号分段，否则你会得到依托答辩