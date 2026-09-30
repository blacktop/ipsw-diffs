## SatelliteSMS

> `/System/Library/Messages/PlugIns/SatelliteSMS.imservice/SatelliteSMS`

```diff

-1436.100.6.2.12
-  __TEXT.__text: 0xbad4
+1440.100.7.2.5
+  __TEXT.__text: 0xbacc
   __TEXT.__auth_stubs: 0xb80
   __TEXT.__objc_stubs: 0x2c0
   __TEXT.__objc_methlist: 0x37c
   __TEXT.__const: 0x3aa
-  __TEXT.__objc_methname: 0x10b4
+  __TEXT.__objc_methname: 0x10dc
   __TEXT.__oslogstring: 0x93f
   __TEXT.__cstring: 0x4f1
   __TEXT.__swift5_typeref: 0x18c

   __DATA_CONST.__auth_got: 0x5d0
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x5b8
+  __DATA_CONST.__const: 0x598
   __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA.__objc_const: 0x810
-  __DATA.__objc_selrefs: 0x460
+  __DATA.__objc_selrefs: 0x468
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x1b0
   __DATA.__data: 0x408

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftMetalKit.dylib
+  - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F5E380A9-1F1C-3088-A83C-F4FBC7BFE271
+  UUID: 02AB77E6-9A6C-32B9-9657-6D556A7C65C3
   Functions: 199
-  Symbols:   199
-  CStrings:  300
+  Symbols:   197
+  CStrings:  301
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftModelIO
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
Functions:
~ sub_8604 -> sub_8564 : 1704 -> 1696
CStrings:
+ "originalServiceName"
+ "trackSentMessageEventOfType:subtype:originalServiceName:messageSize:sendDuration:receiverType:receiverGroupType:wasSuccessful:handle:error:"
- "trackSentMessageEventOfType:subtype:messageSize:sendDuration:receiverType:receiverGroupType:wasSuccessful:handle:error:"

```
