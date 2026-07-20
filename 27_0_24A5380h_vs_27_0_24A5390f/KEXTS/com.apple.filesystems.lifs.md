## com.apple.filesystems.lifs

> `com.apple.filesystems.lifs`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-974.0.7.0.0
-  __TEXT.__os_log: 0x1eba
-  __TEXT.__cstring: 0x29e6
+974.0.11.0.0
+  __TEXT.__os_log: 0x1f16
+  __TEXT.__cstring: 0x29fa
   __TEXT.__const: 0x338
-  __TEXT_EXEC.__text: 0x20244
+  __TEXT_EXEC.__text: 0x20390
   __TEXT_EXEC.__auth_stubs: 0xfb0
   __DATA.__data: 0x578
   __DATA.__common: 0x138

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 460
   Symbols:   0
-  CStrings:  517
+  CStrings:  519
 
Functions:
~ _lifs_vnop_getattrlistbulk : 1300 -> 1380
~ _lifs_getfsattr_call : 360 -> 384
~ _lifs_mntfromname : 484 -> 496
~ sub_fffffe000aacb28c -> sub_fffffe000aae9c50 : 792 -> 848
~ sub_fffffe000aacb6a4 -> sub_fffffe000aaea0a0 : 752 -> 912
CStrings:
+ "%s: Got LIFS_DIRCACHE_LIMIT_REACHED with offset > 0, but no matching cookie entry was found"
+ "lifs_readdir_cached"
```
