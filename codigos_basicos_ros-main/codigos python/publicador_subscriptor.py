#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard %s", data.data)
    response = "Received: " + data.data
    pub.publish(response)

if __name__ == '__main__':
    rospy.init_node('pub_sub_node', anonymous=True)
    
    pub = rospy.Publisher('response', String, queue_size=10)
    rospy.Subscriber('chatter', String, callback)
    
    rospy.spin()