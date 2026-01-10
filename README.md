# nlohmann-json-deb

#EN

This project automates the packaging of the [nlohmann/json](https://github.com/nlohmann/json) C++ library into a Debian `.deb` package.

## Why?

- Enables easy installation on Ubuntu/Debian: `sudo dpkg -i libnlohmann-json-dev_3.11.3_amd64.deb`
- Follows Linux packaging standards
- Demonstrates DevOps skills: automation, reproducibility, packaging

## Requirements

- Ubuntu 22.04 (or WSL2)
- `git`, `dpkg-dev`

## How to build

```bash
chmod +x build.sh
./build.sh

#RU
# nlohmann/json .deb Packager

Этот проект автоматизирует упаковку библиотеки [nlohmann/json](https://github.com/nlohmann/json) на C++ в пакет Debian `.deb`.

## Зачем?

- Обеспечивает простую установку в Ubuntu/Debian: `sudo dpkg -i libnlohmann-json-dev_3.11.3_amd64.deb`
- Соответствует стандартам упаковки Linux
- Демонстрирует навыки DevOps: автоматизация, воспроизводимость, упаковка

## Требования

- Ubuntu 22.04 (или WSL2)
- `git`, `dpkg-dev`

## Как собрать

```bash
chmod +x build.sh
./build.sh
