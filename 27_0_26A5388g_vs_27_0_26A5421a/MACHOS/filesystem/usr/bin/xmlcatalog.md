## xmlcatalog

> `/usr/bin/xmlcatalog`

```diff

-39.10.3.0.0
-  __TEXT.__text: 0x11b4
+40.1.0.0.0
+  __TEXT.__text: 0x1368
   __TEXT.__auth_stubs: 0x260
-  __TEXT.__cstring: 0x742
-  __TEXT.__unwind_info: 0x58
+  __TEXT.__cstring: 0x768
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0x130
   __DATA_CONST.__got: 0x20
   __DATA.__bss: 0x30
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1
+  Functions: 3
   Symbols:   44
-  CStrings:  56
+  CStrings:  59
 
Functions:
~ sub_100000570 : 4532 -> 4680
CStrings:
+ "Invalid arg %s\n"
+ "Invalid command %s\n"
+ "Missing arguments for %s\n"
+ "Too much arguments"
- "No catalog entry specified to remove from\n"
```
