## IOMFB_FDR_Loader

> `/usr/bin/IOMFB_FDR_Loader`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

-700.50.85.0.0
-  __TEXT.__text: 0x34964
+700.50.97.9.0
+  __TEXT.__text: 0x3497c
   __TEXT.__auth_stubs: 0x700
-  __TEXT.__gcc_except_tab: 0x3dc
+  __TEXT.__gcc_except_tab: 0x3e8
   __TEXT.__const: 0x1c00
-  __TEXT.__cstring: 0x8cf0
+  __TEXT.__cstring: 0x8d45
   __TEXT.__unwind_info: 0x5f0
   __DATA_CONST.__const: 0xde0
   __DATA_CONST.__cfstring: 0x480

   - /usr/lib/libc++.1.dylib
   Functions: 531
   Symbols:   143
-  CStrings:  978
+  CStrings:  980
 
Functions:
~ sub_10000eff8 : 2276 -> 2308
~ sub_100024f24 -> sub_100024f44 : 276 -> 268
CStrings:
+ "Parser e: cannot allocate IOMFBACSSConfig"
+ "Parser e: cannot allocate IOMFBACSSConfig\n"
```
