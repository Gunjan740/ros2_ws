#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberPublisherNode(Node):  
    def __init__(self):
        super().__init__("number_publisher") 
        #self.declare_parameter("test123")            # declaring neww parameter
        #self.declare_parameter("another_param") 
        self.declare_parameter("number_to_publish",2)     #2 is default parameter

        self.number_ = self.get_parameter("number_to_publish").value
# robot_news_ ststion is a publisher which is publishing a message on robot_news topic
        self.publisher_ =self.create_publisher(Int64, "number", 10)
        self.timer_ = self.create_timer(0.5,self.publish_number)
        self.get_logger().info("number publisher has been started.")

    def publish_number(self):
        msg = Int64()
        msg.data = self.number_

        self.publisher_.publish(msg)    

def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode()  
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
