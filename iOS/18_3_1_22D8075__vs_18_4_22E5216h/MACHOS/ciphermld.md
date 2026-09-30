## ciphermld

> `/usr/libexec/ciphermld`

```diff

-239.80.5.0.0
-  __TEXT.__text: 0x290
-  __TEXT.__auth_stubs: 0x150
-  __TEXT.__const: 0x3a
-  __TEXT.__cstring: 0x6f
+274.0.0.0.0
+  __TEXT.__text: 0x824
+  __TEXT.__auth_stubs: 0x260
+  __TEXT.__const: 0x42
+  __TEXT.__cstring: 0x75
   __TEXT.__objc_methname: 0x10
-  __TEXT.__oslogstring: 0x2a
+  __TEXT.__oslogstring: 0x50
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0xa8
-  __DATA_CONST.__got: 0x8
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xa8
+  __TEXT.__swift5_typeref: 0xa
+  __TEXT.__unwind_info: 0x90
+  __DATA_CONST.__auth_got: 0x130
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
-  __DATA.__common: 0x8
+  __DATA.__data: 0x20
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CipherML.framework/CipherML

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1
-  Symbols:   46
-  CStrings:  8
+  Functions: 11
+  Symbols:   71
+  CStrings:  10
 
Symbols:
+ _$s8Dispatch0A13WorkItemFlagsVMa
+ _$s8Dispatch0A13WorkItemFlagsVMn
+ _$s8Dispatch0A13WorkItemFlagsVs10SetAlgebraAAMc
+ _$s8Dispatch0A3QoSV11unspecifiedACvgZ
+ _$s8Dispatch0A3QoSVMa
+ _$sSayxGSTsMc
+ _$sSo18OS_dispatch_sourceC8DispatchE16makeSignalSource6signal5queueSo0a1_b1_c1_H0_ps5Int32V_So0a1_b1_I0CSgtFZ
+ _$sSo18OS_dispatch_sourceP8DispatchE15setEventHandler3qos5flags7handleryAC0D3QoSV_AC0D13WorkItemFlagsVyyXBSgtF
+ _$sSo18OS_dispatch_sourceP8DispatchE6resumeyyF
+ _$ss10SetAlgebraPyxqd__ncSTRd__7ElementQyd__ACRtzlufCTj
+ _OBJC_CLASS_$_OS_dispatch_source
+ __Block_copy
+ __Block_release
+ __NSConcreteStackBlock
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftOSLog
+ _objc_release_x21
+ _objc_release_x26
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_release
+ _swift_retain
- _objc_release_x22
CStrings:
+ "Received SIGTERM, shutting down"
+ "v8@?0"

```
