import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from autonomous_driving_pkg.srv import EmergencyStop

class VehicleBrain(Node):
    def __init__(self):
        super().__init__('vehicle_brain_node')
        
        # Sensörü dinlemek için Subscriber
        self.subscription = self.create_subscription(Float32, 'obstacle_distance', self.distance_callback, 10)
        
        # Acil fren servisi için Client (Müşteri)
        self.cli = self.create_client(EmergencyStop, 'emergency_stop')
        
        self.get_logger().info('🧠 Beyin Aktif: Sensör verileri analiz ediliyor...')

    def distance_callback(self, msg):
        distance = msg.data
        if distance < 2.0: # 2 metreden yakınsa
            self.get_logger().error(f'⚠️ TEHLİKE! Engel Mesafesi: {distance:.2f}m. Fren Servisi Çağrılıyor!')
            self.call_emergency_stop()

    def call_emergency_stop(self):
        # Servisin aktif olup olmadığını kontrol et
        if not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Servis aktif değil, bekleniyor...')
            return

        req = EmergencyStop.Request()
        req.confirm_stop = True
        
        # Servisi asenkron olarak çağır
        self.cli.call_async(req)

def main(args=None):
    rclpy.init(args=args)
    node = VehicleBrain()
    rclpy.spin(node)
    rclpy.shutdown()
