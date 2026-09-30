## libcopyfile.dylib

> `/usr/lib/system/libcopyfile.dylib`

```diff

-  __TEXT.__text: 0x7a18
+  __TEXT.__text: 0x7a88
   __TEXT.__const: 0x1c8
   __TEXT.__cstring: 0x1bf1
   __TEXT.__unwind_info: 0xf8
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
Functions:
~ _nameInDefaultList : 152 -> 160
~ _copyfile_internal : 7668 -> 7744
~ sub_2c06affac -> _copyfile_set_dst_permissions : 72 -> 476
~ sub_2c06afff4 -> _copyfile_validate_dst : 72 -> 284
~ _copyfile_fix_perms -> sub_2c12f42f8 : 216 -> 72
~ _copyfile_set_dst_permissions -> sub_2c12f4340 : 476 -> 72
~ _copyfile_validate_dst -> _copyfile_fix_perms : 284 -> 216
~ _xattr_intent_with_flags : 56 -> 64
~ _xattr_preserve_for_intent : 116 -> 136

```
