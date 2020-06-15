; Auto-generated. Do not edit!


(cl:in-package camera_control_msgs-msg)


;//! \htmlinclude GrabImagesActionGoal.msg.html

(cl:defclass <GrabImagesActionGoal> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (goal_id
    :reader goal_id
    :initarg :goal_id
    :type actionlib_msgs-msg:GoalID
    :initform (cl:make-instance 'actionlib_msgs-msg:GoalID))
   (goal
    :reader goal
    :initarg :goal
    :type camera_control_msgs-msg:GrabImagesGoal
    :initform (cl:make-instance 'camera_control_msgs-msg:GrabImagesGoal)))
)

(cl:defclass GrabImagesActionGoal (<GrabImagesActionGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GrabImagesActionGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GrabImagesActionGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name camera_control_msgs-msg:<GrabImagesActionGoal> is deprecated: use camera_control_msgs-msg:GrabImagesActionGoal instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <GrabImagesActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader camera_control_msgs-msg:header-val is deprecated.  Use camera_control_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'goal_id-val :lambda-list '(m))
(cl:defmethod goal_id-val ((m <GrabImagesActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader camera_control_msgs-msg:goal_id-val is deprecated.  Use camera_control_msgs-msg:goal_id instead.")
  (goal_id m))

(cl:ensure-generic-function 'goal-val :lambda-list '(m))
(cl:defmethod goal-val ((m <GrabImagesActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader camera_control_msgs-msg:goal-val is deprecated.  Use camera_control_msgs-msg:goal instead.")
  (goal m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GrabImagesActionGoal>) ostream)
  "Serializes a message object of type '<GrabImagesActionGoal>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal_id) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GrabImagesActionGoal>) istream)
  "Deserializes a message object of type '<GrabImagesActionGoal>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal_id) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GrabImagesActionGoal>)))
  "Returns string type for a message object of type '<GrabImagesActionGoal>"
  "camera_control_msgs/GrabImagesActionGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GrabImagesActionGoal)))
  "Returns string type for a message object of type 'GrabImagesActionGoal"
  "camera_control_msgs/GrabImagesActionGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GrabImagesActionGoal>)))
  "Returns md5sum for a message object of type '<GrabImagesActionGoal>"
  "105715bcaded1c63ade78037f4d890dd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GrabImagesActionGoal)))
  "Returns md5sum for a message object of type 'GrabImagesActionGoal"
  "105715bcaded1c63ade78037f4d890dd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GrabImagesActionGoal>)))
  "Returns full string definition for message of type '<GrabImagesActionGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%GrabImagesGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: camera_control_msgs/GrabImagesGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%##########################################~%################## GOAL ##################~%##########################################~%~%# Flag which indicates if the exposure times are provided and hence should be~%# set before grabbing~%bool exposure_given~%~%# Only relevant, if exposure_given is true:~%# The list of target exposure times in microseconds.~%# It is possible to grab only one image as well as several images with~%# different exposure times. This values can be overriden from the brightness~%# search, in case that the flag exposure_fixed is not true.~%float32[] exposure_times~%~%# Flag which indicates if the gain is provided and hence should be set before~%# grabbing~%bool gain_given~%~%# Only relevant, if gain_given is true:~%# The target gain in percent of the maximal value the camera supports.~%# For USB-Cameras, the gain is in dB, for GigE-Cameras it is given in so~%# called 'device specific units'. This value can be overriden from the~%# brightness search, in case that the gain_fixed flag is set to false.~%float32[] gain_values~%~%# Flag which indicates if the gamma value is provided and hence should be set~%# before grabbing~%bool gamma_given~%~%# Only relevant, if gain_given is true:~%# Gamma correction of pixel intensity.~%# Adjusts the brightness of the pixel values output by the camera's sensor~%# to account for a non-linearity in the human perception of brightness or~%# of the display system (such as CRT).~%float32[] gamma_values~%~%# Flag which indicates if the brightness values are provided and hence should~%# be set before grabbing~%bool brightness_given~%~%# Only relevant, if brightness_given is true:~%# The average intensity values of the images. It depends the exposure time~%# as well as the gain setting.~%float32[] brightness_values~%~%# Only relevant, if brightness_given is true:~%# If the camera should try reach the desired brightness, at least one of the~%# following flags MUST be set. If both are set, the interface will use the~%# profile that tries to keep the gain at minimum to reduce white noise.~%# 'exposure_auto' will adapt the exposure time to reach the brightness, wheras~%# 'gain_auto' does so by adapting the gain. If one of these flags is set to~%# false, the connected property will be kept fix.~%# In most of the cases trying to reach a target brightness only by varying the~%# gain and keeping the exposure time fix is not a good approach, because the~%# exposure range is many times higher than the gain range.~%bool exposure_auto~%bool gain_auto~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GrabImagesActionGoal)))
  "Returns full string definition for message of type 'GrabImagesActionGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%GrabImagesGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: camera_control_msgs/GrabImagesGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%##########################################~%################## GOAL ##################~%##########################################~%~%# Flag which indicates if the exposure times are provided and hence should be~%# set before grabbing~%bool exposure_given~%~%# Only relevant, if exposure_given is true:~%# The list of target exposure times in microseconds.~%# It is possible to grab only one image as well as several images with~%# different exposure times. This values can be overriden from the brightness~%# search, in case that the flag exposure_fixed is not true.~%float32[] exposure_times~%~%# Flag which indicates if the gain is provided and hence should be set before~%# grabbing~%bool gain_given~%~%# Only relevant, if gain_given is true:~%# The target gain in percent of the maximal value the camera supports.~%# For USB-Cameras, the gain is in dB, for GigE-Cameras it is given in so~%# called 'device specific units'. This value can be overriden from the~%# brightness search, in case that the gain_fixed flag is set to false.~%float32[] gain_values~%~%# Flag which indicates if the gamma value is provided and hence should be set~%# before grabbing~%bool gamma_given~%~%# Only relevant, if gain_given is true:~%# Gamma correction of pixel intensity.~%# Adjusts the brightness of the pixel values output by the camera's sensor~%# to account for a non-linearity in the human perception of brightness or~%# of the display system (such as CRT).~%float32[] gamma_values~%~%# Flag which indicates if the brightness values are provided and hence should~%# be set before grabbing~%bool brightness_given~%~%# Only relevant, if brightness_given is true:~%# The average intensity values of the images. It depends the exposure time~%# as well as the gain setting.~%float32[] brightness_values~%~%# Only relevant, if brightness_given is true:~%# If the camera should try reach the desired brightness, at least one of the~%# following flags MUST be set. If both are set, the interface will use the~%# profile that tries to keep the gain at minimum to reduce white noise.~%# 'exposure_auto' will adapt the exposure time to reach the brightness, wheras~%# 'gain_auto' does so by adapting the gain. If one of these flags is set to~%# false, the connected property will be kept fix.~%# In most of the cases trying to reach a target brightness only by varying the~%# gain and keeping the exposure time fix is not a good approach, because the~%# exposure range is many times higher than the gain range.~%bool exposure_auto~%bool gain_auto~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GrabImagesActionGoal>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal_id))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GrabImagesActionGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'GrabImagesActionGoal
    (cl:cons ':header (header msg))
    (cl:cons ':goal_id (goal_id msg))
    (cl:cons ':goal (goal msg))
))
