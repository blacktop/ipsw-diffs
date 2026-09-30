## apfs.util

> `/System/Library/Filesystems/apfs.fs/apfs.util`

```diff

-2317.82.1.0.0
-  __TEXT.__text: 0x2c14
+2332.100.53.0.6
+  __TEXT.__text: 0x2c2c
   __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__cstring: 0x1be6
-  __TEXT.__const: 0x10
-  __TEXT.__unwind_info: 0x90
+  __TEXT.__cstring: 0x1bf5
+  __TEXT.__const: 0x40
+  __TEXT.__unwind_info: 0x88
   __DATA_CONST.__auth_got: 0x178
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x68

   - /usr/lib/libutil.dylib
   Functions: 21
   Symbols:   56
-  CStrings:  178
+  CStrings:  179
 
CStrings:
+ "-fixup"
+ "Failed to mark %s as purgeable, errno: %d (%s) (flags 0x%llx supplemental 0x%llx)\n"
- "Failed to mark %s as purgeable %d (%s) (flags 0x%llx supplemental 0x%llx)\n"

```
