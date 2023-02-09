import rclpy
from rclpy.node import Node
from std_msgs.msg import String,UInt32

class WriteNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info('Hello,I am %s.'%name)
        self.pub_novel = self.create_publisher(String,'mbot',10)
        
        self.count = 0
        self.timer_period = 5
        self.timer = self.create_timer(self.timer_period,self.timer_callback)

        self.account = 80
        self.sub_money=self.create_subscription(UInt32,'mbot_money',self.rec_money_callback,10)


    def timer_callback(self):
        msg = String()
        msg.data = '第%d章:小李不困困了'%self.count
        self.pub_novel.publish(msg)
        self.get_logger().info('小李不困发布了一个章节，内容为：%s'%msg.data)
        self.count += 1

    def rec_money_callback(self,money):
        self.account += money.data
        self.get_logger().info('收到了%d稿费,现在小李不困有%d元'%(money.data,self.account))

def main(args = None):
    rclpy.init(args = args)
    li4_sub = WriteNode('li4_sub')
    rclpy.spin(li4_sub)
    rclpy.shutdown()