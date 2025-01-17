#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list, list_to_pose
import tf
def change_end_pose(group, input_pose):
    end_goal = pose_to_list(group.get_current_pose().pose)
    for i, ele in enumerate(input_pose):
        if ele != None:
            end_goal[i] = ele
    # print  "\nOUT: ", input_pose, end_goal
    group.set_pose_target(list_to_pose(end_goal))
    if group.go(wait=True):
    # if group.plan():
        print "\nSolution found for ", input_pose
        print "\nGroup moved to ", end_goal
    else:
        print "\nNo solution found for ", input_pose
    # group.stop()

home = [0, 0.0258920968167, 0.515676649148, -0.005011902123, -0.00127171250972, -0.250399255128, 0.968128853312]
new_test_loc = [0.0, 0.01915, 0.3078, -0.00154, 0.999, -0.00792, 0.0008]
new_loc_2 = [ 3.39748068306e-05,0.0110740305564,0.318166473561,0.00154339362383,0.999989231987,0.00280462895599,0.00335974725145]

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('inverse_kinematics', anonymous=True)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_arm = moveit_commander.MoveGroupCommander("arm")
group_arm.set_planner_id("TRRT")
# group_arm.set_planner_id("SPARStwo")

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               moveit_msgs.msg.DisplayTrajectory,
                                               queue_size=20)
planning_frame = group_arm.get_planning_frame()
group_arm.set_goal_tolerance(0.005)
print "============ \nReference frame: %s" % planning_frame
eef_link = group_arm.get_end_effector_link()
print "End effector: %s" % eef_link
group_names = robot.get_group_names()
print "Goal_tolerance\n", group_arm.get_goal_tolerance()
print "Robot Groups:", robot.get_group_names(), "\n============"


print "Group_arm pose\n", group_arm.get_current_pose()
print "Joint Angles\n", group_arm.get_current_joint_values()

end_effector_coordinate = [0.0, 0.18, 0.15]
# end_effector_coordinate = [0.1, 0.197971252863, 0.157264105097]
end_effector_orientatation = [-3.14, 1.57, 0] #in euler
# end_effector_orientatation = [None, None, None] #in euler
quaternion = tf.transformations.quaternion_from_euler(end_effector_orientatation[0],end_effector_orientatation[1],end_effector_orientatation[2])
end_effector_coordinate.extend(quaternion)
end_effector_coordinate = [0.000568104599418, 0.185172728856, 0.166854905361, -0.999938911634, -0.00102509074687, 0, 0.0110054604623]
# change_end_pose(group_arm, [0.0, None, 0.5196, 0.0, 0.0, None, 1.0])
# change_end_pose(group_arm, [0, 0, 0, 0, 0, 0, 1.0])
# change_end_pose(group_arm, [0, -0.4559887551713903, 0.07897818182406445, 0.706845410317391, 0, 0, 0.707368055252284])
# change_end_pose(group_arm, [0.10, 0.10, 0.30, 0, 0, 0, 0])
# change_end_pose(group_arm, home)
# change_end_pose(group_arm, new_test_loc)
# change_end_pose(group_arm, [0.20, 0.20, 0.20, 0.707, 0.707, 0, 0.707])
print "quat:", quaternion
print "array:", end_effector_coordinate
# change_end_pose(group_arm, group_arm.get_current_pose().pose)
change_end_pose(group_arm, [0.000568104599418, 0.185172728856, 0.166854905361, -0.999938911634, -0.00102509074687, 0, 0.0110054604623])
# change_end_pose(group_arm, [0.010568104599418, 0.185172728856, 0.166854905361, -0.999938911634, -0.00102509074687, 0, 0.0110054604623])
# change_end_pose(group_arm, [0.020568104599418, 0.185172728856, 0.166854905361, -0.999938911634, -0.00102509074687, 0, 0.0110054604623])
# change_end_pose(group_arm, [0.030568104599418, 0.185172728856, 0.166854905361, -0.999938911634, -0.00102509074687, 0, 0.0110054604623])
# change_end_pose(group_arm, [0.040568104599418, 0.185172728856, 0.166854905361, -0.999938911634, -0.00102509074687, 0, 0.0110054604623])
# change_end_pose(group_arm, [0.050568104599418, 0.185172728856, 0.166854905361, -0.999938911634, -0.00102509074687, 0, 0.0110054604623])
# change_end_pose(group_arm, [0.060568104599418, 0.185172728856, 0.166854905361, -0.999938911634, -0.00102509074687, 0, 0.0110054604623])
# change_end_pose(group_arm, [0.070568104599418, 0.185172728856, 0.166854905361, -0.999938911634, -0.00102509074687, 0, 0.0110054604623])
# change_end_pose(group_arm, [0.080568104599418, 0.185172728856, 0.166854905361, -0.999938911634, -0.00102509074687, 0, 0.0110054604623])
# change_end_pose(group_arm, [0.090568104599418, 0.185172728856, 0.166854905361, -0.999938911634, -0.00102509074687, 0, 0.0110054604623])
# change_end_pose(group_arm, [0.100568104599418, 0.185172728856, 0.166854905361, -0.999938911634, -0.00102509074687, 0, 0.0110054604623])
# change_end_pose(group_arm, [0.110568104599418, 0.185172728856, 0.166854905361, -0.999938911634, -0.00102509074687, 0, 0.0110054604623])
# change_end_pose(group_arm, [0.20, 0.20, 0.20, 1, 1, 0, 1])
# change_end_pose(group_arm, [0.0, -0.2477628272874607, 0.4472224202239656, 0.3047862245403626, 0.07725225351232594, -0.23323341117218666, 0.9201845589721035])
# change_end_pose(group_arm, [0.127, 0.0, None, None, -0.037, 0.679, 0.729])
# change_end_pose(group_arm, [0.07, 0.9, 0.383, -0.076, -0.037, 0.679, 0.729])

print "\nGroup_arm pose\n", group_arm.get_current_pose()
print "Joint Angles\n", group_arm.get_current_joint_values()
# print "get_goal_joint_tolerance\n", group_arm.get_goal_joint_tolerance()
# print "get_goal_position_tolerance\n", group_arm.get_goal_position_tolerance()
# print "get_goal_orientation_tolerancees\n", group_arm.get_goal_orientation_tolerance()