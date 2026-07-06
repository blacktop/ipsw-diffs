## FedStatsPluginStatic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginStatic.appex/FedStatsPluginStatic`

```diff

-  __TEXT.__text: 0xd90
-  __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__const: 0x12a
+  __TEXT.__text: 0x98c
+  __TEXT.__auth_stubs: 0x200
+  __TEXT.__const: 0x112
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x28
-  __TEXT.__swift5_typeref: 0x74
+  __TEXT.__swift5_typeref: 0x46
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_reflstr: 0xe
   __TEXT.__swift5_assocty: 0x18

   __TEXT.__swift5_types: 0x4
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__swift_as_cont: 0x4
-  __TEXT.__unwind_info: 0xc0
-  __TEXT.__eh_frame: 0xc8
-  __DATA_CONST.__const: 0xc8
+  __TEXT.__swift_as_cont: 0x8
+  __TEXT.__unwind_info: 0xa8
+  __TEXT.__eh_frame: 0xd0
+  __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xf8
-  __DATA_CONST.__got: 0x38
-  __DATA_CONST.__auth_ptr: 0x68
-  __DATA.__data: 0x28
+  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x20
+  __DATA_CONST.__auth_ptr: 0x60
+  __DATA.__data: 0x10
   __DATA.__bss: 0x100
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /System/Library/PrivateFrameworks/PriMLFoundation.framework/PriMLFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24
+  Functions: 19
   Symbols:   41
   CStrings:  1
 
Sections:
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ _swift_bridgeObjectRelease
+ _swift_release_x21
+ _swift_release_x8
- __swiftEmptyArrayStorage
- __swiftEmptyDictionarySingleton
- _swift_bridgeObjectRetain
- _swift_getTypeByMangledNameInContext2
- _swift_release_x20
- _swift_release_x23
- _swift_retain_x20

```
