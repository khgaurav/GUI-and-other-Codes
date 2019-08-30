cmake_minimum_required(VERSION 3.0.0)
project(hello_rs VERSION 0.1.0)

include(CTest)
enable_testing()


add_executable(hello_rs src/main.cpp)

find_package(PCL 1.6 REQUIRED)
find_package(OpenCV REQUIRED COMPONENTS core imgproc highgui)

include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})
target_link_libraries(hello_rs ${PCL_LIBRARIES})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
find_package(realsense2 REQUIRED)
target_link_libraries(hello_rs ${realsense2_LIBRARY})

