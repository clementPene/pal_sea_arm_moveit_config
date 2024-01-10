controller_list:
  - name: fake_arm_torso_controller
    joints:
      - torso_lift_joint
      - arm_1_joint
      - arm_2_joint
      - arm_3_joint
      - arm_4_joint
      - arm_5_joint
      - arm_6_joint
      - arm_7_joint
  - name: fake_arm_controller
    joints:
      - arm_1_joint
      - arm_2_joint
      - arm_3_joint
      - arm_4_joint
      - arm_5_joint
      - arm_6_joint
      - arm_7_joint
@[if end_effector == "pal-pro-gripper"]@
  - name: fake_gripper_controller
    joints:
      - gripper_finger_joint
@[end if]@