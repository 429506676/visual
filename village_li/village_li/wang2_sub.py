import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from village_interface.srv import BorrowMoney

class WriteNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info('Hello,I am %s.'%name)
        self.sub_money=self.create_subscription(String,'mbot',self.rec_money_callback,10)

        self.borrow_client = self.create_client(BorrowMoney,'borrow')

    def rec_money_callback(self,msg):
        self.get_logger().info('订阅了小李不困的小说，现在内容为：%s'%msg.data)

    def borrow_money_eat(self,money=5):
        self.get_logger().info('借钱吃饭，要借%d元'%money)
        while not self.borrow_client.wait_for_service(1.0):
            self.get_logger().info('服务不在线，请稍等……')
        request = BorrowMoney.Request()
        request.name = self.get_name()
        request.money = money

        self.borrow_client.call_async(request).add_done_callback(self.borrow_response_callback)

    def borrow_response_callback(self,response):
        result = response.result()
        if result.success:
            self.get_logger().info('借到%d钱'%result.money)
        else:
            self.get_logger().info('连%d块钱都不借，呸！'%result.money)

def main(args = None):
    rclpy.init(args = args)
    wang2_sub = WriteNode('wang2')
    wang2_sub.borrow_money_eat()
    rclpy.spin(wang2_sub)
    rclpy.shutdown()