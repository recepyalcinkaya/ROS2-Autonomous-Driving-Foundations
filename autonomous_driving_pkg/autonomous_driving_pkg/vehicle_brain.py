import rclpy
from rclpy.node import Node

class VehicleBrain(Node):
    def __init__(self):
        # Düğüm (Node) ismini tanımlıyoruz
        super().__init__('vehicle_brain_node')
        self.get_logger().info('🧠 Otonom Araç Beyni Başlatıldı! Sistemler test ediliyor...')
        self.get_logger().info('Beklemede: Sensör verileri aranıyor...')

def main(args=None):
    rclpy.init(args=args)
    node = VehicleBrain()
    try:
        # Kodun kapanana kadar sürekli çalışmasını (spin) sağlar
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
