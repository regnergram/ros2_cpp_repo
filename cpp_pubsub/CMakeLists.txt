cmake_minimum_required(VERSION 3.8)
project(cpp_pubsub)                     # Hier wird der Name des Packages definiert

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)           # diese Zeile muss manuell hinzugefuegt werden, damit gebuildet werden kann.
find_package(std_msgs REQUIRED)         # Beispiel einer Einbindung eines Packages, welches ROS2-Knoten benoetigt wird.

add_executable(talker src/talker.cpp)   # Hier werden die Executables, also die ausfuehrbaren ROS2-Knoten definiert. 
                                        # Links steht der frei waehlbare Name eines Executables, rechts die Datei, die 
                                        # bei Aufruf des Executables ausgefuehrt werden soll.

# JR: Folgende Zeilen wurden bei Erstellung des Packages mit der --node-name talker 
# Option mit hinzugefuegt. Sie sind aber unnoetig:
target_include_directories(talker PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_compile_features(talker PUBLIC c_std_99 cxx_std_17)  # Require C99 and C++17
# JR: Ende

# JR: Folgende Zeile wurde bei Erstellung des Packages mit den Optionen "--node-name talker --dependencies std_msgs" hinzugefuegt.
ament_target_dependencies(talker rclcpp std_msgs) # Hier werden die fuer das Executable benoetigten Packages
                                                  # eingebunden


install(TARGETS talker                  # Dieser Befehl ist essentiell, um die Executables finden zu koennen.
  DESTINATION lib/${PROJECT_NAME})      

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
