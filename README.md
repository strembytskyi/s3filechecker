# 📦 s3filechecker — S3 File Checker CLI

A simple CLI tool to find the **latest file** (by modification date) in an **S3-compatible bucket**, such as Yandex.Cloud, SberCloud, MinIO, etc.

Supports **custom endpoints** and **access credentials**.

---

## ✨ Features

- ✅ Works with any S3-compatible storage (AWS, Yandex.Cloud, SberCloud, MinIO, etc.)
- 🔐 Credentials via CLI flags or environment variables
- 🔍 Search with or without prefix (i.e., whole bucket)
- 🧩 Easy to install and run locally

---

## 🛠 Installation

### Requirements

- Python ≥ 3.8
- `pip` (Python package manager)

### macOS / Linux

```bash
git clone https://your.git.repo/s3filechecker.git
cd s3filechecker

python3 -m venv venv
source venv/bin/activate
pip install .
```

You can now use `s3filechecker` as a global command:

```bash
s3filechecker --help
```

> 💡 To install system-wide (not recommended), use `sudo pip install .`

---

## 🚀 Usage

### Basic example

```bash
s3filechecker   --bucket my-bucket   --endpoint https://storage.yandexcloud.net   --access-key AKIA...   --secret-key secret123
```

### Search with prefix

```bash
s3filechecker   --bucket my-bucket   --prefix logs/2024/   --endpoint https://storage.example.com   --access-key AKIA...   --secret-key secret123
```

### Search entire bucket

Leave `--prefix` empty or omit it entirely:

```bash
s3filechecker   --bucket my-bucket   --endpoint https://storage.example.com   --access-key AKIA...   --secret-key secret123
```

---

## 🔐 Using environment variables (recommended)

```bash
export AWS_ACCESS_KEY_ID=AKIA...
export AWS_SECRET_ACCESS_KEY=secret123

s3filechecker   --bucket my-bucket   --endpoint https://storage.example.com
```

---

## 📋 Example output

```
Latest file: logs/2024/backup-17.tar.gz
Last modified: 2024-04-15 18:22:09 UTC
```

---

## 🧼 Uninstall

```bash
pip uninstall s3filechecker
```

---

## 📄 License

MIT License
