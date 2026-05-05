import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # YAML dosyasının yolunu bul
    config_file = os.path.join(
        get_package_share_directory('autonomous_driving_pkg'),
        'config',
        'vehicle_params.yaml'
    )

    return LaunchDescription([
        Node(
            package='autonomous_driving_pkg',
            executable='sensor_publisher',
            name='front_lidar_sensor',
            output='screen'
        ),
        Node(
            package='autonomous_driving_pkg',
            executable='actuator_controller',
            name='brake_and_throttle_actuator',
            output='screen'
        ),
        Node(
            package='autonomous_driving_pkg',
            executable='vehicle_brain',
            name='central_processing_unit',
            output='screen',
            parameters=[config_file]  # <--- YENİ EKLENEN SATIR
        )
    ])
