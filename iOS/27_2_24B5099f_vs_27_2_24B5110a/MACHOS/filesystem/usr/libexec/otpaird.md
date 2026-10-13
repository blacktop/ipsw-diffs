## otpaird

> `usr/libexec/otpaird`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-62460.40.74.0.0
-  __TEXT.__text: 0x3b64
+62460.40.78.0.0
+  __TEXT.__text: 0x3b78
   __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_stubs: 0xfc0
-  __TEXT.__objc_methlist: 0x88c
+  __TEXT.__objc_stubs: 0xfe0
+  __TEXT.__objc_methlist: 0x8a8
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x8c
-  __TEXT.__objc_methname: 0x176d
+  __TEXT.__objc_methname: 0x177d
   __TEXT.__cstring: 0x2e7
   __TEXT.__oslogstring: 0x2b2
   __TEXT.__objc_classname: 0xbb

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0x120
-  __DATA.__objc_const: 0xb40
-  __DATA.__objc_selrefs: 0x628
+  __DATA.__objc_const: 0xb48
+  __DATA.__objc_selrefs: 0x630
   __DATA.__objc_ivar: 0x64
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x120

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 121
+  Functions: 122
   Symbols:   139
-  CStrings:  410
+  CStrings:  411
 
Functions:
~ sub_100003b98 : 76 -> 8
+ sub_100003ba0
CStrings:
+ "isHomeAccessory"
```
