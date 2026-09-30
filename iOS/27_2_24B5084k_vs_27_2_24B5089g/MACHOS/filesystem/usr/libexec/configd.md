## configd

> `/usr/libexec/configd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1452.0.0.0.0
-  __TEXT.__text: 0x683b4
-  __TEXT.__auth_stubs: 0x24d0
+1453.0.0.0.0
+  __TEXT.__text: 0x683d4
+  __TEXT.__auth_stubs: 0x24e0
   __TEXT.__objc_stubs: 0x14e0
   __TEXT.__objc_methlist: 0xa64
   __TEXT.__const: 0x238

   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__auth_got: 0x1278
+  __DATA_CONST.__auth_got: 0x1280
   __DATA_CONST.__got: 0x6c8
   __DATA_CONST.__auth_ptr: 0x110
   __DATA.__objc_const: 0xc48

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 962
-  Symbols:   818
+  Symbols:   819
   CStrings:  1673
 
Symbols:
+ _nw_resolver_config_set_interface_name
Functions:
~ sub_100050e18 : 532 -> 564
```
