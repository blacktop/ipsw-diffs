## tzinit

> `/usr/libexec/tzinit`

```diff

-  __TEXT.__text: 0xfde8
+  __TEXT.__text: 0xfd80
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x726
-  __TEXT.__gcc_except_tab: 0xb80
+  __TEXT.__gcc_except_tab: 0xb7c
   __TEXT.__cstring: 0x561
   __TEXT.__unwind_info: 0x768
   __DATA_CONST.__const: 0x8a8
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
Functions:
~ sub_100002b00 : 176 -> 156
~ sub_10000a688 -> sub_10000a674 : 524 -> 500
~ sub_10000a894 -> sub_10000a868 : 176 -> 152
~ sub_10000a944 -> sub_10000a900 : 228 -> 204
~ sub_10000e460 -> sub_10000e404 : 480 -> 468

```
