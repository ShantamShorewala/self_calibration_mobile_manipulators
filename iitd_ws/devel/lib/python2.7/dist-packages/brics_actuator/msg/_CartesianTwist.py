# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from brics_actuator/CartesianTwist.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import brics_actuator.msg
import genpy

class CartesianTwist(genpy.Message):
  _md5sum = "e86336d0ca57e442a1f55b8cb29e1a22"
  _type = "brics_actuator/CartesianTwist"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """time timeStamp
Poison poisonStamp
string base_frame_uri
string target_frame_uri
# need some more frames?	
CartesianVector translation 
CartesianVector rotation

================================================================================
MSG: brics_actuator/Poison
string originator 		# node id
string description 		# encoding still an issue
float32 qos			# reliability of the channel
				# 0..1 where 1 means healthy

================================================================================
MSG: brics_actuator/CartesianVector
string unit
float64 x
float64 y
float64 z
"""
  __slots__ = ['timeStamp','poisonStamp','base_frame_uri','target_frame_uri','translation','rotation']
  _slot_types = ['time','brics_actuator/Poison','string','string','brics_actuator/CartesianVector','brics_actuator/CartesianVector']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       timeStamp,poisonStamp,base_frame_uri,target_frame_uri,translation,rotation

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CartesianTwist, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.timeStamp is None:
        self.timeStamp = genpy.Time()
      if self.poisonStamp is None:
        self.poisonStamp = brics_actuator.msg.Poison()
      if self.base_frame_uri is None:
        self.base_frame_uri = ''
      if self.target_frame_uri is None:
        self.target_frame_uri = ''
      if self.translation is None:
        self.translation = brics_actuator.msg.CartesianVector()
      if self.rotation is None:
        self.rotation = brics_actuator.msg.CartesianVector()
    else:
      self.timeStamp = genpy.Time()
      self.poisonStamp = brics_actuator.msg.Poison()
      self.base_frame_uri = ''
      self.target_frame_uri = ''
      self.translation = brics_actuator.msg.CartesianVector()
      self.rotation = brics_actuator.msg.CartesianVector()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2I().pack(_x.timeStamp.secs, _x.timeStamp.nsecs))
      _x = self.poisonStamp.originator
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.poisonStamp.description
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_f().pack(self.poisonStamp.qos))
      _x = self.base_frame_uri
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.target_frame_uri
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.translation.unit
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3d().pack(_x.translation.x, _x.translation.y, _x.translation.z))
      _x = self.rotation.unit
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3d().pack(_x.rotation.x, _x.rotation.y, _x.rotation.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.timeStamp is None:
        self.timeStamp = genpy.Time()
      if self.poisonStamp is None:
        self.poisonStamp = brics_actuator.msg.Poison()
      if self.translation is None:
        self.translation = brics_actuator.msg.CartesianVector()
      if self.rotation is None:
        self.rotation = brics_actuator.msg.CartesianVector()
      end = 0
      _x = self
      start = end
      end += 8
      (_x.timeStamp.secs, _x.timeStamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.poisonStamp.originator = str[start:end].decode('utf-8')
      else:
        self.poisonStamp.originator = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.poisonStamp.description = str[start:end].decode('utf-8')
      else:
        self.poisonStamp.description = str[start:end]
      start = end
      end += 4
      (self.poisonStamp.qos,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.base_frame_uri = str[start:end].decode('utf-8')
      else:
        self.base_frame_uri = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.target_frame_uri = str[start:end].decode('utf-8')
      else:
        self.target_frame_uri = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.translation.unit = str[start:end].decode('utf-8')
      else:
        self.translation.unit = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.translation.x, _x.translation.y, _x.translation.z,) = _get_struct_3d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.rotation.unit = str[start:end].decode('utf-8')
      else:
        self.rotation.unit = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.rotation.x, _x.rotation.y, _x.rotation.z,) = _get_struct_3d().unpack(str[start:end])
      self.timeStamp.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2I().pack(_x.timeStamp.secs, _x.timeStamp.nsecs))
      _x = self.poisonStamp.originator
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.poisonStamp.description
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_f().pack(self.poisonStamp.qos))
      _x = self.base_frame_uri
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.target_frame_uri
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.translation.unit
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3d().pack(_x.translation.x, _x.translation.y, _x.translation.z))
      _x = self.rotation.unit
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3d().pack(_x.rotation.x, _x.rotation.y, _x.rotation.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.timeStamp is None:
        self.timeStamp = genpy.Time()
      if self.poisonStamp is None:
        self.poisonStamp = brics_actuator.msg.Poison()
      if self.translation is None:
        self.translation = brics_actuator.msg.CartesianVector()
      if self.rotation is None:
        self.rotation = brics_actuator.msg.CartesianVector()
      end = 0
      _x = self
      start = end
      end += 8
      (_x.timeStamp.secs, _x.timeStamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.poisonStamp.originator = str[start:end].decode('utf-8')
      else:
        self.poisonStamp.originator = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.poisonStamp.description = str[start:end].decode('utf-8')
      else:
        self.poisonStamp.description = str[start:end]
      start = end
      end += 4
      (self.poisonStamp.qos,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.base_frame_uri = str[start:end].decode('utf-8')
      else:
        self.base_frame_uri = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.target_frame_uri = str[start:end].decode('utf-8')
      else:
        self.target_frame_uri = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.translation.unit = str[start:end].decode('utf-8')
      else:
        self.translation.unit = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.translation.x, _x.translation.y, _x.translation.z,) = _get_struct_3d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.rotation.unit = str[start:end].decode('utf-8')
      else:
        self.rotation.unit = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.rotation.x, _x.rotation.y, _x.rotation.z,) = _get_struct_3d().unpack(str[start:end])
      self.timeStamp.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f