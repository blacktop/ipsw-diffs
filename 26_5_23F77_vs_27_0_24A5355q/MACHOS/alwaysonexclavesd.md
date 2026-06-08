## alwaysonexclavesd

> `/usr/libexec/alwaysonexclavesd`

```diff

-40.100.10.0.0
-  __TEXT.__text: 0x70
-  __TEXT.__auth_stubs: 0x50
-  __TEXT.__const: 0x52
-  __TEXT.__cstring: 0x3b
+60.0.0.0.1
+  __TEXT.__text: 0x164
+  __TEXT.__auth_stubs: 0x80
+  __TEXT.__const: 0x5a
+  __TEXT.__cstring: 0xa8
+  __TEXT.__swift5_typeref: 0x8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0x28
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x40
+  __DATA_CONST.__got: 0x10
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__data: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AlwaysOnExclavesDaemon.framework/AlwaysOnExclavesDaemon
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 49AFE876-061D-3CC3-88D9-6527D4FB0053
-  Functions: 1
-  Symbols:   15
-  CStrings:  2
+  UUID: 21EBFF42-AA43-3779-B6F0-83361AF35ADD
+  Functions: 2
+  Symbols:   21
+  CStrings:  5
 
Symbols:
+ _$s22AlwaysOnExclavesDaemon0D0C5start5label12mach_serviceySS_SStKFZ
+ _$sSS6appendyySSF
+ _$ss11_StringGutsV4growyySiF
+ _$ss15_print_unlockedyyx_q_zts16TextOutputStreamR_r0_lF
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_SSAHSus6UInt32VtF
+ _$ss26DefaultStringInterpolationVN
+ _$ss26DefaultStringInterpolationVs16TextOutputStreamsWP
+ _$ss5ErrorMp
+ _swift_getTypeByMangledNameInContext2
- _$s22AlwaysOnExclavesDaemon0D0C5label12mach_serviceACSS_SStcfc
- _$s22AlwaysOnExclavesDaemon0D0C5startyyFTj
- _swift_allocObject
CStrings:
+ " could not start AlwaysOnExclavesDaemon"
+ "Fatal error"
+ "alwaysonexclavesd/alwaysonexclavesd.swift"

```
