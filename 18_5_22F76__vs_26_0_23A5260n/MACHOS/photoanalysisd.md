## photoanalysisd

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd`

```diff

-760.6.150.0.0
-  __TEXT.__text: 0x2048
-  __TEXT.__auth_stubs: 0x480
+800.14.111.0.0
+  __TEXT.__text: 0x204c
+  __TEXT.__auth_stubs: 0x470
   __TEXT.__objc_stubs: 0xc0
   __TEXT.__objc_methlist: 0x1c8
   __TEXT.__objc_methname: 0x22f
   __TEXT.__swift5_typeref: 0x7e
   __TEXT.__cstring: 0x117
-  __TEXT.__const: 0x50
+  __TEXT.__const: 0x90
   __TEXT.__constg_swiftt: 0xc0
   __TEXT.__swift5_reflstr: 0x19
   __TEXT.__swift5_fieldmd: 0x44

   __TEXT.__oslogstring: 0x5a
   __TEXT.__unwind_info: 0x158
   __TEXT.__eh_frame: 0x170
-  __DATA_CONST.__auth_got: 0x248
+  __DATA_CONST.__auth_got: 0x240
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x238
+  __DATA_CONST.__const: 0x210
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30

   __DATA.__objc_const: 0x250
   __DATA.__objc_selrefs: 0x108
   __DATA.__objc_data: 0x1c0
-  __DATA.__data: 0x200
+  __DATA.__data: 0x1c0
   __DATA.__bss: 0x10
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis
   - /System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
-  - /usr/lib/swift/libswiftMapKit.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVideoToolbox.dylib
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
-  UUID: D27C9CFD-A1B2-3176-9E40-CF48DB285D40
+  UUID: F0C95C60-F61D-383A-8DBA-908EF99B386B
   Functions: 66
-  Symbols:   132
+  Symbols:   126
   CStrings:  76
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftMapKit
- __swift_FORCE_LOAD_$_swiftUIKit
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x9
Functions:
~ sub_100001b58 -> sub_100001a20 : 176 -> 184
~ sub_100002f5c -> sub_100002e2c : 80 -> 76

```
