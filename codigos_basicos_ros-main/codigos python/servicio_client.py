#!/usr/bin/env python3
import rospy
from std_srvs.srv import Empty

def service_client():
    rospy.init_node('service_client')
    rospy.wait_for_service('example_service')
    try:
        example_service = rospy.ServiceProxy('example_service', Empty)
        resp = example_service()
        rospy.loginfo("Service call successful")
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)

if __name__ == '__main__':
    service_client()