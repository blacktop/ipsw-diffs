## com.apple.fskit.apfs

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs`

```diff

-2632.0.15.0.1
-  __TEXT.__text: 0xa6ff4
-  __TEXT.__auth_stubs: 0xe90
+2632.0.36.0.1
+  __TEXT.__text: 0xa7050
+  __TEXT.__auth_stubs: 0xea0
   __TEXT.__objc_stubs: 0x5c0
   __TEXT.__objc_methlist: 0x1ec
   __TEXT.__const: 0x88f0

   __TEXT.__objc_methname: 0x51d
   __TEXT.__objc_methtype: 0x21e
   __TEXT.__unwind_info: 0x1380
-  __DATA_CONST.__auth_got: 0x758
+  __DATA_CONST.__auth_got: 0x760
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x80
   __DATA_CONST.__const: 0xbe8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: E0D4800B-D13F-3992-9447-18702080A360
+  UUID: 0B2F2777-3297-3BE0-B004-B0F87D4E6463
   Functions: 2324
-  Symbols:   1191
+  Symbols:   1192
   CStrings:  3953
 
Symbols:
+ _ccdigest_parallel
Functions:
~ _authapfs_digest : 488 -> 584
~ _fs_obj_create_name_checked : 1804 -> 1800
CStrings:
+ "2632.0.36.0.1"
- "2632.0.15.0.1"

```
