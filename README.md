## 12/28 Demo

# se_project

testtest

```sh
git branch <new function>
git checkout <new function>
# change something
git add .
git status # checkout what has been staged
git commit -m 'i change something'
git push -u origin <new function> # remember origin and <new funciton>
# 之後只要打git push 不用打上面一長串
# 在github上面就會出現 <new function> 這個分支
# 在github上面開啟新的pull request
# merge pull request以後...
git checkout main
git pull
# 一切都跟遠端同步了，可以重新開始以上步驟

git pull --rebase # 避免在合併時產生其他commit
```
