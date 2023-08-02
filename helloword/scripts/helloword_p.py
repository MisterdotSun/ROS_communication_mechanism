#!/usr/bin/env python
# coding=utf-8

##指定解释器


import rospy 
if __name__ == "__main__":

	rospy.init_node("hello_p");

	rospy.loginfo("This is a log. hello word! by python!");
