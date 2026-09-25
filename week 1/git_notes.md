# Git 实操速查（week 1）

> 仓库：`https://github.com/TYT350/my_study.git`
> 流程：本地 init → 配置身份 → 写 .gitignore → commit → 绑定远程 → push

## 一、首次初始化（只做一次）

```bash
git init
git config --global user.name "TYT350"
git config --global user.email "tyt_0000@qq.com"
git remote add origin https://github.com/TYT350/my_study.git
git add .
git commit -m "初次提交"
git push -u origin master      # -u 绑定上游分支，仅首次需要
```

- `--global`：整台电脑生效；查看配置 `git config --global --list`
- `Reinitialized existing Git repository` 是正常提示，不是报错
- 远程地址写错可改：`git remote set-url origin 新地址`；查看：`git remote -v`

## 二、日常提交（以后反复用）

```bash
git add .
git commit -m "说明本次改动"
git push
```

- `add` → 进暂存区；`commit` → 存本地仓库快照；`push` → 才上传 GitHub
- **commit 只在本地，不会自动上传**

## 三、.gitignore（仓库根目录）

告诉 Git 哪些文件不追踪：

```gitignore
__pycache__/
*.pyc
.vscode/
*.pdf
*.zip
*.rar
```

- Windows 坑：资源管理器必须勾选【文件扩展名】，否则实际存成 `.gitignore.txt`，Git 不认
- **只对未追踪的文件生效**；已提交的文件需先移出追踪：

```bash
git rm --cached -r "week 2/__pycache__"
```

`--cached` 只删 Git 记录、不删本地文件；`-r` 递归文件夹；**路径带空格必须加双引号**。

## 四、踩坑记录

| 报错 | 原因 | 解决 |
|---|---|---|
| `src refspec main does not match any` | 本地分支是 `master`，却推 `main` | 推 `git push -u origin master` |
| `Recv failure: Connection was reset` | 国内访问 GitHub 不稳定 | 重试 / 手机热点 / ghproxy 镜像 |
| `pathspec 'week\' did not match any files` | 路径有空格没加引号 | `"week 2/__pycache__"` 加双引号 |
| 忽略规则不生效 | 文件名是 `.gitignore.txt` | 显示扩展名后重命名 |

## 五、四个区域

**工作区**（正在编辑的文件）→ `add` → **暂存区** → `commit` → **本地仓库**（`.git`）→ `push` → **远程仓库**（GitHub）
