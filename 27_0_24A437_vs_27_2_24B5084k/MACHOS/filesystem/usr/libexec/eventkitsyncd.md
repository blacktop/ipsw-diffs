## eventkitsyncd

> `/usr/libexec/eventkitsyncd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__oslogstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-431.0.0.0.0
-  __TEXT.__text: 0x747c4
+432.0.0.0.0
+  __TEXT.__text: 0x747e0
   __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_stubs: 0xcc20
+  __TEXT.__objc_stubs: 0xcc40
   __TEXT.__objc_methlist: 0x7510
   __TEXT.__cstring: 0x5b5a
-  __TEXT.__objc_methname: 0xfcc5
+  __TEXT.__objc_methname: 0xfcd6
   __TEXT.__objc_classname: 0x8ae
   __TEXT.__objc_methtype: 0x2576
   __TEXT.__const: 0x278

   __DATA_CONST.__got: 0x4d8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0xefb0
-  __DATA.__objc_selrefs: 0x3f78
+  __DATA.__objc_selrefs: 0x3f80
   __DATA.__objc_ivar: 0x998
   __DATA.__objc_data: 0x1e50
   __DATA.__data: 0x800

   - /usr/lib/libz.1.dylib
   Functions: 2865
   Symbols:   371
-  CStrings:  4641
+  CStrings:  4642
 
Functions:
~ sub_10001d164 : 1212 -> 1240
CStrings:
+ "== Started EventKitSync-432"
+ "emptyMeltedCache"
- "== Started EventKitSync-431"
```
