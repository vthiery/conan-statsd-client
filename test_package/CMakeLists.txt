cmake_minimum_required(VERSION 3.2)

project(PackageTest CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_EXTENSIONS OFF)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(Threads)
add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS} ${CMAKE_THREAD_LIBS_INIT})