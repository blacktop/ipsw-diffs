## HealthCycleTrackingWidgetExtension

> `/private/var/staged_system_apps/Health.app/PlugIns/HealthCycleTrackingWidgetExtension.appex/HealthCycleTrackingWidgetExtension`

```diff

-5200.5.1.0.0
+6074.1.2.4.0
   __TEXT.__text: 0x248
   __TEXT.__auth_stubs: 0x70
   __TEXT.__swift5_entry: 0x8

   __DATA_CONST.__auth_got: 0x38
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x48
-  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x10
   __DATA.__bss: 0x80
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
   - /System/Library/PrivateFrameworks/HealthMenstrualCyclesWidgetUI.framework/HealthMenstrualCyclesWidgetUI
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: CA5847FE-C5C1-3CA7-9D02-4A8AC0273D00
+  UUID: 76ABF328-092C-3D6A-9BD8-8985285DAAAD
   Functions: 8
-  Symbols:   35
+  Symbols:   32
   CStrings:  0
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd

```
