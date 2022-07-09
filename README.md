# ros2_cpp_repo

Wichtig: Wenn Packages benötigt werden, so müssen sie in *CMakeLists.txt* und in *package.xml* mit berücksichtigt werden. Folgende Codezeilen müssen also in den jeweiligen Dateien hinzugefügt werden:

In *CMakeLists.txt*:

```sh
find_package(package_name REQUIRED)                              # Package wird ueberhaupt mit eingebunden
ament_target_dependencies(executable_name rclcpp package_name)   # Package wird im Executable beruecksichtigt
```

In *package.xml*:

```xml
 <depend>package_name</depend>  <!--Einbindung des Packages 'package_name' -->
```