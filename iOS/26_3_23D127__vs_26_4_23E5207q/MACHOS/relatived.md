## relatived

> `/usr/libexec/relatived`

```diff

-305.0.16.0.0
-  __TEXT.__text: 0x144b0
+333.0.0.0.0
+  __TEXT.__text: 0x15488
   __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_stubs: 0x3020
-  __TEXT.__objc_methlist: 0x1108
-  __TEXT.__const: 0x178
-  __TEXT.__gcc_except_tab: 0x680
-  __TEXT.__objc_methname: 0x3931
-  __TEXT.__cstring: 0xf87
+  __TEXT.__objc_stubs: 0x30e0
+  __TEXT.__objc_methlist: 0x1138
+  __TEXT.__const: 0x272
+  __TEXT.__gcc_except_tab: 0x688
+  __TEXT.__objc_methname: 0x3a81
+  __TEXT.__cstring: 0x112f
   __TEXT.__oslogstring: 0x22ca
-  __TEXT.__objc_classname: 0x3fb
-  __TEXT.__objc_methtype: 0x9ce
-  __TEXT.__unwind_info: 0x5d8
+  __TEXT.__objc_classname: 0x3fe
+  __TEXT.__objc_methtype: 0x9e0
+  __TEXT.__unwind_info: 0x6e0
   __DATA_CONST.__auth_got: 0x498
   __DATA_CONST.__got: 0x328
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xb60
-  __DATA_CONST.__cfstring: 0x980
+  __DATA_CONST.__const: 0xbb0
+  __DATA_CONST.__cfstring: 0x9c0
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x29b8
-  __DATA.__objc_selrefs: 0xd58
-  __DATA.__objc_ivar: 0x218
+  __DATA.__objc_const: 0x2a58
+  __DATA.__objc_selrefs: 0xd88
+  __DATA.__objc_ivar: 0x228
   __DATA.__objc_data: 0x780
   __DATA.__data: 0x460
-  __DATA.__bss: 0xb0
+  __DATA.__bss: 0xc0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 37CB50B3-37F0-31CD-8A20-6A97B306AB60
-  Functions: 550
-  Symbols:   259
-  CStrings:  1138
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  UUID: 666A8A60-08DC-3145-BB3A-BC04157B35FA
+  Functions: 600
+  Symbols:   265
+  CStrings:  1164
 
Symbols:
+ _MGIsDeviceOneOfType
+ ___assert_rtn
+ __os_feature_enabled_impl
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x9
CStrings:
+ "-[RMConnectionEndpoint start]"
+ "/Library/Caches/com.apple.xbs/31F4B446-2FB3-41EA-843C-67E4B77D6D1E/TemporaryDirectory.nApWMT/Sources/RelativeMotion/Common/RMConnectionEndpoint.m"
+ "/Library/Caches/com.apple.xbs/31F4B446-2FB3-41EA-843C-67E4B77D6D1E/TemporaryDirectory.nApWMT/Sources/RelativeMotion/Common/RMConnectionListener.m"
+ "/Library/Caches/com.apple.xbs/31F4B446-2FB3-41EA-843C-67E4B77D6D1E/TemporaryDirectory.nApWMT/Sources/RelativeMotion/relatived/RMDataStreamHandler.m"
+ "3"
+ "CoreLocation"
+ "OpportunisticAnchoredTracking"
+ "RMConnectionEndpoint.m"
+ "TQ,N,V_deviceMotionReferenceFrame"
+ "Tq,N,V_deviceMotionBodyFrame"
+ "_bodyFrame"
+ "_deviceMotionBodyFrame"
+ "_deviceMotionReferenceFrame"
+ "_referenceFrame"
+ "bodyFrame"
+ "deviceMotionBodyFrame"
+ "deviceMotionReferenceFrame"
+ "deviceMotionWithReferenceFrame:bodyFrame:"
+ "referenceFrame"
+ "self.connectionDelegate"
+ "self.dataDelegate"
+ "self.messagingConnection"
+ "setDeviceMotionBodyFrame:"
+ "setDeviceMotionReferenceFrame:"
+ "startDeviceMotionUpdatesUsingReferenceFrame:bodyFrame:withHandler:"
+ "unsignedIntValue"
+ "v24@?0@\"CMDeviceMotionMultiFrame\"8@\"NSError\"16"
+ "v40@0:8Q16q24@?32"
- "/Library/Caches/com.apple.xbs/Sources/RelativeMotion/Common/RMConnectionEndpoint.m"
- "/Library/Caches/com.apple.xbs/Sources/RelativeMotion/Common/RMConnectionListener.m"
- "/Library/Caches/com.apple.xbs/Sources/RelativeMotion/relatived/RMDataStreamHandler.m"
- "startDeviceMotionUpdatesWithHandler:"

```
