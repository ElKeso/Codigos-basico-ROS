import rospy

from geometry_msgs.msg import PoseStamped



class Base_Drone:
    def __init__(self):
        self.data = PoseStamped
        self.subscriber_base = rospy.Subscriber("/topico", PoseStamped, self.callback)

    def callback(self, msg):
        self.data = msg

    def get_data(self):
        return self.data
    


if __name__ == "__main__":
    rospy.init_node("ejemplo")
    rate = rospy.Rate(1)
    data = Base_Drone.get_data()
    

