import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    li4_pop_node=Node('li4')
    li4_pop_node.get_logger().info('大家好，我是li4_pop')
    rclpy.spin(li4_pop_node)
    rclpy.shutdown()