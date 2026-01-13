# CMakeLists.txt
cmake_minimum_required(VERSION 3.15)
project(json-test CXX)

# Подключаем зависимости от Conan (если используется)
if(EXISTS "${CMAKE_BINARY_DIR}/conan_deps.cmake")
    include(${CMAKE_BINARY_DIR}/conan_deps.cmake)
else()
    # Резервный вариант: ищем в системе (для .deb)
    find_path(NLOHMANN_JSON_INCLUDE_DIR nlohmann/json.hpp)
    if(NOT NLOHMANN_JSON_INCLUDE_DIR)
        message(FATAL_ERROR "nlohmann/json not found. Install .deb or use Conan.")
    endif()
    add_library(nlohmann_json INTERFACE)
    target_include_directories(nlohmann_json INTERFACE ${NLOHMANN_JSON_INCLUDE_DIR})
endif()

# Ваш исполняемый файл
add_executable(json-test main.cpp)  # ← замените на ваш исходник

# Линкуем библиотеку
target_link_libraries(json-test nlohmann_json)
