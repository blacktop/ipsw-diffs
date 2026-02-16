## modelcatalogdump

> `/usr/bin/modelcatalogdump`

```diff

-218.28.0.0.0
-  __TEXT.__text: 0x1615c
-  __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__cstring: 0x566
-  __TEXT.__const: 0x5cc
+233.32.1.0.0
+  __TEXT.__text: 0x15438
+  __TEXT.__auth_stubs: 0xfc0
+  __TEXT.__objc_stubs: 0x120
+  __TEXT.__const: 0x5ac
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0xa0
-  __TEXT.__swift5_typeref: 0x3d1
+  __TEXT.__swift5_typeref: 0x3b1
   __TEXT.__swift5_fieldmd: 0x78
+  __TEXT.__cstring: 0x5a6
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x34
   __TEXT.__swift5_types: 0x10
-  __TEXT.__swift_as_entry: 0x28
-  __TEXT.__swift_as_ret: 0x48
-  __TEXT.__swift5_capture: 0x50
-  __TEXT.__objc_methname: 0x9e
+  __TEXT.__swift_as_entry: 0x24
+  __TEXT.__swift_as_ret: 0x40
+  __TEXT.__swift5_capture: 0x30
+  __TEXT.__objc_methtype: 0xf
   __TEXT.__swift5_reflstr: 0x2d
-  __TEXT.__unwind_info: 0x4e8
-  __TEXT.__eh_frame: 0xda0
-  __DATA_CONST.__auth_got: 0x7d0
+  __TEXT.__objc_methname: 0x9e
+  __TEXT.__unwind_info: 0x4c0
+  __TEXT.__eh_frame: 0xd40
+  __DATA_CONST.__auth_got: 0x7e8
   __DATA_CONST.__got: 0x180
-  __DATA_CONST.__auth_ptr: 0x208
-  __DATA_CONST.__const: 0x3a8
+  __DATA_CONST.__auth_ptr: 0x210
+  __DATA_CONST.__const: 0x3b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x48
   __DATA.__data: 0x340
-  __DATA.__common: 0x18
   __DATA.__bss: 0x680
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/TabularData.framework/TabularData

   - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: DED8D935-2161-316A-9039-9874B2540899
-  Functions: 439
-  Symbols:   98
-  CStrings:  41
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 764C6A70-2E79-3641-86D9-99BE4CD30070
+  Functions: 464
+  Symbols:   109
+  CStrings:  42
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftsimd
+ _swift_bridgeObjectRelease_n
+ _swift_willThrowTypedImpl
- _objc_release_x27
- _swift_willThrow
CStrings:
+ "CRITICAL: Asset Information table failed to print due to error: "

```
