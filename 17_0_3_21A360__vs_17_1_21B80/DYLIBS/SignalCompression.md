## SignalCompression

> `/System/Library/PrivateFrameworks/SignalCompression.framework/SignalCompression`

```diff

-7.0.0.0.0
-  __TEXT.__text: 0x8634
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0xa0
+12.0.0.0.0
+  __TEXT.__text: 0x8da4
+  __TEXT.__auth_stubs: 0x780
+  __TEXT.__objc_methlist: 0xc8
   __TEXT.__const: 0x15a6
-  __TEXT.__gcc_except_tab: 0x15c
-  __TEXT.__cstring: 0x423
+  __TEXT.__gcc_except_tab: 0x198
+  __TEXT.__cstring: 0x443
+  __TEXT.__oslogstring: 0xfe
   __TEXT.__constg_swiftt: 0x20c
   __TEXT.__swift5_typeref: 0x15e
   __TEXT.__swift5_reflstr: 0x189

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__unwind_info: 0x3d8
+  __TEXT.__unwind_info: 0x3e4
   __TEXT.__eh_frame: 0x260
   __TEXT.__objc_classname: 0x2c
-  __TEXT.__objc_methname: 0x201
-  __TEXT.__objc_methtype: 0x121
-  __TEXT.__objc_stubs: 0x80
+  __TEXT.__objc_methname: 0x259
+  __TEXT.__objc_methtype: 0x1a9
+  __TEXT.__objc_stubs: 0xc0
   __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x48
+  __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4c0
-  __DATA_CONST.__objc_selrefs: 0x78
-  __AUTH_CONST.__cfstring: 0x20
+  __DATA_CONST.__objc_const: 0x4e0
+  __DATA_CONST.__objc_selrefs: 0x88
+  __AUTH_CONST.__const: 0x570
   __AUTH_CONST.__objc_const: 0x90
-  __AUTH_CONST.__const: 0x530
-  __AUTH_CONST.__auth_got: 0x3b8
+  __AUTH_CONST.__auth_got: 0x3d0
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x200
   __DATA.__objc_classrefs: 0x18
   __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x34
+  __DATA.__objc_ivar: 0x38
   __DATA.__data: 0x760
-  __DATA.__bss: 0x780
+  __DATA.__bss: 0x7a0
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E22389EC-7901-3F19-9A01-0A0A3D19360D
-  Functions: 264
-  Symbols:   346
-  CStrings:  86
+  UUID: C61744E4-5A9A-31CF-91FA-E77B6623D0E0
+  Functions: 278
+  Symbols:   381
+  CStrings:  98
 
Symbols:
+ -[MotionDecoderWrapper .cxx_construct]
+ -[MotionDecoderWrapper decodeFrameInternal:decodedFrame:decodeError:].cold.1
+ -[MotionDecoderWrapper motionDecoderWrapperLogSharedInstance]
+ -[MotionEncoderWrapper encodeFrameInternal:type:encodeError:].cold.1
+ -[MotionEncoderWrapper encodeFrameInternal:type:encodeError:].cold.2
+ -[MotionEncoderWrapper initWithAttributeCount:componentCount:quantization:].cold.1
+ -[MotionEncoderWrapper motionEncoderWrapperLogSharedInstance]
+ GCC_except_table15
+ GCC_except_table2
+ GCC_except_table8
+ GCC_except_table9
+ _OBJC_IVAR_$_MotionDecoderWrapper.encoderInfo
+ __NSConcreteGlobalBlock
+ __ZN3gcl6motion7Decoder17getCurrentFrameQPEv
+ __ZN3gcl6motion7Decoder20getCurrentFrameFlagsEv
+ __ZN3gcl6motion7Decoder21getCurrentFrameNumberEv
+ __ZN3gcl6motion7Decoder25getlastDecodedFrameNumberEv
+ __ZN3gcl6motion7Decoder28getCurrentFramePayloadLengthEv
+ __ZZ61-[MotionDecoderWrapper motionDecoderWrapperLogSharedInstance]E14sharedInstance
+ __ZZ61-[MotionDecoderWrapper motionDecoderWrapperLogSharedInstance]E9onceToken
+ __ZZ61-[MotionEncoderWrapper motionEncoderWrapperLogSharedInstance]E14sharedInstance
+ __ZZ61-[MotionEncoderWrapper motionEncoderWrapperLogSharedInstance]E9onceToken
+ ___61-[MotionDecoderWrapper motionDecoderWrapperLogSharedInstance]_block_invoke
+ ___61-[MotionEncoderWrapper motionEncoderWrapperLogSharedInstance]_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_literal_global
+ __os_log_error_impl
+ _dispatch_once
+ _objc_msgSend$motionDecoderWrapperLogSharedInstance
+ _objc_msgSend$motionEncoderWrapperLogSharedInstance
+ _os_log_create
- GCC_except_table0
- GCC_except_table1
- GCC_except_table12
- GCC_except_table13
- _NSLog
- ___CFConstantStringClassReference
CStrings:
+ "Could not serialize encoder params"
+ "Error Input buffer is null"
+ "Error cannot compress inputs %d"
+ "Failed to decode with error %d c:%d p:%d q:%d l:%d f:%d"
+ "Local Encoder version is %d %d %d"
+ "Remote Encoder version is %d %d %d, Local Encoder version is %d %d %d"
+ "com.apple.signalcompression"
+ "encoderInfo"
+ "motionDecoderWrapper"
+ "motionDecoderWrapperLogSharedInstance"
+ "motionEncoderWrapper"
+ "motionEncoderWrapperLogSharedInstance"
+ "v8@?0"
+ "{AttributeInfo=\"apiVersion\"i\"version\"{Version=\"major\"C\"minor\"C\"revision\"S}\"attributeCount\"i\"componentsPerAttribute\"i\"quatizationBits\"C}"
- "Error: can't start encoding frame sequence!"

```
