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

-974.0.11.0.0
-  __TEXT.__os_log: 0x1f16
+974.0.13.0.2
+  __TEXT.__os_log: 0x1f5d
   __TEXT.__cstring: 0x29fa
   __TEXT.__const: 0x338
-  __TEXT_EXEC.__text: 0x20390
+  __TEXT_EXEC.__text: 0x203c8
   __TEXT_EXEC.__auth_stubs: 0xfb0
   __DATA.__data: 0x578
   __DATA.__common: 0x138

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 460
   Symbols:   0
-  CStrings:  519
+  CStrings:  520
 
Functions:
~ _lifs_request_done : 572 -> 628
CStrings:
+ "%s: we got no buffer to copyin, but requested to copyin, returning EIO"
```
