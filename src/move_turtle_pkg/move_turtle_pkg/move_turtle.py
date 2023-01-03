import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile
import math

class Move_turtle(Node):
  def __init__(self):
    super().__init__('move_turtle')
    self.qos_profile = QoSProfile(depth = 10)
    self.move_turtle = self.create_publisher(Twist,'turtle1/cmd_vel',self.qos_profile)
    self.move_turtle2 = self.create_publisher(Twist,'turtle2/cmd_vel',self.qos_profile)
    self.move_turtle3 = self.create_publisher(Twist,'turtle3/cmd_vel',self.qos_profile)

    self.timer = self.create_timer(0.1, self.turtle_move)
    self.timer = self.create_timer(0.1, self.turtle_move2)
    self.timer = self.create_timer(0.1, self.turtle_move3)


    self.velocity=0.0
    self.theta=0.0

  def turtle_move(self):
    msg = Twist()
    msg.linear.x = self.velocity
    msg.linear.y = 0.0
    msg.linear.z = 0.0

    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = 2.0

    self.move_turtle.publish(msg)
    self.get_logger().info(f'Published mesage: {msg.linear},{msg.angular}')
    self.velocity += 0.01
    self.theta += 0.1

  def turtle_move2(self):
    msg = Twist()
    msg.linear.x = self.velocity * math.cos(45)
    msg.linear.y = 0.0
    msg.linear.z = 0.0

    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = -2.0

    self.move_turtle2.publish(msg)
    self.get_logger().info(f'Published mesage: {msg.linear},{msg.angular}')
    self.velocity += 0.01
    self.theta += 0.1

  def turtle_move3(self):
    msg = Twist()
    msg.linear.x = self.velocity * math.sin(60)
    msg.linear.y = 0.0
    msg.linear.z = 0.0

    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = -2.0

    self.move_turtle2.publish(msg)
    self.get_logger().info(f'Published mesage: {msg.linear},{msg.angular}')
    self.velocity += 0.01
    self.theta += 0.1

def main(args=None):
  rclpy.init(args=args)
  node = Move_turtle()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    node.get_logger().info('Keyboard interrupt!!!!')
  finally:
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()
