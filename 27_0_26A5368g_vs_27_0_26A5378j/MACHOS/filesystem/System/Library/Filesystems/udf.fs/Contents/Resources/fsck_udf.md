## fsck_udf

> `/System/Library/Filesystems/udf.fs/Contents/Resources/fsck_udf`

```diff

-  __TEXT.__text: 0x10db4
+  __TEXT.__text: 0x10dbc
   __TEXT.__auth_stubs: 0x420
   __TEXT.__init_offsets: 0x8
   __TEXT.__gcc_except_tab: 0x604
-  __TEXT.__cstring: 0x34d0
+  __TEXT.__cstring: 0x34fe
   __TEXT.__const: 0x4f5c
   __TEXT.__unwind_info: 0x538
   __DATA_CONST.__const: 0x348

   - /usr/lib/libc++.1.dylib
   Functions: 366
   Symbols:   84
-  CStrings:  399
+  CStrings:  400
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100001638 : 264 -> 288
~ sub_100003144 -> sub_10000315c : 156 -> 152
~ sub_100003280 -> sub_100003294 : 128 -> 124
~ sub_10000d8f4 -> sub_10000d904 : 480 -> 468
~ sub_10000e2c8 -> sub_10000e2cc : 996 -> 976
~ sub_10000e8f8 -> sub_10000e8e8 : 736 -> 756
~ sub_10000f270 -> sub_10000f274 : 140 -> 148
~ sub_10000f458 -> sub_10000f464 : 476 -> 472
CStrings:
+ "FE/EFE (%u, %u) L_EA+L_AD exceeds sector size"

```
