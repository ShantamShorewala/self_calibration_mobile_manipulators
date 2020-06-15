;; Auto-generated. Do not edit!


(when (boundp 'brics_actuator::ProgramExecuteVelocity)
  (if (not (find-package "BRICS_ACTUATOR"))
    (make-package "BRICS_ACTUATOR"))
  (shadow 'ProgramExecuteVelocity (find-package "BRICS_ACTUATOR")))
(unless (find-package "BRICS_ACTUATOR::PROGRAMEXECUTEVELOCITY")
  (make-package "BRICS_ACTUATOR::PROGRAMEXECUTEVELOCITY"))

(in-package "ROS")
;;//! \htmlinclude ProgramExecuteVelocity.msg.html


(defclass brics_actuator::ProgramExecuteVelocity
  :super ros::object
  :slots (_velocity ))

(defmethod brics_actuator::ProgramExecuteVelocity
  (:init
   (&key
    ((:velocity __velocity) 0)
    )
   (send-super :init)
   (setq _velocity (round __velocity))
   self)
  (:velocity
   (&optional __velocity)
   (if __velocity (setq _velocity __velocity)) _velocity)
  (:serialization-length
   ()
   (+
    ;; int8 _velocity
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _velocity
       (write-byte _velocity s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _velocity
     (setq _velocity (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _velocity 127) (setq _velocity (- _velocity 256)))
   ;;
   self)
  )

(setf (get brics_actuator::ProgramExecuteVelocity :md5sum-) "3dafcaf7789e3ecdfbe8f6970942cec9")
(setf (get brics_actuator::ProgramExecuteVelocity :datatype-) "brics_actuator/ProgramExecuteVelocity")
(setf (get brics_actuator::ProgramExecuteVelocity :definition-)
      "int8 velocity

")



(provide :brics_actuator/ProgramExecuteVelocity "3dafcaf7789e3ecdfbe8f6970942cec9")


