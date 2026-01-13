// main.cpp
#include <iostream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

int main() {
    json j;
    j["message"] = "Hello from DevOps!";
    j["project"] = "nlohmann-json-deb";
    
    std::cout << j.dump(2) << std::endl;
    return 0;
}
