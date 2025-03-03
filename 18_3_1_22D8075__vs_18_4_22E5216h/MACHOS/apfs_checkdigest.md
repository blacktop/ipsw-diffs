## apfs_checkdigest

> `/System/Library/Filesystems/apfs.fs/apfs_checkdigest`

```diff

-2317.82.1.0.0
-  __TEXT.__text: 0xab8
-  __TEXT.__auth_stubs: 0x1d0
+2332.100.75.502.1
+  __TEXT.__text: 0xd48
+  __TEXT.__auth_stubs: 0x240
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x60f
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0xe8
+  __TEXT.__unwind_info: 0x80
+  __DATA_CONST.__auth_got: 0x120
   __DATA_CONST.__got: 0x20
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
   Functions: 7
-  Symbols:   35
+  Symbols:   43
   CStrings:  28
 
Symbols:
+ ___chkstk_darwin
+ _cc_clear
+ _ccdigest_init
+ _ccdigest_update
+ _ccsha3_256_di
+ _ccsha3_384_di
+ _ccsha3_512_di
+ _memset

```
