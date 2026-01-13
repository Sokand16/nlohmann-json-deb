# conanfile.py
from conan import ConanFile
from conan.tools.files import copy, get
import os

class NlohmannJsonConan(ConanFile):
    name = "nlohmann_json"
    version = "3.11.3"
    license = "MIT"
    url = "https://github.com/nlohmann/json"
    description = "JSON for Modern C++"
    topics = ("json", "header-only", "c++11")
    settings = "os", "compiler", "build_type", "arch"
    no_copy_source = True  # не копировать исходники при установке

    def source(self):
        # Скачиваем архив с GitHub (не через git — Conan-совместимо)
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def package(self):
        # Копируем LICENSE и json.hpp в нужные папки
        copy(self, "LICENSE.MIT", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))
        copy(self, "json.hpp", 
             src=os.path.join(self.source_folder, "single_include", "nlohmann"),
             dst=os.path.join(self.package_folder, "include", "nlohmann"))

    def package_info(self):
        # Header-only: нет библиотек для линковки
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
        self.cpp_info.set_property("cmake_file_name", "nlohmann_json")
        self.cpp_info.set_property("cmake_target_name", "nlohmann_json::nlohmann_json")
