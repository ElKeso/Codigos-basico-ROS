#!/usr/bin/env python3
import rospy
from std_srvs.srv import Empty, EmptyResponse

def handle_service_request(req):
    rospy.loginfo("Service request received")
    return EmptyResponse()

def service_server():
    rospy.init_node('service_server')
    service = rospy.Service('example_service', Empty, handle_service_request)
    rospy.loginfo("Service server ready")
    rospy.spin()

if __name__ == '__main__':
    service_server()