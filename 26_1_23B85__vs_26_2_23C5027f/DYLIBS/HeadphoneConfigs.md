## HeadphoneConfigs

> `/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs`

```diff

-451.4.0.0.0
-  __TEXT.__text: 0xca614
+452.1.0.0.0
+  __TEXT.__text: 0xca6b8
   __TEXT.__auth_stubs: 0x1d30
   __TEXT.__objc_methlist: 0x4f10
   __TEXT.__const: 0x2284
   __TEXT.__cstring: 0xaa53
-  __TEXT.__oslogstring: 0xa2ab
+  __TEXT.__oslogstring: 0xa2db
   __TEXT.__gcc_except_tab: 0x8a0
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__constg_swiftt: 0x1240

   __TEXT.__objc_methtype: 0x1c5a
   __TEXT.__objc_stubs: 0x9a20
   __DATA_CONST.__got: 0xb68
-  __DATA_CONST.__const: 0x11c0
+  __DATA_CONST.__const: 0x11d8
   __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xa8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftMetalKit.dylib
   - /usr/lib/swift/libswiftModelIO.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DC2F0B5A-AA76-3B71-834E-B23A6282C6C6
+  UUID: 75E6EC52-ED70-3636-AB67-BBC9BA12163A
   Functions: 4131
-  Symbols:   7004
-  CStrings:  6153
+  Symbols:   7010
+  CStrings:  6154
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swiftCallKit_$_HeadphoneConfigs
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage_$_HeadphoneConfigs
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
+ __swift_FORCE_LOAD_$_swiftVideoToolbox_$_HeadphoneConfigs
Functions:
~ ___36-[BTSFitTestController startFitTest]_block_invoke.138 : 864 -> 1012
~ -[BTSFitTestController resetVolume] : 268 -> 284
CStrings:
+ "Fit Test: Decrease volume for AudioVideo for fit test"

```
