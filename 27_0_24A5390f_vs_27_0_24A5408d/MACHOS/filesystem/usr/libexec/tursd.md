## tursd

> `/usr/libexec/tursd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1157.0.0.0.0
-  __TEXT.__text: 0x84a4
+1160.0.0.0.0
+  __TEXT.__text: 0x843c
   __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_stubs: 0x1ba0
+  __TEXT.__objc_stubs: 0x1b40
   __TEXT.__objc_methlist: 0x1144
   __TEXT.__const: 0x1b2
   __TEXT.__cstring: 0xa73
   __TEXT.__oslogstring: 0x2c5
-  __TEXT.__objc_methname: 0x3b38
+  __TEXT.__objc_methname: 0x3b0c
   __TEXT.__objc_classname: 0x146
   __TEXT.__objc_methtype: 0x92e
   __TEXT.__swift5_typeref: 0x4a

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x320
+  __TEXT.__unwind_info: 0x318
   __DATA_CONST.__const: 0x710
-  __DATA_CONST.__cfstring: 0x820
+  __DATA_CONST.__cfstring: 0x800
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x2f8
-  __DATA_CONST.__got: 0x260
+  __DATA_CONST.__got: 0x258
   __DATA_CONST.__auth_ptr: 0x58
   __DATA.__objc_const: 0x17c8
-  __DATA.__objc_selrefs: 0xd18
+  __DATA.__objc_selrefs: 0xd00
   __DATA.__objc_ivar: 0x98
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x218

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 318
-  Symbols:   199
-  CStrings:  760
+  Symbols:   198
+  CStrings:  756
 
Symbols:
- _OBJC_CLASS_$_NSLocale
Functions:
~ sub_1000049dc : 124 -> 20
CStrings:
- "currentLocale"
- "en"
- "isEqualToString:"
- "languageCode"
```
