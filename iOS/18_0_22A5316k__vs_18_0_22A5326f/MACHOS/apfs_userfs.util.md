## apfs_userfs.util

> `/System/Library/Filesystems/apfs_userfs.fs/apfs_userfs.util`

```diff

-2311.0.0.0.3
-  __TEXT.__text: 0x4f4
-  __TEXT.__auth_stubs: 0x120
-  __TEXT.__cstring: 0x285
+2313.0.4.0.7
+  __TEXT.__text: 0x720
+  __TEXT.__auth_stubs: 0x190
+  __TEXT.__cstring: 0x307
   __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0x90
+  __DATA_CONST.__auth_got: 0xc8
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__cfstring: 0xa0
-  __DATA.__common: 0x8
+  __DATA_CONST.__cfstring: 0xc0
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  Functions: 2
-  Symbols:   26
-  CStrings:  27
+  Functions: 4
+  Symbols:   33
+  CStrings:  32
 
Symbols:
+ ___error
+ _close
+ _free
+ _malloc_type_malloc
+ _open
+ _pread
+ _snprintf
CStrings:
+ "%!s(MISSING): failed to allocate memory"
+ "%!s(MISSING): failed to open device %!s(MISSING) with error %!d(MISSING)"
+ "%!s(MISSING): failed to read from %!s(MISSING) with error %!d(MISSING) \n"
+ "/dev/%!s(MISSING)"
+ "Whole"

```
