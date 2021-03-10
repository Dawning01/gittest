git 的测试
git 远程
cd .ssh
ls
cat id_rsa.pub
git remote add origin git@github.com: XXXX

查看连接名称
git remote
断开
git remote rm [origin]
将本地分之推送
git push -u -origin master
git push origin [:branch] 删除向远程仓库推送的分支
git push origin [tag]推送一个本地标签到远程

git push origin [tags] 推送所有本地所有标签到远程
git push origin --delete tag [tagname]删除向远程仓库推送的标签
# 用于本地版本比远程版本旧时强行推送本地版本
git push --force origin
#从远程获取代码
git pull



