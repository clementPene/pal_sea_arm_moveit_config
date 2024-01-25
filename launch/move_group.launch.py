# Copyright (c) 2023 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Dict
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():

    # Create the launch description and populate
    ld = LaunchDescription()

    launch_args = declare_launch_arguments()

    for arg in launch_args.values():
        ld.add_action(arg)

    declare_actions(ld, launch_args)

    return ld


def declare_launch_arguments() -> Dict:

    arg_dict = {}

    use_sim_time = DeclareLaunchArgument(
        'use_sim_time', default_value='false',
        description='Use simulation time')

    arg_dict[use_sim_time.name] = use_sim_time

    robot_name = DeclareLaunchArgument(
        'robot_name',
        default_value='pal_sea_arm',
        description='Name of the robot. ',
        choices=['pmb2', 'tiago', 'pmb3', 'tiago_dual', 'tiago_pro', 'pal_sea_arm'])

    arg_dict[robot_name.name] = robot_name

    end_effector = DeclareLaunchArgument(
        'end_effector',
        default_value='pal-pro-gripper',
        description='End effector model of the arm.',
        choices=['pal-pro-gripper', 'no-ee'])

    arg_dict[end_effector.name] = end_effector

    ft_sensor = DeclareLaunchArgument(
        'ft_sensor',
        default_value='rokubi',
        description='FT sensor model. ',
        choices=['rokubi', 'no-ft-sensor'])

    arg_dict[ft_sensor.name] = ft_sensor

    namespace = DeclareLaunchArgument(
        'namespace',
        default_value='',
        description='Define namespace of the robot. ')

    arg_dict[namespace.name] = namespace

    return arg_dict


def declare_actions(launch_description: LaunchDescription, launch_args: Dict):

    robot_description_path = os.path.join(
        get_package_share_directory('pal_sea_arm_description'),
        'robots', 'pal_sea_arm.urdf.xacro')

    robot_description_semantic = os.path.join(
        get_package_share_directory('pal_sea_arm_moveit_config'),
        'config/srdf/pal_sea_arm.srdf.xacro')

    # Trajectory Execution Functionality
    moveit_simple_controllers_path = os.path.join(
        get_package_share_directory('pal_sea_arm_moveit_config'),
        'config/controllers/controllers_pal-pro-gripper.yaml')

    planning_scene_monitor_parameters = {
        'publish_planning_scene': True,
        'publish_geometry_updates': True,
        'publish_state_updates': True,
        'publish_transforms_updates': True,
    }

    moveit_config = (
        MoveItConfigsBuilder('pal_sea_arm')
        .robot_description(file_path=robot_description_path)
        .robot_description_semantic(file_path=robot_description_semantic)
        .robot_description_kinematics(file_path=os.path.join('config', 'kinematics_kdl.yaml'))
        .trajectory_execution(moveit_simple_controllers_path)
        .planning_pipelines(pipelines=['ompl'])
        .planning_scene_monitor(planning_scene_monitor_parameters)
        .pilz_cartesian_limits(file_path=os.path.join('config', 'pilz_cartesian_limits.yaml'))
        .to_moveit_configs()
    )

    launch_description.add_action(moveit_config)

    # Start the actual move_group node/action server
    run_move_group_node = Node(
        package='moveit_ros_move_group',
        executable='move_group',
        output='screen',
        parameters=[
            {'use_sim_time': LaunchConfiguration('use_sim_time')},
            moveit_config.to_dict(),
        ],
    )
    launch_description.add_action(run_move_group_node)

    return
