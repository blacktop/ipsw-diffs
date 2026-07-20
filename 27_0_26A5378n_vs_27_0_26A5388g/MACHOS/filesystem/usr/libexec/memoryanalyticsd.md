## memoryanalyticsd

> `/usr/libexec/memoryanalyticsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__data`

```diff

-97.0.0.0.0
-  __TEXT.__text: 0x1a44c
+100.0.0.0.0
+  __TEXT.__text: 0x1a464
   __TEXT.__auth_stubs: 0x920
   __TEXT.__objc_stubs: 0x2900
   __TEXT.__objc_methlist: 0xc8c

   __TEXT.__oslogstring: 0x35ab
   __TEXT.__objc_classname: 0x135
   __TEXT.__objc_methtype: 0x3e8
-  __TEXT.__cstring: 0x3398
+  __TEXT.__cstring: 0x33ae
   __TEXT.__gcc_except_tab: 0x1f4
   __TEXT.__unwind_info: 0x590
   __DATA_CONST.__const: 0xb60
-  __DATA_CONST.__cfstring: 0x34a0
+  __DATA_CONST.__cfstring: 0x34c0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x3c8
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA_CONST.__objc_intobj: 0x840
+  __DATA_CONST.__objc_intobj: 0x858
   __DATA_CONST.__objc_doubleobj: 0x1a0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0x4a0
-  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__got: 0x200
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x17d8
   __DATA.__objc_selrefs: 0xb10

   - /usr/lib/libsqlite3.dylib
   Functions: 551
   Symbols:   220
-  CStrings:  1418
+  CStrings:  1419
 
Functions:
~ sub_100009fa8 : 3648 -> 3672
CStrings:
+ "SetStoreUpdateService"
```
