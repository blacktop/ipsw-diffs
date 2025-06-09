## PFLHRPeriodPredPush

> `/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredPush.appex/PFLHRPeriodPredPush`

```diff

 67.0.0.0.0
-  __TEXT.__text: 0xd64
+  __TEXT.__text: 0xd60
   __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__const: 0xce
+  __TEXT.__const: 0xf2
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_typeref: 0x5e

   __DATA_CONST.__auth_got: 0xe8
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0xf0
+  __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0x58
+  __DATA.__data: 0x38
   __DATA.__bss: 0x100
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
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
-  UUID: 6566C9AA-DCA7-330C-874D-4A4B3A4FF7F4
+  UUID: D62E3A81-D006-37BD-918B-A5E5434B8E79
   Functions: 23
-  Symbols:   41
+  Symbols:   39
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
Functions:
~ sub_100002148 -> sub_1000020f8 : 80 -> 76

```
