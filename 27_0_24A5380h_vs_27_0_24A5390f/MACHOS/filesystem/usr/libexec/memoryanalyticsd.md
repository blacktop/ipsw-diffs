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
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-97.0.0.0.0
-  __TEXT.__text: 0x19554
+100.0.0.0.0
+  __TEXT.__text: 0x1956c
   __TEXT.__auth_stubs: 0xa70
   __TEXT.__objc_stubs: 0x29e0
   __TEXT.__objc_methlist: 0xc7c

   __TEXT.__oslogstring: 0x3662
   __TEXT.__objc_classname: 0x135
   __TEXT.__objc_methtype: 0x3e8
-  __TEXT.__cstring: 0x3478
+  __TEXT.__cstring: 0x348e
   __TEXT.__gcc_except_tab: 0x1f4
   __TEXT.__unwind_info: 0x588
   __DATA_CONST.__const: 0xad8
-  __DATA_CONST.__cfstring: 0x35c0
+  __DATA_CONST.__cfstring: 0x35e0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x3d0
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA_CONST.__objc_intobj: 0x840
+  __DATA_CONST.__objc_intobj: 0x858
   __DATA_CONST.__objc_doubleobj: 0x1a0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0x548
-  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__got: 0x228
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x17d8
   __DATA.__objc_selrefs: 0xb48

   - /usr/lib/libsqlite3.dylib
   Functions: 538
   Symbols:   246
-  CStrings:  1437
+  CStrings:  1438
 
Functions:
~ sub_10000993c : 3648 -> 3672
CStrings:
+ "SetStoreUpdateService"
```
