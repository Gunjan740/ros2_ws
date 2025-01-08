#!/usr/bin/env python3     
#interpreterlineforpython3         
import rclpy
from rclpy.node import Node

class MyNode(Node):
    
    def __init__(self):
        super().__init__("py_test")    #change node name 
        self.counter_= 0
        self.get_logger().info("Hello ros2!!!!!")
        self.create_timer(0.5,self.timer_callback)

    def timer_callback(self):
        self.counter_ += 1 
        self.get_logger().info("Hello" + str(self.counter_))



def main(args=None):
    rclpy.init(args=args)           # to intiallise the communication
    '''
    #code here starts
    node =Node("py_test")               # node created 
    node.get_logger().info("Hello ROS2")
    '''
    node = MyNode()         #change node name
    rclpy.spin(node)        # it will pause the program and keep node alive.when you start subscribers, publishers, services rhen you eill have code to execute and have callback functions and those callbacks will be clalled by this spin function.
    #code ends--
    rclpy.shutdown()                # to stop the communication


if __name__ == "__main__":
    main()