## VoiceTriggerSecure

> `/System/ExclaveKit/System/Library/Frameworks/VoiceTriggerSecure.framework/VoiceTriggerSecure`

```diff

-200.54.0.0.0
+220.24.0.0.0
   __TEXT.__text: 0xa48
   __TEXT.__auth_stubs: 0x160
   __TEXT.__cstring: 0x132
   __TEXT.__const: 0xd6
-  __TEXT.__constg_swiftt: 0xe0
+  __TEXT.__constg_swiftt: 0xe8
   __TEXT.__swift5_typeref: 0x5a
   __TEXT.__swift5_fieldmd: 0x64
   __TEXT.__swift5_reflstr: 0x13

   __DATA.__auth_got: 0xb0
   __DATA.__got: 0x20
   __DATA.__auth_ptr: 0x50
-  __DATA.__const: 0x8
+  __DATA.__const: 0x20
   __DATA.__objc_classlist: 0x18
   __DATA.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x220
-  __DATA.__data: 0x1f8
+  __DATA.__data: 0x200
   __DATA.__bss: 0x180
   - /System/ExclaveKit/System/Library/Frameworks/Foundation.framework/Foundation
   - /System/ExclaveKit/System/Library/Frameworks/VoiceTriggerCommon.framework/VoiceTriggerCommon
   - /System/ExclaveKit/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /System/ExclaveKit/usr/lib/libSystem.dylib
   - /System/ExclaveKit/usr/lib/libobjc.A.dylib
+  - /System/ExclaveKit/usr/lib/swift/libswiftC.dylib
   - /System/ExclaveKit/usr/lib/swift/libswiftCore.dylib
+  - /System/ExclaveKit/usr/lib/swift/libswift_errno.dylib
   - /System/ExclaveKit/usr/lib/swift/libswift_stdio.dylib
+  - /System/ExclaveKit/usr/lib/swift/libswift_time.dylib
   Functions: 20
-  Symbols:   242
+  Symbols:   253
   CStrings:  8
 
Symbols:
+ _$s18VoiceTriggerSecureAAC7ServiceC10connectionAD9Tightbeam16ClientConnectionC_tcfCTq
+ __swift_FORCE_LOAD_$_swiftC
+ __swift_FORCE_LOAD_$_swiftC_$_VoiceTriggerSecure
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_errno_$_VoiceTriggerSecure
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swift_time_$_VoiceTriggerSecure

```
