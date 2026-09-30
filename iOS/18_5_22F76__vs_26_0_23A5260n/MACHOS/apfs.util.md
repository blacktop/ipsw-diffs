## apfs.util

> `/System/Library/Filesystems/apfs.fs/apfs.util`

```diff

-2332.120.31.0.2
-  __TEXT.__text: 0x2c2c
-  __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__cstring: 0x1bf5
+2632.0.15.0.1
+  __TEXT.__text: 0x2c94
+  __TEXT.__auth_stubs: 0x330
+  __TEXT.__cstring: 0x1c29
   __TEXT.__const: 0x40
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0x178
+  __TEXT.__unwind_info: 0x90
+  __DATA_CONST.__auth_got: 0x198
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__cfstring: 0x20

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 0ECAF2D3-73D3-33E8-9F15-862A17E6A5C9
+  UUID: 7ADBD896-3B73-3328-B9E7-0153F47D7580
   Functions: 21
-  Symbols:   56
-  CStrings:  180
+  Symbols:   60
+  CStrings:  181
 
Symbols:
+ _close
+ _ffsctl
+ _open
+ _warnx
Functions:
~ sub_1000027b4 : 136 -> 240
CStrings:
+ "Opening file %s for single file purge failed: %s (%d)"
+ "Purging the single file %s failed: %s (%d)"
- "Purging the single file %s returned %d (%s)\n"

```
