from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import FindPackageShare, LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    param_file = os.path.join(
        FindPackageShare('pointcloud_to_laserscan').find('pointcloud_to_laserscan_node'),
        'param',
        'pointcloud_to_laserscan_node.param.yaml'
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            name='scanner', default_value='scanner',
            description='Namespace for sample topics'
        ),
        Node(
            package='pointcloud_to_laserscan', executable='dummy_pointcloud_publisher',
            remappings=[('cloud', [LaunchConfiguration(variable_name='scanner'), '/cloud'])],
            parameters=[{'cloud_frame_id': 'cloud', 'cloud_extent': 2.0, 'cloud_size': 500}],
            name='cloud_publisher'
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', '1', 'map', 'cloud']
        ),
        Node(
            package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
            remappings=[
                ('~/input/pointcloud', [LaunchConfiguration('scanner'), '/cloud']),
                ('~/output/laserscan', [LaunchConfiguration('scanner'), '/scan']),
                ('~/output/pointcloud', [LaunchConfiguration('scanner'), '/cloud_out']),
                ('~/output/ray', [LaunchConfiguration('scanner'), '/ray']),
                ('~/output/stixel', [LaunchConfiguration('scanner'), '/stixel'])
            ],
            parameters=[param],
            name='pointcloud_to_laserscan'
        )
    ])
