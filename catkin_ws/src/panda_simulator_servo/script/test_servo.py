#!/usr/bin/env python3
import rospy
from control_msgs.msg import JointJog

rospy.init_node('test_servo')
pub = rospy.Publisher('/servo_server/delta_joint_cmds', JointJog, queue_size=1)
rate = rospy.Rate(50)

msg = JointJog()
msg.header.frame_id = 'panda_link0'
msg.joint_names = ['panda_joint1']
msg.velocities = [0.1]  # rad/s

while not rospy.is_shutdown():
    msg.header.stamp = rospy.Time.now()
    pub.publish(msg)
    rate.sleep()
