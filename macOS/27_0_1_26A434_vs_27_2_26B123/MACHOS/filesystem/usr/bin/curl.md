## curl

> `/usr/bin/curl`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-168.0.2.0.0
-  __TEXT.__text: 0x13a48
+168.40.2.0.0
+  __TEXT.__text: 0x13ab0
   __TEXT.__auth_stubs: 0x890
-  __TEXT.__const: 0x11710
-  __TEXT.__cstring: 0x85a3
+  __TEXT.__const: 0x11718
+  __TEXT.__cstring: 0x85c0
   __TEXT.__unwind_info: 0x328
   __DATA_CONST.__const: 0x45f0
   __DATA_CONST.__auth_got: 0x448

   - /usr/lib/libz.1.dylib
   Functions: 173
   Symbols:   144
-  CStrings:  1591
+  CStrings:  1592
 
Functions:
~ sub_10000fd48 : 1340 -> 1444
CStrings:
+ "APPLE_PKGKIT_ESCALATING_ROOT"
```
