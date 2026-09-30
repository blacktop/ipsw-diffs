## HealthStandaloneIntents

> `/System/Library/ExtensionKit/Extensions/HealthStandaloneIntents.appex/HealthStandaloneIntents`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x73f8
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__const: 0x8ba
-  __TEXT.__cstring: 0x7e6
+6074.1.2.4.0
+  __TEXT.__text: 0x85bc
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__const: 0x948
+  __TEXT.__cstring: 0x806
   __TEXT.__swift5_typeref: 0x2b0
   __TEXT.__swift5_reflstr: 0xe4
   __TEXT.__swift5_assocty: 0x118

   __TEXT.__oslogstring: 0x24
   __TEXT.__swift5_proto: 0x80
   __TEXT.__swift5_types: 0x18
-  __TEXT.__swift_as_entry: 0x3c
-  __TEXT.__swift_as_ret: 0x30
+  __TEXT.__swift_as_entry: 0x38
+  __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x310
-  __TEXT.__eh_frame: 0x300
-  __DATA_CONST.__auth_got: 0x408
-  __DATA_CONST.__got: 0x168
-  __DATA_CONST.__auth_ptr: 0x448
-  __DATA_CONST.__const: 0x380
+  __TEXT.__unwind_info: 0x2f8
+  __TEXT.__eh_frame: 0x360
+  __DATA_CONST.__auth_got: 0x420
+  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__auth_ptr: 0x450
+  __DATA_CONST.__const: 0x3e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x28
-  __DATA.__data: 0x280
+  __DATA.__data: 0x208
   __DATA.__common: 0x80
   __DATA.__bss: 0x1008
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

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
-  UUID: CC5531C0-1E6B-3E6F-974E-76E647A85FE2
-  Functions: 212
+  UUID: A3D96EBF-0D7D-3646-8ED0-64C6EF46D9C3
+  Functions: 210
   Symbols:   79
   CStrings:  37
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_release_x23
+ _swift_coroFrameAlloc
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "settings-navigation://com.apple.Settings.Apps/com.apple.Health/"
- "prefs://root=HEALTH&path="

```
