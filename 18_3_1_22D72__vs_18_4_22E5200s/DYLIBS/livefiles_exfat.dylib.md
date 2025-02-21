## livefiles_exfat.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_exfat.dylib`

```diff

-463.60.8.0.0
-  __TEXT.__text: 0x1b4c4
+488.100.9.0.0
+  __TEXT.__text: 0x1c1f0
   __TEXT.__auth_stubs: 0x420
-  __TEXT.__const: 0x4b48
-  __TEXT.__oslogstring: 0x48b2
-  __TEXT.__cstring: 0x67e
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__const: 0x4b50
+  __TEXT.__oslogstring: 0x4862
+  __TEXT.__cstring: 0x699
+  __TEXT.__unwind_info: 0x238
   __TEXT.__objc_methname: 0xe2
   __TEXT.__objc_stubs: 0xe0
   __DATA_CONST.__got: 0x18

   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 173
-  Symbols:   256
-  CStrings:  439
+  Functions: 175
+  Symbols:   258
+  CStrings:  441
 
Symbols:
+ _DIROPS_IsDotOrDotDotName
+ _EXFAT_Inactive
CStrings:
+ "%s"
+ "%s: Amount of secondary entries is invalid."
+ "%s: offset: %llu, length: %lu, flags: %u, operationID: %llu.\n"
+ "EXFAT_Inactive"
+ "_N_INACTIVE"
- "%s: offset: %llu, length: %lu, startIO: %d, flags: %u, operationID: %llu.\n"
- "%s: volume label entry is there, but 0 length"
- "DIROPS_GetDirEntryByOffset: Amount of secondary entries is invalid."

```
