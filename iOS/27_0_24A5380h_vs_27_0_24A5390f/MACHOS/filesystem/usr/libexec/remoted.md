## remoted

> `/usr/libexec/remoted`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-245.0.4.0.0
-  __TEXT.__text: 0x3d534
+245.0.6.0.0
+  __TEXT.__text: 0x3d5f4
   __TEXT.__auth_stubs: 0x1860
   __TEXT.__objc_stubs: 0x24a0
   __TEXT.__objc_methlist: 0x1560
   __TEXT.__const: 0x22a
-  __TEXT.__oslogstring: 0x84b3
+  __TEXT.__oslogstring: 0x8502
   __TEXT.__cstring: 0x21d9
   __TEXT.__objc_methname: 0x254c
   __TEXT.__objc_classname: 0x2c9
   __TEXT.__objc_methtype: 0x79b
   __TEXT.__gcc_except_tab: 0x1120
-  __TEXT.__unwind_info: 0xdc8
+  __TEXT.__unwind_info: 0xdd0
   __DATA_CONST.__const: 0x12c8
   __DATA_CONST.__cfstring: 0xea0
   __DATA_CONST.__objc_classlist: 0xd8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1375
+  Functions: 1376
   Symbols:   492
-  CStrings:  1775
+  CStrings:  1776
 
CStrings:
+ "get_local_device_description denied: missing entitlement (client=\"%{public}s\")"
```
