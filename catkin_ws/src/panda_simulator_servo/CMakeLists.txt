cmake_minimum_required(VERSION 3.0.2)
project(panda_simulator_servo)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY launch config script
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
