## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__assert`

```diff

   __TEXT.__cstring: 0x4da0d
   __TEXT_EXEC.__text: 0x148e38
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x70c
-  __DATA.__bss: 0xd48
+  __DATA.__data: 0x704
+  __DATA.__bss: 0xd50
   __DATA_CONST.__auth_got: 0x11a0
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x8
CStrings:
+ "14:48:08"
+ "2026/07/11"
+ "Jul 11 2026"
- "2026/07/09"
- "23:19:03"
- "Jul  9 2026"
```
