#include <ros/ros.h>
#include <tf/transform_listener.h>
#include <geometry_msgs/PointStamped.h>

int main(int argc,char** argv)
{
	ros::init(argc,argv,"robot_tf_listener");
	
	ros::NodeHandle nh;

	tf::TransformListener listener;
	
	ros::Rate rate(10.0);
	while(nh.ok())
	{
		geometry_msgs::PointStamped laser_point;
		laser_point.header.frame_id = "base_laser";

		laser_point.header.stamp=ros::Time();

		//假设这是激光雷达检测到的点，在其前方0.3m处
		laser_point.point.x=0.3;
		laser_point.point.y=0.0;
		laser_point.point.z=0.0;

		try
		{
			listener.waitForTransform("base_link","base_laser",ros::Time(0),ros::Duration(3.0));
			geometry_msgs::PointStamped base_point;
			listener.transformPoint("base_link",laser_point,base_point);

			ROS_INFO("base_laser:(%.2f,%.2f,%.2f)----->base_link:(%.2f,%.2f,%.2f) at time %.2f",laser_point.point.x,laser_point.point.y,laser_point.point.z,base_point.point.x,base_point.point.y,base_point.point.z,base_point.header.stamp.toSec());
		}
		catch(tf::TransformException& ex)
		{
			ROS_ERROR("Received an exception trying to transform a from \"base_laser\" to \"base_link\";%s",ex.what());
		}
		rate.sleep();	
	}	

	return 0;
}
