## apfs_checkdigest

> `/System/Library/Filesystems/apfs.fs/apfs_checkdigest`

```diff

-2632.0.15.0.1
-  __TEXT.__text: 0xd78
-  __TEXT.__auth_stubs: 0x240
+2632.0.36.0.1
+  __TEXT.__text: 0xdd8
+  __TEXT.__auth_stubs: 0x250
   __TEXT.__const: 0x28
   __TEXT.__cstring: 0x60f
   __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0x120
+  __DATA_CONST.__auth_got: 0x128
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x20

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
-  UUID: CED95387-7172-3C67-A0B3-4E8F865661C8
+  UUID: 7B9FF43C-6BE3-34C7-AE8E-42F3F86EA082
   Functions: 8
-  Symbols:   43
+  Symbols:   44
   CStrings:  28
 
Symbols:
+ _ccdigest_parallel
Functions:
~ sub_100000fac : 484 -> 580

```
