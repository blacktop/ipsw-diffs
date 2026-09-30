## livefiles_exfat.dylib

> `/System/Library/Filesystems/exfat.fs/Contents/Resources/livefiles_exfat.dylib`

```diff

-463.60.8.0.0
-  __TEXT.__text: 0x1b6b8
+488.100.10.0.0
+  __TEXT.__text: 0x1c3e4
   __TEXT.__auth_stubs: 0x420
-  __TEXT.__const: 0x4b48
-  __TEXT.__oslogstring: 0x48bc
-  __TEXT.__cstring: 0x6a3
-  __TEXT.__unwind_info: 0x248
+  __TEXT.__const: 0x4b50
+  __TEXT.__oslogstring: 0x486c
+  __TEXT.__cstring: 0x6be
+  __TEXT.__unwind_info: 0x240
   __TEXT.__objc_methname: 0x137
   __TEXT.__objc_stubs: 0x100
   __DATA_CONST.__got: 0x18

   - /System/Library/PrivateFrameworks/LiveFS.framework/Versions/A/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 845B5646-2CEC-3763-B9E6-CED2ADFA3411
-  Functions: 175
-  Symbols:   279
-  CStrings:  441
+  UUID: A9476869-48B3-3E76-B18B-A5D6BB983894
+  Functions: 177
+  Symbols:   281
+  CStrings:  443
 
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
