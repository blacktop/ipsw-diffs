## newfs_udf

> `/System/Library/Filesystems/udf.fs/Contents/Resources/newfs_udf`

```diff

-  __TEXT.__text: 0x1224c
+  __TEXT.__text: 0x12250
   __TEXT.__auth_stubs: 0x5c0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x658
   __TEXT.__gcc_except_tab: 0x390
-  __TEXT.__cstring: 0x38c8
+  __TEXT.__cstring: 0x38f6
   __TEXT.__unwind_info: 0x548
   __DATA_CONST.__const: 0x348
   __DATA_CONST.__cfstring: 0x180

   - /usr/lib/libutil.dylib
   Functions: 342
   Symbols:   115
-  CStrings:  340
+  CStrings:  341
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100000c30 : 264 -> 288
~ sub_10000b048 -> sub_10000b060 : 88 -> 84
~ sub_10000b110 -> sub_10000b124 : 108 -> 104
~ sub_10000bf74 -> sub_10000bf84 : 200 -> 196
~ sub_10000c03c -> sub_10000c048 : 272 -> 268
~ sub_10000c19c -> sub_10000c1a4 : 380 -> 376
CStrings:
+ "FE/EFE (%u, %u) L_EA+L_AD exceeds sector size"

```
