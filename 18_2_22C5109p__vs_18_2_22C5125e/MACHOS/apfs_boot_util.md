## apfs_boot_util

> `/System/Library/Filesystems/apfs.fs/apfs_boot_util`

```diff

-2317.60.14.0.2
-  __TEXT.__text: 0x32c8
-  __TEXT.__auth_stubs: 0x570
+2317.60.21.0.1
+  __TEXT.__text: 0x343c
+  __TEXT.__auth_stubs: 0x580
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x13a1
-  __TEXT.__unwind_info: 0xd0
-  __DATA_CONST.__auth_got: 0x2b8
+  __TEXT.__cstring: 0x144f
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__auth_got: 0x2c0
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__cfstring: 0x60

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
   Functions: 32
-  Symbols:   98
-  CStrings:  161
+  Symbols:   99
+  CStrings:  164
 
Symbols:
+ _fsctl
+ _lstat
- _ffsctl
CStrings:
+ "%!s(MISSING):%!d(MISSING): base path %!s(MISSING) doesn't match graft path %!s(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): failed to get ExclaveOS registration base path: %!s(MISSING) (%!d(MISSING))\n"
+ "%!s(MISSING):%!d(MISSING): failed to lstat ExclaveOS registration path: %!s(MISSING) (%!d(MISSING))\n"

```
