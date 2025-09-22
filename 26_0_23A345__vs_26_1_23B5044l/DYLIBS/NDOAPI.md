## NDOAPI

> `/System/Library/PrivateFrameworks/NDOAPI.framework/NDOAPI`

```diff

-502.0.0.0.0
-  __TEXT.__text: 0xcf878
-  __TEXT.__auth_stubs: 0x12a0
+511.0.0.0.0
+  __TEXT.__text: 0xd0c1c
+  __TEXT.__auth_stubs: 0x12e0
   __TEXT.__objc_methlist: 0x15c
-  __TEXT.__const: 0xb208
-  __TEXT.__cstring: 0x367e
-  __TEXT.__constg_swiftt: 0x20a4
-  __TEXT.__swift5_typeref: 0x1ef6
-  __TEXT.__swift5_reflstr: 0x1f00
-  __TEXT.__swift5_fieldmd: 0x259c
-  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__const: 0xb258
+  __TEXT.__cstring: 0x371e
+  __TEXT.__constg_swiftt: 0x20c0
+  __TEXT.__swift5_typeref: 0x1f7c
+  __TEXT.__swift5_reflstr: 0x1f50
+  __TEXT.__swift5_fieldmd: 0x25d0
+  __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x570
-  __TEXT.__swift5_proto: 0x940
+  __TEXT.__swift5_proto: 0x944
   __TEXT.__swift5_types: 0x254
-  __TEXT.__swift5_capture: 0x5c8
-  __TEXT.__oslogstring: 0x10f0
+  __TEXT.__swift5_capture: 0x5ec
+  __TEXT.__oslogstring: 0x1120
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__swift_as_entry: 0x28
+  __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x28
-  __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x4188
-  __TEXT.__eh_frame: 0x55f8
+  __TEXT.__swift5_mpenum: 0x18
+  __TEXT.__unwind_info: 0x41b8
+  __TEXT.__eh_frame: 0x5680
   __TEXT.__objc_classname: 0x1b
   __TEXT.__objc_methname: 0x67d
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0xe78
+  __DATA_CONST.__got: 0x3a8
+  __DATA_CONST.__const: 0xe70
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2b0
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x950
-  __AUTH_CONST.__const: 0x2c50
+  __AUTH_CONST.__auth_got: 0x970
+  __AUTH_CONST.__const: 0x2cc8
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x1b58
   __AUTH.__objc_data: 0x170
   __AUTH.__data: 0x1638
-  __DATA.__data: 0x1a48
-  __DATA.__bss: 0xdfe0
+  __DATA.__data: 0x1a98
+  __DATA.__bss: 0xe060
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0x39d0
   __DATA_DIRTY.__bss: 0x3c00

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
-  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4302D2CC-478A-35FA-9453-8A7CD1A3F214
-  Functions: 6052
-  Symbols:   1261
-  CStrings:  728
+  UUID: 9D2B571B-1875-3563-B77F-3375A8DA4DAA
+  Functions: 6072
+  Symbols:   1275
+  CStrings:  734
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_NSObject
+ _symbolic SS_So8NSObjectCt
+ _symbolic Sb16forUniversalLink_t
+ _symbolic Si11forConsumer_t
+ _symbolic Si5inApp_t
+ _symbolic _____ 6NDOAPI11NDOAnalyticO
+ _symbolic ______AAt 6NDOAPI9NDOErrorsO
+ _symbolic _____ySSSo8NSObjectCG s18_DictionaryStorageC
+ _symbolic _____ySS_So8NSObjectCtG s23_ContiguousArrayStorageC
- __swift_FORCE_LOAD_$_swiftOSLog
- __swift_FORCE_LOAD_$_swiftOSLog_$_NDOAPI
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "Sending analytic event: %s with payload %s"
+ "com.apple.newdeviceoutreach."
+ "coverage.viewload"
+ "coverageCentralLoaded"
+ "followupDisplayCount"

```
