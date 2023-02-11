from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    li4_node = Node(
        package='village_li',
        executable='li4_service',
        parameters=[{'writer_timer_period': 2}]
    )
    wang2_node = Node(
        package='village_li',
        executable='wang2_sub'
    )

    launch_d = LaunchDescription([li4_node,wang2_node])
    return launch_d