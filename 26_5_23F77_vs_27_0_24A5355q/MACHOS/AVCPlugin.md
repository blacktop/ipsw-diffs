## AVCPlugin

> `/System/Library/ExtensionKit/Extensions/AVCPlugin.appex/AVCPlugin`

```diff

-101.0.0.0.0
-  __TEXT.__text: 0x10a9c
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_stubs: 0x1c0
-  __TEXT.__const: 0xe00
-  __TEXT.__objc_classname: 0x20
-  __TEXT.__objc_methname: 0x160
+26.0.0.0.0
+  __TEXT.__text: 0x15818
+  __TEXT.__auth_stubs: 0x1130
+  __TEXT.__objc_stubs: 0x1e0
+  __TEXT.__const: 0xe38
+  __TEXT.__objc_classname: 0x41
+  __TEXT.__objc_methname: 0x17b
   __TEXT.__objc_methtype: 0x1
-  __TEXT.__constg_swiftt: 0x23c
-  __TEXT.__swift5_typeref: 0x33e
-  __TEXT.__swift5_reflstr: 0x3e7
-  __TEXT.__swift5_fieldmd: 0x3f8
-  __TEXT.__oslogstring: 0x101
-  __TEXT.__cstring: 0x2dd
-  __TEXT.__swift5_capture: 0x20
-  __TEXT.__swift5_proto: 0xc4
+  __TEXT.__constg_swiftt: 0x268
+  __TEXT.__swift5_typeref: 0x36a
+  __TEXT.__swift5_reflstr: 0x405
+  __TEXT.__swift5_fieldmd: 0x3d4
+  __TEXT.__oslogstring: 0x196
+  __TEXT.__cstring: 0x2bd
+  __TEXT.__swift5_capture: 0x40
+  __TEXT.__swift5_proto: 0xb8
   __TEXT.__swift5_types: 0x38
-  __TEXT.__swift_as_entry: 0x44
-  __TEXT.__swift_as_ret: 0x4c
-  __TEXT.__swift5_assocty: 0x90
+  __TEXT.__swift_as_entry: 0x64
+  __TEXT.__swift_as_ret: 0x6c
+  __TEXT.__swift_as_cont: 0x80
+  __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x500
-  __TEXT.__eh_frame: 0xbe0
-  __DATA_CONST.__auth_got: 0x668
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__auth_ptr: 0x2a0
-  __DATA_CONST.__const: 0xa00
-  __DATA_CONST.__objc_classlist: 0x8
+  __TEXT.__unwind_info: 0x5f0
+  __TEXT.__eh_frame: 0xeb8
+  __DATA_CONST.__const: 0x960
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xd8
-  __DATA.__objc_selrefs: 0x70
-  __DATA.__data: 0x510
-  __DATA.__bss: 0x1880
-  __DATA.__common: 0x38
+  __DATA_CONST.__auth_got: 0x8a0
+  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__auth_ptr: 0x308
+  __DATA.__objc_const: 0x168
+  __DATA.__objc_selrefs: 0x78
+  __DATA.__objc_data: 0x50
+  __DATA.__data: 0x610
+  __DATA.__bss: 0x1700
+  __DATA.__common: 0x40
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CallHistory.framework/CallHistory
   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground
   - /System/Library/PrivateFrameworks/Morpheus.framework/Morpheus
   - /System/Library/PrivateFrameworks/MorpheusExtensions.framework/MorpheusExtensions
+  - /System/Library/PrivateFrameworks/PriMLCore.framework/PriMLCore
+  - /System/Library/PrivateFrameworks/PriMLDataPolicy.framework/PriMLDataPolicy
+  - /System/Library/PrivateFrameworks/PriMLFoundation.framework/PriMLFoundation
   - /System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning
   - /System/Library/PrivateFrameworks/SwiftSQLite.framework/SwiftSQLite
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 02F3F3DA-B5DF-36C5-86A4-DB1B8E7517FA
-  Functions: 345
-  Symbols:   117
-  CStrings:  46
+  UUID: 890E470A-FBC5-35A4-ADD2-C62C31817545
+  Functions: 388
+  Symbols:   132
+  CStrings:  49
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ _objc_release_x25
+ _swift_allocBox
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x25
+ _swift_updateClassMetadata2
- __swift_FORCE_LOAD_$_swiftCoreMedia
- _objc_release_x21
- _objc_release_x27
- _objc_release_x28
- _swift_retain
CStrings:
+ "Failed to decode AVCCustomTaskParameters from PluginPreference: %@"
+ "Running Legacy plugin"
+ "Running unified plugin"
+ "_TtC9AVCPlugin16AVCUnifiedRunner"
+ "com.apple.priml.PFLPluginReach"
+ "standardUserDefaults"
+ "taskRecord"
- "current_pfl_task"
- "download"
- "morpheus.globals"
- "train"

```
