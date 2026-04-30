import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class SensorPublisher(Node):
    def __init__(self):
        super().__init__('lidar_sensor_node')
        
        # 'obstacle_distance' adında bir yayıncı (Publisher) oluşturuyoruz
        self.publisher_ = self.create_publisher(Float32, 'obstacle_distance', 10)
        
        # 0.5 saniyede bir timer_callback fonksiyonunu çalıştır
        timer_period = 0.5 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.get_logger().info('📡 LiDAR Sensörü Aktif: Veri yayını başlıyor...')

    def timer_callback(self):
        msg = Float32()
        # 1.0 ile 50.0 metre arası rastgele mesafe üret (Simülasyon)
        msg.data = random.uniform(1.0, 50.0) 
        
        # Veriyi ROS 2 ağına gönder
        self.publisher_.publish(msg)
        self.get_logger().info(f'Yayınlanan Engel Mesafesi: "{msg.data:.2f} metre"')

def main(args=None):
    rclpy.init(args=args)
    sensor_node = SensorPublisher()
    
    try:
        rclpy.spin(sensor_node)
    except KeyboardInterrupt:
        pass
        
    sensor_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
