## linkd

> `/usr/libexec/linkd`

```diff

-226.8.0.0.0
-  __TEXT.__text: 0x134ebc
-  __TEXT.__auth_stubs: 0x29d0
+226.9.0.3.0
+  __TEXT.__text: 0x1357dc
+  __TEXT.__auth_stubs: 0x29e0
   __TEXT.__objc_stubs: 0xa0
   __TEXT.__objc_methlist: 0x6c4
   __TEXT.__swift5_entry: 0x8
   __TEXT.__const: 0x501c
-  __TEXT.__cstring: 0x4864
+  __TEXT.__cstring: 0x4874
   __TEXT.__constg_swiftt: 0x2138
   __TEXT.__swift5_typeref: 0x3842
   __TEXT.__swift5_builtin: 0x190
   __TEXT.__swift5_reflstr: 0x1bc5
   __TEXT.__swift5_fieldmd: 0x1e30
   __TEXT.__swift5_assocty: 0x520
-  __TEXT.__objc_methname: 0x3153
-  __TEXT.__oslogstring: 0x33bf
+  __TEXT.__objc_methname: 0x3197
+  __TEXT.__oslogstring: 0x34bf
   __TEXT.__swift5_capture: 0x10b8
   __TEXT.__swift5_proto: 0x4c8
   __TEXT.__swift5_types: 0x24c

   __TEXT.__objc_methtype: 0xdcb
   __TEXT.__swift5_protos: 0x88
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x5410
+  __TEXT.__unwind_info: 0x5418
   __TEXT.__eh_frame: 0xd310
-  __DATA_CONST.__auth_got: 0x14f0
-  __DATA_CONST.__got: 0x980
+  __DATA_CONST.__auth_got: 0x14f8
+  __DATA_CONST.__got: 0x988
   __DATA_CONST.__auth_ptr: 0xba8
   __DATA_CONST.__const: 0x67c0
   __DATA_CONST.__cfstring: 0x20

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA.__objc_const: 0x2e28
-  __DATA.__objc_selrefs: 0xc10
+  __DATA.__objc_selrefs: 0xc20
   __DATA.__objc_data: 0x7e0
-  __DATA.__data: 0x5558
+  __DATA.__data: 0x5548
   __DATA.__common: 0xd48
   __DATA.__bss: 0x68f0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/Koa.framework/Koa
   - /System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata
   - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
+  - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6890
-  Symbols:   1156
-  CStrings:  1276
+  Functions: 6901
+  Symbols:   1158
+  CStrings:  1283
 
Symbols:
+ _MobileInstallationWaitForSystemAppMigrationToComplete
+ _OBJC_CLASS_$_LNAvailabilityChecker
CStrings:
+ "%s AppShortcut is marked as unavailable on current platform, skipping"
+ "%s is marked as unavailable on current platform, skipping"
+ "Error checking app migration %s"
+ "LinkProgrammaticInterface-226.9.0.3"
+ "System app migration completed"
+ "Waiting for system app migration..."
+ "availableForCurrentPlatformVersion"
+ "initWithAvailabilityAnnotations:"
- "LinkProgrammaticInterface-226.8"

```
