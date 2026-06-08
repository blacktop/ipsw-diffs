## Siri

> `/System/Library/DataClassMigrators/Siri.migrator/Siri`

```diff

-3525.5.12.11.2
-  __TEXT.__text: 0x3180
-  __TEXT.__auth_stubs: 0x350
+3600.62.21.1.5
+  __TEXT.__text: 0x2edc
+  __TEXT.__auth_stubs: 0x360
   __TEXT.__objc_stubs: 0x8e0
-  __TEXT.__objc_methlist: 0x134
+  __TEXT.__objc_methlist: 0x140
   __TEXT.__const: 0x1c
-  __TEXT.__cstring: 0x69a
-  __TEXT.__oslogstring: 0x502
+  __TEXT.__cstring: 0x717
+  __TEXT.__oslogstring: 0x5de
   __TEXT.__objc_classname: 0xd
-  __TEXT.__objc_methname: 0x711
+  __TEXT.__objc_methname: 0x72f
   __TEXT.__objc_methtype: 0x20
-  __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__auth_got: 0x1b0
-  __DATA_CONST.__got: 0xf0
+  __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__const: 0x10
-  __DATA_CONST.__cfstring: 0x4e0
+  __DATA_CONST.__cfstring: 0x520
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0xf0
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x258
+  __DATA.__objc_selrefs: 0x260
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 99C9040D-BBC7-3E1E-9142-1B3C83E7AB11
-  Functions: 28
-  Symbols:   95
-  CStrings:  207
+  UUID: 6C3C31F6-A788-3ADD-8609-F9B634C23B0F
+  Functions: 29
+  Symbols:   96
+  CStrings:  218
 
Symbols:
+ _AFIsLinwoodFFEnabled
+ ___kCFBooleanTrue
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%s Device is not an internal install. Skipping."
+ "%s Feature is not enabled. Skipping."
+ "%s Marking one-time reset as complete."
+ "%s One-time reset has already been performed. Skipping."
+ "%s Setting opt-in value to unspecified."
+ "-[SiriMigrator _performInternalSiriDataSharingResetIfNeeded]"
+ "InternalSiriDataSharingResetPerformed"
+ "SiriMigratorInternalReset"
+ "_performRaiseToSpeakMigration"

```
