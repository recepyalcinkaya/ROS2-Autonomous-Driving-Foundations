import rclpy
from rclpy.node import Node
from autonomous_driving_pkg.srv import EmergencyStop

class ActuatorController(Node):
    def __init__(self):
        super().__init__('actuator_controller_node')
        # Acil fren servisini oluşturuyoruz
        self.srv = self.create_service(EmergencyStop, 'emergency_stop', self.handle_emergency_stop)
        self.get_logger().info('⚙️ Aktüatör Sistemi Hazır: Acil Durum Servisi Dinleniyor...')

    def handle_emergency_stop(self, request, response):
        if request.confirm_stop:
            self.get_logger().warn('🚨 ACİL FREN TETİKLENDİ! Araç durduruluyor...')
            response.is_stopped = True
            response.message = "ABS ve Mekanik Frenler Tam Güçte Devrede!"
        else:
            response.is_stopped = False
            response.message = "Durma emri reddedildi."
        
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ActuatorController()
    rclpy.spin(node)
    rclpy.shutdown()
