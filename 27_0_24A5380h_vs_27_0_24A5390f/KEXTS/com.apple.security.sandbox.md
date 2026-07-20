## com.apple.security.sandbox

> `com.apple.security.sandbox`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__got`

```diff

-3051.0.30.0.0
-  __TEXT.__os_log: 0x1d58
-  __TEXT.__const: 0x1ed021
-  __TEXT.__cstring: 0x6f50
-  __TEXT_EXEC.__text: 0x38ee0
-  __TEXT_EXEC.__auth_stubs: 0x1090
+3051.0.42.0.2
+  __TEXT.__os_log: 0x1d7e
+  __TEXT.__const: 0x1ee609
+  __TEXT.__cstring: 0x6f21
+  __TEXT_EXEC.__text: 0x38ef0
+  __TEXT_EXEC.__auth_stubs: 0x1080
   __DATA.__data: 0x220
-  __DATA.__bss: 0x15300
+  __DATA.__bss: 0x152fc
   __DATA_CONST.__const: 0x3928
   __DATA_CONST.__kalloc_type: 0xc00
   __DATA_CONST.__kalloc_var: 0x550
-  __DATA_CONST.__auth_got: 0x848
+  __DATA_CONST.__auth_got: 0x840
   __DATA_CONST.__got: 0xc0
-  Functions: 659
+  Functions: 658
   Symbols:   0
   CStrings:  1309
 
CStrings:
+ "mask size (%zu) exceeds maximum (%zu)"
- "\"mask size (%zu) exceeds maximum (%zu)\" @%s:%d"
```
