---
title: "Git configure password in linux"
date: 2024-06-05T12:24:01+05:30
draft: false

---
# clone the desired repo
(git clone repourl)
```
git clone https://github.com/yashbhangale/geeksdirhugo.git
```
# assign access token (password) to the remote repo 
```
sudo git remote set-url origin https://Accesstokenpastehere@github.com/yashbhangale/geeksdirhugo.git
```
then cd into repo 
# assign username and user email 
```
sudo git config --global user.email "yashbhangale9@gmail.com"
```
```
sudo git config --global user.name "yashbhangale"
```
