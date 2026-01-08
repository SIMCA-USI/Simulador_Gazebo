# Simulador Gazebo - Workspace ROS2 `ws_mutt`
## Configuración inicial

1. Clonar el repositorio:


git clone https://github.com/SIMCA-USI/Simulador_Gazebo.git
cd Simulador_Gazebo


2. Construir el workspace

colcon build
source install/setup.bash

3. Ejecutar simulaciones:
Lanzar el mundo y el robot en Gazebo

ros2 launch mutt_robot gps_waypoint_follower.launch.py use_rviz:=True

Seguir un punto pulsado en mapviz

ros2 run mutt_robot interactive_waypoint_follower

