## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

 737.160.1.0.2
-  __TEXT.__os_log: 0x1385
+  __TEXT.__os_log: 0x13cc
   __TEXT.__cstring: 0x21a0
   __TEXT.__const: 0x2c0
-  __TEXT_EXEC.__text: 0x1ace0
+  __TEXT_EXEC.__text: 0x1ad18
   __TEXT_EXEC.__auth_stubs: 0xf60
   __DATA.__data: 0x528
   __DATA.__common: 0x130

   __DATA_CONST.__kalloc_var: 0xf0
   Functions: 402
   Symbols:   1120
-  CStrings:  398
+  CStrings:  399
 
Functions:
~ _lifs_request_done : 572 -> 628
CStrings:
+ "%s: we got no buffer to copyin, but requested to copyin, returning EIO"
```
