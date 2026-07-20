## com.apple.driver.AppleProResHW

> `com.apple.driver.AppleProResHW`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-600.38.0.0.0
+600.45.0.0.0
   __TEXT.__const: 0x23a8
-  __TEXT.__os_log: 0x9d00
+  __TEXT.__os_log: 0x9d48
   __TEXT.__cstring: 0x114b
-  __TEXT_EXEC.__text: 0x502e0
+  __TEXT_EXEC.__text: 0x541e8
   __TEXT_EXEC.__auth_stubs: 0x5e0
   __DATA.__data: 0x458
   __DATA.__common: 0x78
   __DATA.__bss: 0x9a20
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0xba28
+  __DATA_CONST.__const: 0xbfe0
   __DATA_CONST.__kalloc_type: 0x480
   __DATA_CONST.__kalloc_var: 0x140
   __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0x60
-  Functions: 2818
+  Functions: 3015
   Symbols:   0
-  CStrings:  563
+  CStrings:  564
 
CStrings:
+ "ERROR AppleProResHW (0x%x): %d: %s(): Could not allocate spare buffer.\n"
```
