import rclpy
from rclpy.node import Node
from std_msgs.msg import String,UInt32
from village_interface.srv import BorrowMoney

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

        self.borrow_server=self.create_service(BorrowMoney,'borrow',self.borrow_money_callback)
        self.declare_parameter('writer_timer_period',5)

    def borrow_money_callback(self,request,response):
        self.get_logger().info('收到来自%s的借钱请求，帐户里目前有%d'%(request.name,self.account))
        if request.money <= self.account*0.1:
            response.success = True
            response.money = request.money
            self.account = self.account - request.money
            self.get_logger().info('借钱成功，借出%d，目前账户还有%d'%(response.money,self.account))
        else:
            response.success = False
            response.money = 0
            self.get_logger().info('对不起，小李不困不能借给你')
        return response

    def timer_callback(self):
        timer_period = self.get_parameter('writer_timer_period').get_parameter_value().integer_value
        self.timer.timer_period_ns = timer_period * (1000*1000*1000)
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