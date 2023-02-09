import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class WriteNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info('Hello,I am %s.'%name)
        self.pub_novel = self.create_publisher(String,'mbot',10)
        
        self.count = 0
        self.timer_period = 5
        self.timer = self.create_timer(self.timer_period,self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = '第%d章:小李不困困了'%self.count
        self.pub_novel.publish(msg)
        self.get_logger().info('小李不困发布了一个章节，内容为：%s'%msg.data)
        self.count += 1

def main(args = None):
    rclpy.init(args = args)
    li4_pub = WriteNode('li4_pub')
    rclpy.spin(li4_pub)
    rclpy.shutdown()