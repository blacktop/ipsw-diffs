## AskToExtension

> `/System/Library/ExtensionKit/Extensions/AskToExtension.appex/AskToExtension`

```diff

-57.2.1.1.0
-  __TEXT.__text: 0x1f14
-  __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__const: 0x18e
+59.1.0.0.0
+  __TEXT.__text: 0x2870
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__const: 0x24c
+  __TEXT.__constg_swiftt: 0x60
+  __TEXT.__swift5_typeref: 0x7f
+  __TEXT.__swift5_reflstr: 0x59
+  __TEXT.__swift5_fieldmd: 0x54
+  __TEXT.__cstring: 0x57
+  __TEXT.__swift5_proto: 0x20
+  __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x44
-  __TEXT.__swift5_typeref: 0x71
-  __TEXT.__swift5_fieldmd: 0x38
-  __TEXT.__swift5_reflstr: 0x49
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__objc_methname: 0x107
-  __TEXT.__cstring: 0x37
-  __TEXT.__oslogstring: 0xd8
-  __TEXT.__swift5_proto: 0x14
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xe0
+  __TEXT.__oslogstring: 0x148
+  __TEXT.__unwind_info: 0xf0
   __TEXT.__eh_frame: 0x80
-  __DATA_CONST.__auth_got: 0x258
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__auth_ptr: 0xd8
-  __DATA_CONST.__const: 0x228
+  __DATA_CONST.__auth_got: 0x288
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__auth_ptr: 0xf0
+  __DATA_CONST.__const: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x78
-  __DATA.__data: 0x40
+  __DATA.__data: 0x58
+  __DATA.__bss: 0x400
   __DATA.__common: 0x18
-  __DATA.__bss: 0x280
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Messages.framework/Messages
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AskToCore.framework/AskToCore
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

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

   - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3911CB60-5DFC-32BD-A34A-079D7390A8A9
-  Functions: 47
-  Symbols:   79
-  CStrings:  21
+  UUID: A1B70206-88D7-38A0-97AC-96B0A6832799
+  Functions: 62
+  Symbols:   80
+  CStrings:  25
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftModelIO
+ _objc_release_x26
+ _objc_retain
+ _objc_retain_x23
+ _objc_retain_x27
+ _swift_arrayDestroy
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _objc_release_x28
- _objc_retain_x20
CStrings:
+ "AskTo"
+ "AskTo breadcrumbing is not enabled"
+ "AskToBreadcrumbing"
+ "Breadcrumbing question with system ID %s using content hash %s"

```
