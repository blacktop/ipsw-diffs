## com.apple.filesystems.lifs

> `com.apple.filesystems.lifs`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

   __TEXT.__os_log: 0x1385
   __TEXT.__cstring: 0x21a0
   __TEXT.__const: 0x2c0
-  __TEXT_EXEC.__text: 0x1acbc
+  __TEXT_EXEC.__text: 0x1ace0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x528
   __DATA.__common: 0x130
Functions:
~ _lifs_getfsattr_call : 360 -> 384
~ _lifs_mntfromname : 484 -> 496
```
