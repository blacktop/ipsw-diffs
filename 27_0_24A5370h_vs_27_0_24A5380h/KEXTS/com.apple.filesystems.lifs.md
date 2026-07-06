## com.apple.filesystems.lifs

> `com.apple.filesystems.lifs`

```diff

   __TEXT.__os_log: 0x1eba
   __TEXT.__cstring: 0x29e6
   __TEXT.__const: 0x338
-  __TEXT_EXEC.__text: 0x20214
+  __TEXT_EXEC.__text: 0x20244
   __TEXT_EXEC.__auth_stubs: 0xfb0
   __DATA.__data: 0x578
   __DATA.__common: 0x138
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Functions:
~ _lifs_vnop_readdir : 1740 -> 1764
~ _lifs_vnop_getattrlistbulk : 1292 -> 1300
~ sub_fffffe000aacff4c -> sub_fffffe000aacb28c : 788 -> 792
~ sub_fffffe000aad0360 -> sub_fffffe000aacb6a4 : 740 -> 752

```
