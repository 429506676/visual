import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class WriteNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info('Hello,I am %s.'%name)
        self.sub_money=self.create_subscription(String,'mbot',self.rec_money_callback,10)


    def rec_money_callback(self,msg):
        self.get_logger().info('订阅了小李不困的小说，现在内容为：%s'%msg.data)


def main(args = None):
    rclpy.init(args = args)
    wang2_sub = WriteNode('wang2_sub')
    rclpy.spin(wang2_sub)
    rclpy.shutdown()