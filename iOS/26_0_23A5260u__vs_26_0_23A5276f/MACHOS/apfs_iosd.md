## apfs_iosd

> `/System/Library/Filesystems/apfs.fs/apfs_iosd`

```diff

-2632.0.15.0.1
-  __TEXT.__text: 0x39c14
-  __TEXT.__auth_stubs: 0xcb0
+2632.0.36.0.1
+  __TEXT.__text: 0x39c60
+  __TEXT.__auth_stubs: 0xcc0
   __TEXT.__const: 0x3c0
   __TEXT.__oslogstring: 0x1e12
   __TEXT.__cstring: 0x74f9
   __TEXT.__unwind_info: 0x6e8
-  __DATA_CONST.__auth_got: 0x658
+  __DATA_CONST.__auth_got: 0x660
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x30
   __DATA_CONST.__const: 0x758

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: 4C40D1ED-527A-33C6-BEF1-240BB6245E91
+  UUID: 5C96D922-1934-3311-BE2C-53993773934A
   Functions: 640
-  Symbols:   232
+  Symbols:   233
   CStrings:  1093
 
Symbols:
+ _ccdigest_parallel
Functions:
~ sub_100004e6c : 2584 -> 2572
~ sub_10000a36c -> sub_10000a360 : 484 -> 580
~ sub_10001aedc -> sub_10001af30 : 500 -> 496
~ sub_100038e3c -> sub_100038e8c : 136 -> 132

```
