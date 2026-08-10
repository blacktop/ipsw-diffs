## IOMFB_FDR_Loader

> `/usr/bin/IOMFB_FDR_Loader`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__common`
- `__DATA.__bss`

```diff

-700.50.85.0.0
-  __TEXT.__text: 0x34878
+700.50.96.5.0
+  __TEXT.__text: 0x34890
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__gcc_except_tab: 0x3d4
+  __TEXT.__gcc_except_tab: 0x3e0
   __TEXT.__const: 0x1c00
-  __TEXT.__cstring: 0x8ec9
+  __TEXT.__cstring: 0x8f1e
   __TEXT.__unwind_info: 0x5e8
   __DATA_CONST.__const: 0x2820
   __DATA_CONST.__cfstring: 0x480

   - /usr/lib/libc++.1.dylib
   Functions: 531
   Symbols:   145
-  CStrings:  1064
+  CStrings:  1066
 
Functions:
~ sub_10000efac : 2276 -> 2308
~ sub_100024e78 -> sub_100024e98 : 276 -> 268
CStrings:
+ "Parser e: cannot allocate IOMFBACSSConfig"
+ "Parser e: cannot allocate IOMFBACSSConfig\n"
```
