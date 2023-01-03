import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile


class Move_turtle2(Node):
  def __init__(self):
    super().__init__('move_turtle2')
    self.qos_profile = QoSProfile(depth = 10)
    self.move_turtle2 = self.create_publisher(Twist,'turtle2/cmd_vel',self.qos_profile)
    self.timer = self.create_timer(0.1, self.turtle_move)
    self.velocity=0.0

  def turtle_move(self):
    msg = Twist()
    msg.linear.x = self.velocity
    msg.linear.y = 0.0
    msg.linear.z = 0.0

    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = -2.0

    self.move_turtle2.publish(msg)
    self.get_logger().info(f'Published mesage: {msg.linear},{msg.angular}')
    self.velocity +=0.01

def main(args=None):
  rclpy.init(args=args)
  node = Move_turtle2()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    node.get_logger().info('Keyboard interrupt!!!!')
  finally:
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()
