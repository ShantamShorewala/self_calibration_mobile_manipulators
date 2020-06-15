; Auto-generated. Do not edit!


(cl:in-package brics_actuator-msg)


;//! \htmlinclude ProgramExecuteVelocity.msg.html

(cl:defclass <ProgramExecuteVelocity> (roslisp-msg-protocol:ros-message)
  ((velocity
    :reader velocity
    :initarg :velocity
    :type cl:fixnum
    :initform 0))
)

(cl:defclass ProgramExecuteVelocity (<ProgramExecuteVelocity>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ProgramExecuteVelocity>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ProgramExecuteVelocity)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name brics_actuator-msg:<ProgramExecuteVelocity> is deprecated: use brics_actuator-msg:ProgramExecuteVelocity instead.")))

(cl:ensure-generic-function 'velocity-val :lambda-list '(m))
(cl:defmethod velocity-val ((m <ProgramExecuteVelocity>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader brics_actuator-msg:velocity-val is deprecated.  Use brics_actuator-msg:velocity instead.")
  (velocity m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ProgramExecuteVelocity>) ostream)
  "Serializes a message object of type '<ProgramExecuteVelocity>"
  (cl:let* ((signed (cl:slot-value msg 'velocity)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ProgramExecuteVelocity>) istream)
  "Deserializes a message object of type '<ProgramExecuteVelocity>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'velocity) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ProgramExecuteVelocity>)))
  "Returns string type for a message object of type '<ProgramExecuteVelocity>"
  "brics_actuator/ProgramExecuteVelocity")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ProgramExecuteVelocity)))
  "Returns string type for a message object of type 'ProgramExecuteVelocity"
  "brics_actuator/ProgramExecuteVelocity")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ProgramExecuteVelocity>)))
  "Returns md5sum for a message object of type '<ProgramExecuteVelocity>"
  "3dafcaf7789e3ecdfbe8f6970942cec9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ProgramExecuteVelocity)))
  "Returns md5sum for a message object of type 'ProgramExecuteVelocity"
  "3dafcaf7789e3ecdfbe8f6970942cec9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ProgramExecuteVelocity>)))
  "Returns full string definition for message of type '<ProgramExecuteVelocity>"
  (cl:format cl:nil "int8 velocity~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ProgramExecuteVelocity)))
  "Returns full string definition for message of type 'ProgramExecuteVelocity"
  (cl:format cl:nil "int8 velocity~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ProgramExecuteVelocity>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ProgramExecuteVelocity>))
  "Converts a ROS message object to a list"
  (cl:list 'ProgramExecuteVelocity
    (cl:cons ':velocity (velocity msg))
))
