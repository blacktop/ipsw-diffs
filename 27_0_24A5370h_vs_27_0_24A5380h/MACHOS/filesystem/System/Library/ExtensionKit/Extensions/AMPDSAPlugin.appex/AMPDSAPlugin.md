## AMPDSAPlugin

> `/System/Library/ExtensionKit/Extensions/AMPDSAPlugin.appex/AMPDSAPlugin`

```diff

-  __TEXT.__text: 0xb518
-  __TEXT.__auth_stubs: 0xbc0
+  __TEXT.__text: 0xae48
+  __TEXT.__auth_stubs: 0xb30
   __TEXT.__objc_stubs: 0x40
-  __TEXT.__const: 0x932
-  __TEXT.__constg_swiftt: 0x120
-  __TEXT.__swift5_typeref: 0x238
-  __TEXT.__swift5_reflstr: 0x220
-  __TEXT.__swift5_fieldmd: 0x1b8
+  __TEXT.__const: 0x918
+  __TEXT.__constg_swiftt: 0x114
+  __TEXT.__swift5_typeref: 0x232
+  __TEXT.__swift5_reflstr: 0x215
+  __TEXT.__swift5_fieldmd: 0x1ac
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x20
   __TEXT.__cstring: 0x231
-  __TEXT.__oslogstring: 0x535
+  __TEXT.__oslogstring: 0x505
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_methtype: 0x15
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x34
-  __TEXT.__swift_as_cont: 0x40
+  __TEXT.__swift_as_cont: 0x30
   __TEXT.__objc_classname: 0x28
-  __TEXT.__objc_methname: 0x51
+  __TEXT.__objc_methname: 0x46
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x338
-  __TEXT.__eh_frame: 0x640
-  __DATA_CONST.__const: 0x5d8
+  __TEXT.__unwind_info: 0x328
+  __TEXT.__eh_frame: 0x650
+  __DATA_CONST.__const: 0x618
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x5e8
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__auth_ptr: 0x218
-  __DATA.__objc_const: 0x90
+  __DATA_CONST.__auth_got: 0x5a0
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__auth_ptr: 0x210
+  __DATA.__objc_const: 0xb8
   __DATA.__objc_selrefs: 0x10
-  __DATA.__objc_data: 0x50
-  __DATA.__data: 0x278
+  __DATA.__data: 0x260
   __DATA.__bss: 0xd80
-  __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground
   - /System/Library/PrivateFrameworks/Morpheus.framework/Morpheus
   - /System/Library/PrivateFrameworks/MorpheusExtensions.framework/MorpheusExtensions
   - /System/Library/PrivateFrameworks/PriMLCore.framework/PriMLCore
-  - /System/Library/PrivateFrameworks/PriMLDataPolicy.framework/PriMLDataPolicy
   - /System/Library/PrivateFrameworks/PriMLFoundation.framework/PriMLFoundation
   - /System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning
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
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 216
-  Symbols:   114
-  CStrings:  52
+  Functions: 210
+  Symbols:   120
+  CStrings:  50
 
Sections:
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_capture : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA.__objc_selrefs : content changed
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftUIKit
+ _swift_release_x27
- _objc_release_x23
- _swift_getSingletonMetadata
- _swift_updateClassMetadata2
CStrings:
- "Using synthetic taskId for Local_Directory: %s"
- "taskSource"

```
