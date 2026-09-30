## appleidsetupd

> `/usr/libexec/appleidsetupd`

```diff

-50.233.0.0.0
-  __TEXT.__text: 0xdb0
-  __TEXT.__auth_stubs: 0x250
+50.463.0.0.0
+  __TEXT.__text: 0xee8
+  __TEXT.__auth_stubs: 0x230
   __TEXT.__const: 0x4a
   __TEXT.__swift5_typeref: 0x27
   __TEXT.__swift5_capture: 0x20
   __TEXT.__objc_methname: 0x13
   __TEXT.__swift5_entry: 0x8
   __TEXT.__oslogstring: 0x1b
-  __TEXT.__unwind_info: 0xa0
-  __TEXT.__eh_frame: 0xb8
-  __DATA_CONST.__auth_got: 0x128
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__unwind_info: 0xa8
+  __TEXT.__eh_frame: 0xc0
+  __DATA_CONST.__auth_got: 0x118
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x140

   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/PrivateFrameworks/AOSUI.framework/Versions/A/AOSUI
   - /System/Library/PrivateFrameworks/AppleIDSetup.framework/Versions/A/AppleIDSetup
   - /System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/Versions/A/AppleIDSetupDaemon
   - /usr/appleinternal/lib/liblinkguard.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 43A8A11E-1CF2-3AEB-97C5-D32AF397A4D4
-  Functions: 17
-  Symbols:   74
+  UUID: C6A09788-BF9A-3A5B-AFE8-5592D9C6B8FF
+  Functions: 18
+  Symbols:   72
   CStrings:  3
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftDataDetection
- _$sSw10copyMemory4fromySW_tF
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_arrayDestroy

```
