#!/bin/bash
# Автоматическая сборка .deb-пакета для nlohmann/json

set -e  # Прервать скрипт при любой ошибке

VERSION="3.11.3"
PKG_NAME="nlohmann-json-$VERSION"

echo "Скачиваем nlohmann/json v3.11.3.."
git clone --branch v$VERSION --depth 1 https://github.com/nlohmann/json.git

echo "Создаём структуру .deb..."
mkdir -p $PKG_NAME/{DEBIAN,usr/include/nlohmann}
cp json/single_include/nlohmann/json.hpp $PKG_NAME/usr/include/nlohmann/

echo "Создаём DEBIAN/control..."
cat > $PKG_NAME/DEBIAN/control <<EOF
Package: libnlohmann-json-dev
Version: $VERSION
Section: libdevel
Priority: optional
Architecture: amd64
Maintainer: DevOps Trainee <trainee@example.com>
Description: JSON for Modern C++
 A C++11 library for parsing and generating JSON.
Homepage: https://github.com/nlohmann/json
EOF

echo "Собираем .deb-пакет..."
dpkg-deb --build $PKG_NAME

echo "Готово! Пакет: $PKG_NAME.deb"
