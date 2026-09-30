## RemindersDES

> `/System/Library/DistributedEvaluation/Plugins/RemindersDES.desPlugin/RemindersDES`

```diff

-3799.12.0.0.0
+3806.0.0.0.0
   __TEXT.__text: 0x2950
   __TEXT.__auth_stubs: 0x5f0
   __TEXT.__objc_methlist: 0x184

   __DATA_CONST.__auth_got: 0x2f8
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x98
-  __DATA_CONST.__const: 0x290
+  __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__bss: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/ReminderKit.framework/ReminderKit
   - /System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A36882D0-4EA2-364C-B176-376F1CF9DE43
+  UUID: 20B472D9-1D12-35EB-8F89-5BD4283649D4
   Functions: 62
-  Symbols:   90
+  Symbols:   95
   CStrings:  93
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftUIKit

```
