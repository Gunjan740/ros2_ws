#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberCounterNode(Node):  
    def __init__(self):
        super().__init__("number_counter") 
        self.counter_ = 0  # Initialize 
        
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)

        self.subscriber_ = self.create_subscription(Int64,"number", self.callback_number, 10) 
        self.get_logger().info("Smartphone has been started.")

        
    def callback_number(self, msg):
        self.counter_ += 1  # Increment counter
        self.get_logger().info(f"Message: {msg.data}")  # Log message and counter

        counter_msg = Int64()
        counter_msg.data = self.counter_
        self.publisher_.publish(counter_msg)  

def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()  
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
