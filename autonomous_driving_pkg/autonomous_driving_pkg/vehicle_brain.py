import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from autonomous_driving_pkg.srv import EmergencyStop

class VehicleBrain(Node):
    def __init__(self):
        super().__init__('vehicle_brain_node')
        
        # 1. Parametreyi tanımla ve varsayılan bir değer ata (yaml okunamazsa 2.0 kullanır)
        self.declare_parameter('aeb_danger_distance', 2.0)
        
        self.subscription = self.create_subscription(Float32, 'obstacle_distance', self.distance_callback, 10)
        self.cli = self.create_client(EmergencyStop, 'emergency_stop')
        
        self.get_logger().info('🧠 Beyin Aktif: Sensör verileri analiz ediliyor...')

    def distance_callback(self, msg):
        distance = msg.data
        
        # 2. Parametrenin anlık güncel değerini sistemden çek
        danger_threshold = self.get_parameter('aeb_danger_distance').get_parameter_value().double_value
        
        # 3. Kıyaslamayı bu dinamik değere göre yap
        if distance < danger_threshold:
            self.get_logger().error(f'⚠️ TEHLİKE! Engel Mesafesi: {distance:.2f}m. (Sınır: {danger_threshold}m) Fren Servisi Çağrılıyor!')
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
