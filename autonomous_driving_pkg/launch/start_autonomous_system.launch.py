from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='autonomous_driving_pkg',
            executable='vehicle_brain',
            name='brain_center'
        ),
        Node(
            package='autonomous_driving_pkg',
            executable='sensor_publisher',
            name='front_lidar'
        ),
    ])
