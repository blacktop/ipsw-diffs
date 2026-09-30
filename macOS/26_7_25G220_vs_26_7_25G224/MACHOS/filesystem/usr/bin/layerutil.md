## layerutil

> `usr/bin/layerutil`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 975.2.0.0.0
-  __TEXT.__text: 0x9886c
+  __TEXT.__text: 0x985f4
   __TEXT.__auth_stubs: 0x21d0
   __TEXT.__objc_stubs: 0xbd60
   __TEXT.__objc_methlist: 0x7c30
-  __TEXT.__const: 0x2b48
+  __TEXT.__const: 0x2b38
   __TEXT.__gcc_except_tab: 0xf7c
   __TEXT.__objc_methname: 0x1208e
   __TEXT.__objc_classname: 0x1163
   __TEXT.__objc_methtype: 0x43e8
-  __TEXT.__cstring: 0xfd37
+  __TEXT.__cstring: 0xfd07
   __TEXT.__dlopen_cstrs: 0x4f
   __TEXT.__oslogstring: 0x28
   __TEXT.__swift5_typeref: 0x84

   __DATA_CONST.__auth_got: 0x1100
   __DATA_CONST.__got: 0x5a8
   __DATA_CONST.__auth_ptr: 0xb0
-  __DATA_CONST.__const: 0x4778
+  __DATA_CONST.__const: 0x4760
   __DATA_CONST.__cfstring: 0x46e0
   __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   Functions: 4188
   Symbols:   735
-  CStrings:  5236
+  CStrings:  5234
 
Functions:
~ sub_10003f8c8 : 1628 -> 1556
~ sub_100040054 -> sub_10004000c : 396 -> 352
~ sub_1000405e0 -> sub_10004056c : 1624 -> 1552
~ sub_100040c38 -> sub_100040b7c : 1624 -> 1552
~ sub_1000412b0 -> sub_1000411ac : 3248 -> 3104
~ sub_100041f60 -> sub_100041dcc : 3320 -> 3176
~ sub_100042c58 -> sub_100042a34 : 1360 -> 1288
~ sub_10004327c -> sub_100043010 : 668 -> 656
CStrings:
- "APPLE11"
- "kCoreThemeFeatureSetMetalGPUFamily11"
```
