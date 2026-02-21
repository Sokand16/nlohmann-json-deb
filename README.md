# Упаковка nlohmann/json в .deb-пакет

Проект автоматизирует создание **стандартного `.deb`-пакета** для C++-библиотеки [nlohmann/json](https://github.com/nlohmann/json)

## Состав

- Создаёт корректный `.deb`-пакет (`libnlohmann-json-dev`)  
- Включает рецепт Conan для управления зависимостями  
- Содержит тестовое приложение для проверки работы библиотеки  
- Автоматизирован через скрипт `build.sh`    

## Требования

- Ubuntu 22.04 (или WSL2)
- Пакеты: `git`, `dpkg-dev`, `build-essential`
- Опционально: `conan` (устанавливается через `pip`)

Установка зависимостей:
```bash
sudo apt update && sudo apt install -y git dpkg-dev build-essential
pip3 install conan  # опционально
```

## Сборка .deb-пакет
```bash
chmod +x build.sh
./build.sh
```

Результат:
Файл nlohmann-json-3.11.3.deb — установка через sudo dpkg -i.

## Поддержка Conan (опционально)
В проекте есть рецепт Conan для nlohmann_json/3.11.3.

Чтобы собрать и проверить:
```bash
conan create . --build=missing
conan list "nlohmann_json/*"
```

## Проверка установки
В папке test-project/ лежит простое C++-приложение, которое проверяет, что библиотека действительно работает после установки.

## Вариант 1: проверка через .deb
### 1.Установка пакета:
```bash
sudo dpkg -i nlohmann-json-3.11.3.deb
```

### 2.Соберка и запуск теста:
```bash
cd test-project
mkdir build && cd build
cmake ..
сmake --build .
./json-test
```

## Вариант 2: проверка через Conan
### 1.Перейдите в папку тестового проекта:
```bash
cd test-project
```

### 2.Установите зависимости и сгенерируйте toolchain:
```bash
conan install . --output-folder=build --build=missing
```

### 3.Соберка проекта:
```bash
cd build
cmake .. -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake
cmake --build .
./json-test
```

Вывод:
```bash
{
  "message": "Hello from DevOps!",
  "project": "nlohmann-json-deb"
}
```

## Структура проекта
```
.
├── build.sh                # Основной скрипт автоматизации
├── conanfile.py            # Рецепт Conan для nlohmann/json
├── conandata.yml           # Ссылка на исходники и контрольная сумма
├── README.md
├── .gitignore
└── test-project/           # Тестовое C++-приложение
    ├── main.cpp
    ├── CMakeLists.txt
    └── conanfile.txt
```

## Лицензия
Этот проект: MIT
nlohmann/json: MIT License  
Библиотека разрабатывается и поддерживается в Европе.
