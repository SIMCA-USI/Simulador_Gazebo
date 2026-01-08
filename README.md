# Simulador Gazebo - Workspace ROS2 `ws_mutt`
## Configuración inicial

1. Clonar el repositorio:

```bash
git clone https://github.com/SIMCA-USI/Simulador_Gazebo.git
cd Simulador_Gazebo


2. Construir el workspace
```bash
colcon build
source install/setup.bash

3. Ejecutar simulaciones:
Lanzar el mundo y el robot en Gazebo
```bash
ros2 launch mutt_robot gps_waypoint_follower.launch.py use_rviz:=True

```markdown
Seguir un punto pulsado en mapviz
```bash
ros2 run mutt_robot interactive_waypoint_follower

