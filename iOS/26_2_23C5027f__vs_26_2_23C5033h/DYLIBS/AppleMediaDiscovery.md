## AppleMediaDiscovery

> `/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/AppleMediaDiscovery`

```diff

-1.4.8.0.0
-  __TEXT.__text: 0xf2b60
+1.4.9.0.0
+  __TEXT.__text: 0xf1c98
   __TEXT.__auth_stubs: 0x1710
   __TEXT.__objc_methlist: 0x3b58
   __TEXT.__const: 0x8b8
-  __TEXT.__cstring: 0xb088
-  __TEXT.__oslogstring: 0x4547
+  __TEXT.__cstring: 0xaf88
+  __TEXT.__oslogstring: 0x4507
   __TEXT.__gcc_except_tab: 0x3018
   __TEXT.__dlopen_cstrs: 0xcc
   __TEXT.__swift5_typeref: 0x554

   __TEXT.__unwind_info: 0x1360
   __TEXT.__eh_frame: 0x660
   __TEXT.__objc_classname: 0x67d
-  __TEXT.__objc_methname: 0x9e82
+  __TEXT.__objc_methname: 0x9e35
   __TEXT.__objc_methtype: 0xddb
-  __TEXT.__objc_stubs: 0x8f60
-  __DATA_CONST.__got: 0x6b8
-  __DATA_CONST.__const: 0xdb0
+  __TEXT.__objc_stubs: 0x8f20
+  __DATA_CONST.__got: 0x6b0
+  __DATA_CONST.__const: 0xdc8
   __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2810
+  __DATA_CONST.__objc_selrefs: 0x2800
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x12c0
   __AUTH_CONST.__auth_got: 0xb98
   __AUTH_CONST.__const: 0xf98
-  __AUTH_CONST.__cfstring: 0xdba0
+  __AUTH_CONST.__cfstring: 0xda60
   __AUTH_CONST.__objc_const: 0x62d0
   __AUTH_CONST.__objc_intobj: 0xcd8
   __AUTH_CONST.__objc_dictobj: 0x1068

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7BF820ED-A7D0-3F8B-B886-0314A0D986FC
+  UUID: EA402108-F04B-3DBD-BD56-87286996E21C
   Functions: 1902
-  Symbols:   5324
-  CStrings:  6160
+  Symbols:   5327
+  CStrings:  6136
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAVFoundation_$_AppleMediaDiscovery
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_AppleMediaDiscovery
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftCoreMedia_$_AppleMediaDiscovery
- _OBJC_CLASS_$_CMLSimilarityClient
- _objc_msgSend$asyncResponseSimilarityScoresForElements:shardIndices:error:
- _objc_msgSend$initWithLength:
Functions:
~ +[AMDJSDebugHandler handleDebugRequest:error:] : 21884 -> 21904
~ +[AMDJSCipherMLQueryHandler triggerPECCall:withError:] : 4100 -> 144
~ sub_241d4b0f0 -> sub_241f4d268 : 156 -> 188
~ sub_241d4f1a0 -> sub_241f51338 : 964 -> 980
~ sub_241d534fc -> sub_241f556a4 : 496 -> 512
~ sub_241d54a8c -> sub_241f56c44 : 676 -> 692
~ sub_241d55c94 -> sub_241f57e5c : 376 -> 384
~ sub_241d56d1c -> sub_241f58eec : 80 -> 96
~ sub_241d57610 -> sub_241f597f0 : 300 -> 316
~ sub_241d617f0 -> sub_241f639e0 : 808 -> 824
~ sub_241d68cd4 -> sub_241f6aed4 : 64 -> 80
CStrings:
+ "This codepath is not being used currently."
- "PEC call handle, usecase %@: %@"
- "PEC use case %@ error: %@"
- "PECQueryPayload is nil"
- "PECQueryPayload is not a dictionary"
- "an embedding element is not a number"
- "an embedding is not an array"
- "asyncResponseSimilarityScoresForElements:shardIndices:error:"
- "data absent in PEC query payload"
- "data is not an array"
- "initWithLength:"
- "queryData"
- "shardIndices"
- "shardIndices absent in PEC query payload"
- "shardIndices are not an array"
- "usecase absent in PEC query payload"

```
