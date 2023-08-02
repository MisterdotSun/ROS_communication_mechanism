#include "ros/ros.h"
int main(int argc,char *argv[])
{
	ros::init(argc,argv,"hello_node");	
	ROS_INFO("This is a log. hello word! by c++"); 
	return 0;
}
