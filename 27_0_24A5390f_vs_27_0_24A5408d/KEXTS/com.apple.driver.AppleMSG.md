## com.apple.driver.AppleMSG

> `com.apple.driver.AppleMSG`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-420.0.1.0.0
+420.0.2.0.0
   __TEXT.__const: 0x362
-  __TEXT.__os_log: 0x11b64
-  __TEXT.__cstring: 0x694f
-  __TEXT_EXEC.__text: 0x39e6c
+  __TEXT.__os_log: 0x11b18
+  __TEXT.__cstring: 0x68fa
+  __TEXT_EXEC.__text: 0x39dd4
   __TEXT_EXEC.__auth_stubs: 0x720
   __DATA.__data: 0xd0
   __DATA.__common: 0x250
-  __DATA.__bss: 0x5f0
+  __DATA.__bss: 0x5e8
   __DATA_CONST.__mod_init_func: 0x50
   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x44d8

   __DATA_CONST.__kalloc_var: 0x5a0
   __DATA_CONST.__auth_got: 0x390
   __DATA_CONST.__got: 0xb0
-  Functions: 1772
+  Functions: 1770
   Symbols:   0
-  CStrings:  1013
+  CStrings:  1011
 
CStrings:
+ "\"_msgDriver reference is NULL!\" @%s:%d"
+ "21:51:44"
+ "Aug  5 2026"
+ "_msgDriver != nullptr"
- "\"msgService reference is NULL!\" @%s:%d"
- "\"msgService->_msgDriver reference is NULL!\" @%s:%d"
- "21:20:48"
- "Jul 14 2026"
- "msgService != nullptr"
- "msgService->_msgDriver != nullptr"
```
