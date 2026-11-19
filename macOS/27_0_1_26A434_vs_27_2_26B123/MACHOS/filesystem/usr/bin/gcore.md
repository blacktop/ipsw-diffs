## gcore

> `/usr/bin/gcore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`

```diff

-1071.0.1.0.0
-  __TEXT.__text: 0xd40c
-  __TEXT.__auth_stubs: 0x840
+1071.40.9.0.0
+  __TEXT.__text: 0xd414
+  __TEXT.__auth_stubs: 0x850
   __TEXT.__const: 0xd9
   __TEXT.__cstring: 0x2b7e
   __TEXT.__oslogstring: 0xaa4
   __TEXT.__unwind_info: 0x5d0
   __DATA_CONST.__const: 0x428
-  __DATA_CONST.__auth_got: 0x420
+  __DATA_CONST.__auth_got: 0x428
   __DATA_CONST.__got: 0x60
   __DATA.__data: 0x48
   __DATA.__bss: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
   Functions: 360
-  Symbols:   147
+  Symbols:   148
   CStrings:  567
 
Symbols:
+ _geteuid
Functions:
~ sub_1000084bc : 4788 -> 4796
```
