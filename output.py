import struct
from typing import List
from ctypes import (
    c_int8 as int8_t,
    c_uint8 as uint8_t,
    c_int16 as int16_t,
    c_uint16 as uint16_t,
    c_int32 as int32_t,
    c_uint32 as uint32_t,
    c_int64 as int64_t,
    c_uint64 as uint64_t,
    c_char as char,
    c_wchar as wchar_t,
    c_float as float_t,
    c_double as double_t
)


class Command:
    def __init__(self):

        self.red: uint8_t = 0
        self.green: uint8_t = 0
        self.blue: uint8_t = 0
        self.mod: uint8_t = 0
        self.len: int = 0
        self.time: int = 0

    def to_struct(self):
        res = bytes()
        res += struct.pack("B", self.red)
        res += struct.pack("B", self.green)
        res += struct.pack("B", self.blue)
        res += struct.pack("B", self.mod)
        res += struct.pack("i", self.len)
        res += struct.pack("i", self.time)
        return res

    def from_struct(self, binary, parsed=False):
        if not parsed:
            format_string = self.get_format_string()
            unpacked = struct.unpack(format_string, binary)
        else:
            unpacked = binary
        pos = 0

        self.red = unpacked[pos]
        pos += 1
        self.green = unpacked[pos]
        pos += 1
        self.blue = unpacked[pos]
        pos += 1
        self.mod = unpacked[pos]
        pos += 1
        self.len = unpacked[pos]
        pos += 1
        self.time = unpacked[pos]
        pos += 1
        return pos

    def get_size(self):
        format_string = self.get_format_string()
        return struct.calcsize(format_string)

    def get_format_string(self, secondary_call=False):

        format_string = ""
        format_string += 'B'  # red
        format_string += 'B'  # green
        format_string += 'B'  # blue
        format_string += 'B'  # mod
        format_string += 'i'  # len
        format_string += 'i'  # time
        format_string = '<' * (not secondary_call) + format_string
        return format_string
