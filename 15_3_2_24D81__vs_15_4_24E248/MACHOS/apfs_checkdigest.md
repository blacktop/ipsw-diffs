## apfs_checkdigest

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_checkdigest`

```diff

-2317.81.2.0.0
-  __TEXT.__text: 0xaa8
-  __TEXT.__auth_stubs: 0x1d0
+2332.101.1.0.0
+  __TEXT.__text: 0xd28
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
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/Versions/A/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
-  UUID: 1DD927AF-13B4-3561-A7D8-CEF8C4A4EE01
+  UUID: C22EB75A-EC7A-3B40-8C73-F6851984A612
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
Functions:
~ sub_100002cf0 -> sub_1000006f0 : 1936 -> 1980
~ sub_1000034b8 -> sub_100000ee4 : 148 -> 212
~ sub_10000354c -> sub_100000fb8 : 68 -> 484
~ sub_100003590 -> sub_10000119c : 32 -> 148

```
