# 本地支付长链生成器

一个纯本地运行的小工具：粘贴 ChatGPT `accessToken` 后，在本机创建 hosted checkout 支付会话，并返回支付链接。

## 隐私说明

- 服务端代码不会保存 token、代理、优惠码或生成结果。
- 代理地址只保存在用户自己浏览器的 `localStorage`。
- 服务端请求日志已关闭。
- 发布包不包含任何个人 token、代理、服务器 IP、域名或本机路径。

## Windows 启动

1. 安装 Python 3。
2. 解压本目录。
3. 双击 `run.bat`。
4. 浏览器会自动打开：

```text
http://127.0.0.1:7790/
```

首次启动会自动创建 `.venv` 并安装依赖。

## 手动启动

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe server.py
```

## Docker 部署

### Docker Compose

```bash
docker compose up -d --build
```

启动后访问：

```text
http://服务器IP:7790/
```

停止服务：

```bash
docker compose down
```

### Docker 命令

```bash
docker build -t local-payurl-forum .
docker run -d --name local-payurl-forum --restart unless-stopped -p 7790:7790 local-payurl-forum
```

如需修改宿主机端口，例如改为 `9000`：

```bash
docker run -d --name local-payurl-forum --restart unless-stopped -p 9000:7790 local-payurl-forum
```

容器内通过 `docker_server.py` 监听 `0.0.0.0:7790`，原来的 `server.py` 仍保持 Windows 本地启动方式。

## 发布 GitHub 镜像

项目已内置 GitHub Actions 工作流：

```text
.github/workflows/publish-docker-image.yml
```

发布到 GitHub Container Registry：

```text
ghcr.io/你的GitHub用户名或组织名/仓库名
```

触发方式：

- 在 GitHub 仓库的 `Actions` 页面手动运行 `Publish Docker Image`。
- 只发布 `latest` 标签。
- 镜像支持 `linux/amd64` 和 `linux/arm64`。

拉取示例：

```bash
docker pull ghcr.io/你的GitHub用户名或组织名/仓库名:latest
docker run -d --name local-payurl-forum --restart unless-stopped -p 7790:7790 ghcr.io/你的GitHub用户名或组织名/仓库名:latest
```

如果镜像是私有的，需要先登录：

```bash
docker login ghcr.io
```

## 使用

1. 点击页面中的“复制 Session 地址”。
2. 在已登录 ChatGPT 的浏览器中打开该地址。
3. 复制返回 JSON 里的 `accessToken`，或复制整段 JSON。
4. 粘贴到本工具。
5. 根据需要选择 Plus / Team、地区、代理和优惠码。
6. 点击“生成支付长链”。

## 代理

支持：

```text
http://127.0.0.1:7890
socks5h://user:pass@host:port
socks5://user:pass@host:port
```

检测代理时会优先使用 `http://iprust.io/ip.json`，并自动尝试常见代理协议。
