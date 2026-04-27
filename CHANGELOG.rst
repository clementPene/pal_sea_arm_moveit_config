^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pal_sea_arm_moveit_config
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.0.7 (2026-04-27)
------------------
* Fix prefix module move_group
* Contributors: Aina

1.0.6 (2026-04-23)
------------------
* add module dependency
* add module for movegroup
* add no-ee_ati yaml and xacro
* Contributors: ileniaperrella, susannamastromauro

1.0.5 (2025-04-17)
------------------
* Add coupler link on disable collision for allegro
* Add srdf for allegro
* Contributors: Aina

1.0.4 (2025-02-05)
------------------
* Set robot_description_timeout to 60 seconds
* Contributors: Noel Jimenez

1.0.3 (2024-06-26)
------------------
* Merge branch 'dtk/move-robot-args' into 'humble-devel'
  Change import for launch args
  See merge request robots/pal_sea_arm_moveit_config!8
* Change import for launch args
* Contributors: David ter Kuile, davidterkuile

1.0.2 (2024-05-22)
------------------
* Merge branch 'feat/auto-generated_srdf_files' into 'humble-devel'
  Feat/auto generated srdf files
  See merge request robots/pal_sea_arm_moveit_config!7
* linters
* create srdf on the go
* regenerate srdf disable collision files
* Contributors: Aina Irisarri, davidterkuile

1.0.1 (2024-03-22)
------------------
* Merge branch 'dtk/fix/restructure-launch' into 'humble-devel'
  Dtk/fix/restructure launch
  See merge request robots/pal_sea_arm_moveit_config!6
* remove sensor_manager from moveit_rviz
* Update copyright year
* Add missing linter tests
* Remove unused sensor manager
* Add missing chomp dependency
* updated config files
* Restructure launch files
* Contributors: David ter Kuile, Noel Jimenez, davidterkuile

1.0.0 (2024-01-29)
------------------
* Merge branch 'solve-depend' into 'humble-devel'
  fix depends
  See merge request robots/pal_sea_arm_moveit_config!5
* fix depends
* Merge branch 'ros2-migration' into 'humble-devel'
  Ros2 migration
  See merge request robots/pal_sea_arm_moveit_config!3
* remove torso in the configs files
* fix CMakeLists and package
* migrate move_group launch file and scripts
* migrate srdf and xacros
* migration config files
* migration of CMakeLists.txt and package.xml to ros2
* Contributors: Adria Roig, ileniaperrella

0.0.2 (2023-10-20)
------------------
* Merge branch 'fix/ft_naming' into 'main'
  Change arm_ft\_ to wrist_ft to match TIAGo
  See merge request robots/pal_sea_arm_moveit_config!2
* Change arm_ft\_ to wrist_ft to match TIAGo
* Contributors: Jordan Palacios, thomaspeyrucain

0.0.1 (2023-10-20)
------------------
* Fixing initial version
* Merge branch 'add_packages' into 'main'
  Add pal_sea_arm_moveit_config packages
  See merge request robots/pal_sea_arm_moveit_config!1
* Remove pal_sea_arm dependency
* add a disable collision when the finger is closed the 2 gripper_fingertip_right_link and gripper_fingertip_left_link are okay to touch
* Add pal_sea_arm_moveit_config packages
* Add README.md
* Contributors: Jordan Palacios, narcismiguel, thomaspeyrucain
