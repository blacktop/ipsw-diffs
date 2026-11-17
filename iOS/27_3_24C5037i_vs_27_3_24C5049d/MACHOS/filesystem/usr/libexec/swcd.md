## swcd

> `/usr/libexec/swcd`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1040.1.0.0.0
-  __TEXT.__text: 0x1d210
+1040.2.0.0.0
+  __TEXT.__text: 0x1d580
   __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_stubs: 0x3320
-  __TEXT.__objc_methlist: 0x1044
-  __TEXT.__gcc_except_tab: 0x3c10
-  __TEXT.__cstring: 0x1c1f
+  __TEXT.__objc_stubs: 0x3360
+  __TEXT.__objc_methlist: 0x106c
+  __TEXT.__gcc_except_tab: 0x3c88
+  __TEXT.__cstring: 0x1c3d
   __TEXT.__const: 0xe0
-  __TEXT.__objc_methname: 0x3cda
+  __TEXT.__objc_methname: 0x3d99
   __TEXT.__oslogstring: 0x1994
   __TEXT.__objc_classname: 0x1b4
-  __TEXT.__objc_methtype: 0x11e7
-  __TEXT.__unwind_info: 0xc08
-  __DATA_CONST.__const: 0xae0
+  __TEXT.__objc_methtype: 0x11f6
+  __TEXT.__unwind_info: 0xc48
+  __DATA_CONST.__const: 0xb30
   __DATA_CONST.__cfstring: 0x13e0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__auth_got: 0x510
   __DATA_CONST.__got: 0x278
   __DATA.__objc_const: 0x1528
-  __DATA.__objc_selrefs: 0xf10
+  __DATA.__objc_selrefs: 0xf28
   __DATA.__objc_ivar: 0xdc
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x3c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 374
+  Functions: 381
   Symbols:   249
-  CStrings:  1111
+  CStrings:  1116
 
CStrings:
+ "@32@0:8@16@?24"
+ "_entriesForApplicationIdentifier:fromJSONEnumeration:"
+ "_entriesFromAdditionalServiceDetailsForApplicationIdentifier:"
+ "_enumerateAdditionalServiceDetailsJSONFilesForApplicationIdentifier:block:"
+ "v16@?0@?<v@?@\"_SWCDomain\"@C>8"
```
