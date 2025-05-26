## apfs.util

> `/System/Library/Filesystems/apfs.fs/apfs.util`

```diff

-2236.102.1.0.0
-  __TEXT.__text: 0x286c
+2236.122.2.0.0
+  __TEXT.__text: 0x29ec
   __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__cstring: 0x19d5
+  __TEXT.__cstring: 0x1a8c
   __TEXT.__const: 0x10
   __TEXT.__unwind_info: 0x84
   __DATA_CONST.__auth_got: 0x178

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 20
+  Functions: 21
   Symbols:   56
-  CStrings:  160
+  CStrings:  169
 
CStrings:
+ "-ext"
+ "-purge-reason"
+ "Invalid argument: expected purge reason"
+ "Invalid purge reason specified: %s \n"
+ "foundation-api-discarded"
+ "fp-api-discarded"
+ "ru-discarded"
+ "system-discarded"
+ "user-discarded"

```
