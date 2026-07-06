## mount_udf

> `/System/Library/Filesystems/udf.fs/Contents/Resources/mount_udf`

```diff

-  __TEXT.__text: 0x9ea0
+  __TEXT.__text: 0x9ea4
   __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__cstring: 0x1064
+  __TEXT.__cstring: 0x1092
   __TEXT.__gcc_except_tab: 0x304
   __TEXT.__const: 0x564
   __TEXT.__unwind_info: 0x3d0

   - /usr/lib/libutil.dylib
   Functions: 247
   Symbols:   78
-  CStrings:  160
+  CStrings:  161
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100001250 : 264 -> 288
~ sub_100002b6c -> sub_100002b84 : 88 -> 84
~ sub_100002c34 -> sub_100002c48 : 108 -> 104
~ sub_100003a98 -> sub_100003aa8 : 200 -> 196
~ sub_100003b60 -> sub_100003b6c : 272 -> 268
~ sub_100003cc0 -> sub_100003cc8 : 380 -> 376
CStrings:
+ "FE/EFE (%u, %u) L_EA+L_AD exceeds sector size"

```
