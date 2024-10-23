## VoiceTriggerCommon

> `/System/ExclaveKit/System/Library/Frameworks/VoiceTriggerCommon.framework/VoiceTriggerCommon`

```diff

-200.54.0.0.0
+220.24.0.0.0
   __TEXT.__text: 0x9bc
   __TEXT.__auth_stubs: 0x140
   __TEXT.__const: 0x116

   __DATA.__auth_got: 0xa0
   __DATA.__got: 0x18
   __DATA.__auth_ptr: 0x60
-  __DATA.__const: 0xb0
+  __DATA.__const: 0xc8
   __DATA.__objc_imageinfo: 0x8
   __DATA.__data: 0x8
   __DATA.__bss: 0x100

   - /System/ExclaveKit/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /System/ExclaveKit/usr/lib/libSystem.dylib
   - /System/ExclaveKit/usr/lib/libobjc.A.dylib
+  - /System/ExclaveKit/usr/lib/swift/libswiftC.dylib
   - /System/ExclaveKit/usr/lib/swift/libswiftCore.dylib
+  - /System/ExclaveKit/usr/lib/swift/libswift_errno.dylib
   - /System/ExclaveKit/usr/lib/swift/libswift_stdio.dylib
+  - /System/ExclaveKit/usr/lib/swift/libswift_time.dylib
   Functions: 32
-  Symbols:   257
+  Symbols:   266
   CStrings:  3
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftC
+ __swift_FORCE_LOAD_$_swiftC_$_VoiceTriggerCommon
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_errno_$_VoiceTriggerCommon
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swift_time_$_VoiceTriggerCommon

```
