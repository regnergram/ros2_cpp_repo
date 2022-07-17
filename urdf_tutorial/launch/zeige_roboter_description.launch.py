"""
Dieses Python Skript visualisiert die Roboterbeschreibung aus dem urdf-Ordner mit Rviz.
Siehe Quelle: https://docs.ros.org/en/foxy/Tutorials/Intermediate/URDF/Using-URDF-with-Robot-State-Publisher.html
WICHTIGES ZU DEN LAUNCH FILES:
- Launchfiles muessen immer die Endung launch.py haben, also z.B. dateiname.launch.py
- Der launch-Ordner mit den Launchfiles muss in CMakeLists.txt mit eingebunden werden ueber folgenden Befehl:

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

- Ausserdem muessen alle hier fuer den Start der Nodes benoetigten Packages in der package.xml Datei wie folgt 
  unter "<buildtool_depend>ament_cmake</buildtool_depend>" angegeben werden:

<depend>package_name1</depend>
<depend>package_name2</depend>

- Nach dem colcon build muss noch im Terminal gesourced werden mit:
. install/setup.bash
"""
import os                               # eine Library, um mit Dateipfaden in Python arbeiten zu koennen
from launch import LaunchDescription    # Um ROS2 eine Launch- bzw. Start-Anleitung mitgeben zu koennen
from launch_ros.actions import Node     # damit Nodes in die LaunchDescription eingebunden werden koennen

from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    """
    Diese Funktion muss immer so lauten, damit das Launchfile ausfuehrbar ist.

    """
    pkg_share = FindPackageShare(package='urdf_tutorial').find('urdf_tutorial')
    default_model_path = os.path.join(pkg_share, 'urdf/roboter_beschreibung_beginner.urdf')
    ## 
    # Der Launch eines Nodes benoetigt immer mindestens zwei Argumente:
    # - package: name des packages, in welchem sich der Node befindet
    # - executable: name des executable, welches in der Regel der Name des Knotens ist
    # Des weiteren gibt es noch optionale Argumente:
    # - name: vor allem dann relevant, wenn ein Node mehrmals gestartet werden soll
    # - output: TODO: Recherche, was das besonderes tut
    # - arguments: 
    # - parameters: Besitzt der aufzurufende Node ROS2-Parameter, so koennen sie 
    #               hier nach dem folgenden Schema initialisiert werden:
    #               [
    #                   {'parameter_name1': "string_value"},
    #                   {'parameter_name1': 12345},
    #                   {'parameter_name3': LaunchConfiguration('launch_argument')},
    #               ]
    # - condition: 
    ##
    robot_state_publisher_node = Node(
        package='robot_state_publisher',        
        executable='robot_state_publisher',
        name='robot_state_publisher',
        arguments=[default_model_path]
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        # output='screen',
        # arguments=['-d', LaunchConfiguration('rvizconfig')]
    )

    return LaunchDescription([
        # alle ROS2-Nodes, die durch dieses Launchfile gestartet werden sollen
        # sowie alle Launch-Arguments muessen hier aufgelistet werden.
        # Es wird hierbei die hier geschriebene Reihenfolge beachtet, daher sollten
        # launch-arguments immer oben stehen.
        # Kommas (,) nicht vergessen. ;)
        robot_state_publisher_node,
        rviz_node
    ])