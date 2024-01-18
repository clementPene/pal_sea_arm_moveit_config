cmake_minimum_required(VERSION 3.8)
project(pal_sea_arm_moveit_config)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

ament_auto_package(INSTALL_TO_SHARE launch config)