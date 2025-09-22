## NPTKit

> `/System/Library/PrivateFrameworks/NPTKit.framework/NPTKit`

```diff

-190.0.0.0.0
-  __TEXT.__text: 0x4d5f4
-  __TEXT.__auth_stubs: 0x11b0
-  __TEXT.__objc_methlist: 0x4c4c
+192.0.1.0.0
+  __TEXT.__text: 0x4da44
+  __TEXT.__auth_stubs: 0x11d0
+  __TEXT.__objc_methlist: 0x4c7c
   __TEXT.__const: 0x528
   __TEXT.__cstring: 0x4078
-  __TEXT.__gcc_except_tab: 0xad4
+  __TEXT.__gcc_except_tab: 0xab8
   __TEXT.__oslogstring: 0x1065
   __TEXT.__swift5_typeref: 0x64f
   __TEXT.__swift5_capture: 0x450

   __TEXT.__swift_as_ret: 0x54
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0xd38
+  __TEXT.__unwind_info: 0xd40
   __TEXT.__eh_frame: 0x898
-  __TEXT.__objc_classname: 0x3b1
-  __TEXT.__objc_methname: 0xdfed
+  __TEXT.__objc_classname: 0x3b2
+  __TEXT.__objc_methname: 0xe08e
   __TEXT.__objc_methtype: 0x1967
-  __TEXT.__objc_stubs: 0x8680
-  __DATA_CONST.__got: 0x390
-  __DATA_CONST.__const: 0xa68
+  __TEXT.__objc_stubs: 0x8720
+  __DATA_CONST.__got: 0x398
+  __DATA_CONST.__const: 0xaa8
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35d0
+  __DATA_CONST.__objc_selrefs: 0x35f8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x2c8
-  __AUTH_CONST.__auth_got: 0x8e8
+  __AUTH_CONST.__auth_got: 0x8f8
   __AUTH_CONST.__const: 0xef8
   __AUTH_CONST.__cfstring: 0x6240
-  __AUTH_CONST.__objc_const: 0xc4b8
+  __AUTH_CONST.__objc_const: 0xc4f8
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x258
-  __DATA.__objc_ivar: 0x740
+  __DATA.__objc_ivar: 0x744
   __DATA.__data: 0x718
   __DATA.__bss: 0x180
   __DATA.__common: 0x30

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DE975D0F-3265-3AF0-ABC1-93B2B78082B4
-  Functions: 2008
-  Symbols:   5858
-  CStrings:  4504
+  UUID: B657D8BB-CF61-31DC-94C8-5579F32B03D8
+  Functions: 2016
+  Symbols:   5883
+  CStrings:  4512
 
Symbols:
+ -[SimplePing isInvalidated]
+ -[SimplePing setIsInvalidated:]
+ -[SimplePing setTimeoutTimer:]
+ -[SimplePing timeoutTimer]
+ _CFRetain
+ _CFRunLoopPerformBlock
+ _CFRunLoopWakeUp
+ _OBJC_CLASS_$_NSURLConnection
+ _OBJC_IVAR_$_SimplePing._isInvalidated
+ _OBJC_IVAR_$_SimplePing._timeoutTimer
+ ___15-[NPTPing stop]_block_invoke
+ ___24-[SimplePing stopSocket]_block_invoke
+ ___32-[SimplePing stopHostResolution]_block_invoke
+ ___39-[NPTPing simplePing:didFailWithError:]_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_50_e8_32s40w_e5_v8?0lw40l8s32l8
+ _objc_msgSend$isInvalidated
+ _objc_msgSend$resourceLoaderRunLoop
+ _objc_msgSend$setIsInvalidated:
+ _objc_msgSend$setTimeoutTimer:
+ _objc_msgSend$timeoutTimer
- _CFRunLoopGetCurrent
- _OBJC_IVAR_$_SimplePing.timeoutTimer
- ___block_descriptor_50_e8_32s40s_e5_v8?0ls32l8s40l8
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_NPTKit
CStrings:
+ "!"
+ "T@\"NSData\",C,V_hostAddress"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_timeoutTimer"
+ "T@\"NSString\",R,C,V_hostName"
+ "TB,V_isInvalidated"
+ "TC,R"
+ "TS,V_nextSequenceNumber"
+ "_isInvalidated"
+ "_timeoutTimer"
+ "isInvalidated"
+ "resourceLoaderRunLoop"
+ "setIsInvalidated:"
+ "setTimeoutTimer:"
- "1"
- "T@\"NSData\",C,N,V_hostAddress"
- "T@\"NSString\",R,C,N,V_hostName"
- "TC,R,N"
- "TS,N,V_nextSequenceNumber"

```
