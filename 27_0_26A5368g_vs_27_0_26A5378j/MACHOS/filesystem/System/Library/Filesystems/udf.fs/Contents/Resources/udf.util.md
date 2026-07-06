## udf.util

> `/System/Library/Filesystems/udf.fs/Contents/Resources/udf.util`

```diff

-  __TEXT.__text: 0xa124
+  __TEXT.__text: 0xa128
   __TEXT.__auth_stubs: 0x380
-  __TEXT.__cstring: 0xf78
+  __TEXT.__cstring: 0xfa6
   __TEXT.__gcc_except_tab: 0x328
   __TEXT.__const: 0x564
   __TEXT.__unwind_info: 0x3f0

   - /usr/lib/libc++.1.dylib
   Functions: 255
   Symbols:   70
-  CStrings:  147
+  CStrings:  148
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100001258 : 264 -> 288
~ sub_100002b74 -> sub_100002b8c : 88 -> 84
~ sub_100002c3c -> sub_100002c50 : 108 -> 104
~ sub_100003aa0 -> sub_100003ab0 : 200 -> 196
~ sub_100003b68 -> sub_100003b74 : 272 -> 268
~ sub_100003cc8 -> sub_100003cd0 : 380 -> 376
CStrings:
+ "FE/EFE (%u, %u) L_EA+L_AD exceeds sector size"

```
