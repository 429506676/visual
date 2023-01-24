#include <ros/ros.h>
#include <tf/transform_broadcaster.h>

int main(int argc,char** argv)
{
	ros::init(argc,argv,"robot_tf_broadcaster");
	
	ros::NodeHandle nh;
		
	static tf::TransformBroadcaster br;

	while(nh.ok())
	{
		tf::Transform transform;	
		transform.setOrigin(tf::Vector3(0.1,0.0,0.2));   //设置坐标原点
		//设置父坐标系（小车中心）在子坐标系（激光雷达中心）下的原点
		//即小车中心+（0.1，0.0，0.2）为雷达中心
		//（0.1，0.0，0.2）+障碍位置（x,y,z)为障碍相对小车中心的坐标

		transform.setRotation(tf::Quaternion(0,0,0,1));  //设置旋转方向，用四元数表示

		br.sendTransform(tf::StampedTransform(transform,ros::Time::now(),"base_link","base_laser"));

	}	

	return 0;
}
