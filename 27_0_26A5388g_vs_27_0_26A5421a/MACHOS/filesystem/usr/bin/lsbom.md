## lsbom

> `/usr/bin/lsbom`

### Sections with Same Size but Changed Content

- `__DATA.__data`

```diff

-277.0.0.0.0
-  __TEXT.__text: 0x1038
+279.2.0.0.0
+  __TEXT.__text: 0x10d4
   __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__cstring: 0x7a6
-  __TEXT.__unwind_info: 0x80
+  __TEXT.__cstring: 0x7ee
+  __TEXT.__unwind_info: 0x78
   __DATA_CONST.__auth_got: 0x170
   __DATA_CONST.__got: 0x20
   __DATA.__data: 0x60

   - /usr/lib/libSystem.B.dylib
   Functions: 8
   Symbols:   52
-  CStrings:  47
+  CStrings:  48
 
Functions:
~ sub_1000005e8 : 2728 -> 2800
~ sub_100001154 -> sub_10000119c : 268 -> 352
CStrings:
+ "WARNING! %s tag 0x%08x for \"%s\" is out of range (%u entries); ignoring\n"
```
