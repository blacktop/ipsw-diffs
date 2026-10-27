## ditto

> `/usr/bin/ditto`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-279.2.0.0.0
-  __TEXT.__text: 0x2808
+280.0.0.0.0
+  __TEXT.__text: 0x282c
   __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__cstring: 0x1f74
+  __TEXT.__cstring: 0x1f7f
   __TEXT.__unwind_info: 0x100
   __DATA_CONST.__cfstring: 0x3c0
   __DATA_CONST.__auth_got: 0x260

   - /usr/lib/libSystem.B.dylib
   Functions: 35
   Symbols:   91
-  CStrings:  159
+  CStrings:  160
 
Functions:
~ sub_100002114 : 284 -> 320
CStrings:
+ "cloned %s\n"
```
