## SignalCompression

> `/System/Library/PrivateFrameworks/SignalCompression.framework/SignalCompression`

```diff

-29.0.4.0.0
-  __TEXT.__text: 0xf928
-  __TEXT.__auth_stubs: 0x960
+29.0.7.0.0
+  __TEXT.__text: 0xf47c
+  __TEXT.__auth_stubs: 0x950
   __TEXT.__objc_methlist: 0xc4
-  __TEXT.__const: 0x1c26
-  __TEXT.__gcc_except_tab: 0x328
-  __TEXT.__oslogstring: 0xee7
-  __TEXT.__cstring: 0x4e3
-  __TEXT.__swift5_typeref: 0x254
-  __TEXT.__constg_swiftt: 0x2b8
-  __TEXT.__swift5_reflstr: 0x1a9
-  __TEXT.__swift5_fieldmd: 0x2a8
+  __TEXT.__const: 0x1c40
+  __TEXT.__gcc_except_tab: 0x31c
+  __TEXT.__oslogstring: 0xf19
+  __TEXT.__cstring: 0x4ed
+  __TEXT.__swift5_typeref: 0x25c
+  __TEXT.__constg_swiftt: 0x2e0
+  __TEXT.__swift5_reflstr: 0x1b9
+  __TEXT.__swift5_fieldmd: 0x2b4
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x88
   __TEXT.__swift5_types: 0x40
-  __TEXT.__unwind_info: 0x4e0
-  __TEXT.__eh_frame: 0x264
+  __TEXT.__unwind_info: 0x4e8
+  __TEXT.__eh_frame: 0x2cc
   __TEXT.__objc_classname: 0x2c
-  __TEXT.__objc_methname: 0x257
-  __TEXT.__objc_methtype: 0x19c
+  __TEXT.__objc_methname: 0x27e
+  __TEXT.__objc_methtype: 0x1a2
   __TEXT.__objc_stubs: 0xc0
   __DATA_CONST.__got: 0x138
   __DATA_CONST.__const: 0x80

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x4c0
-  __AUTH_CONST.__const: 0x578
+  __AUTH_CONST.__auth_got: 0x4b8
+  __AUTH_CONST.__const: 0x628
   __AUTH_CONST.__cfstring: 0x1c0
-  __AUTH_CONST.__objc_const: 0x590
+  __AUTH_CONST.__objc_const: 0x5b0
   __AUTH.__objc_data: 0x140
-  __AUTH.__data: 0x208
+  __AUTH.__data: 0x238
   __DATA.__objc_ivar: 0x38
-  __DATA.__data: 0x7c8
+  __DATA.__data: 0x7d0
   __DATA.__bss: 0x1120
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1093931F-402A-3160-8339-E5B14E8618B0
-  Functions: 367
-  Symbols:   534
-  CStrings:  209
+  UUID: AF8CF84A-25C4-3AB8-A6AE-0F38F78993E6
+  Functions: 377
+  Symbols:   538
+  CStrings:  210
 
Symbols:
+ -[MotionEncoderWrapper encodeFrameInternal:outputEncodedBuffer:outputBufferLength:type:encodeError:]
+ -[MotionEncoderWrapper encodeFrameInternal:outputEncodedBuffer:outputBufferLength:type:encodeError:].cold.1
+ -[MotionEncoderWrapper encodeFrameInternal:outputEncodedBuffer:outputBufferLength:type:encodeError:].cold.2
+ -[MotionEncoderWrapper encodeFrameInternal:outputEncodedBuffer:outputBufferLength:type:encodeError:].cold.3
+ ___swift_memcpy8_8
+ _objc_release_x24
+ _swift_dynamicCast
+ _symbolic _____Sg s5UInt8V
- -[MotionEncoderWrapper encodeFrameInternal:type:encodeError:]
- -[MotionEncoderWrapper encodeFrameInternal:type:encodeError:].cold.1
- -[MotionEncoderWrapper encodeFrameInternal:type:encodeError:].cold.2
- _objc_autoreleaseReturnValue
- _objc_release_x21
- _objc_release_x23
CStrings:
+ "Error outbuffer %p is invalid %zu"
+ "Q56@0:8r^i16*24Q32^Q40^Q48"
+ "encodeFrameInternal:outputEncodedBuffer:outputBufferLength:type:encodeError:"
+ "outbuffer"
+ "output buffer does not match requirements %ld %ld"
- "@40@0:8r^i16^Q24^Q32"
- "Invalid value: %ld,%ld"
- "Invalid values: %ld, %ld,%ld"
- "encodeFrameInternal:type:encodeError:"

```
