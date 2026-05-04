import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1. Sensör Düğümü: Çevreyi taramaya başlar
        Node(
            package='autonomous_driving_pkg',
            executable='sensor_publisher',
            name='front_lidar_sensor',
            output='screen'
        ),
        
        # 2. Aktüatör Düğümü: Fren ve motor sistemleri hazır bekler
        Node(
            package='autonomous_driving_pkg',
            executable='actuator_controller',
            name='brake_and_throttle_actuator',
            output='screen'
        ),
        
        # 3. Araç Beyni: Tüm sistemleri dinler ve kararları verir
        Node(
            package='autonomous_driving_pkg',
            executable='vehicle_brain',
            name='central_processing_unit',
            output='screen'
        )
    ])
