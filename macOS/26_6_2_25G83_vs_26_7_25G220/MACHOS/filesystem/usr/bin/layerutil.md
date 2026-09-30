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

-975.0.0.0.0
-  __TEXT.__text: 0x985b4
+975.2.0.0.0
+  __TEXT.__text: 0x9886c
   __TEXT.__auth_stubs: 0x21d0
   __TEXT.__objc_stubs: 0xbd60
   __TEXT.__objc_methlist: 0x7c30
-  __TEXT.__const: 0x2b38
+  __TEXT.__const: 0x2b48
   __TEXT.__gcc_except_tab: 0xf7c
   __TEXT.__objc_methname: 0x1208e
   __TEXT.__objc_classname: 0x1163
   __TEXT.__objc_methtype: 0x43e8
-  __TEXT.__cstring: 0xfc97
+  __TEXT.__cstring: 0xfd37
   __TEXT.__dlopen_cstrs: 0x4f
   __TEXT.__oslogstring: 0x28
   __TEXT.__swift5_typeref: 0x84

   __DATA_CONST.__auth_got: 0x1100
   __DATA_CONST.__got: 0x5a8
   __DATA_CONST.__auth_ptr: 0xb0
-  __DATA_CONST.__const: 0x4760
+  __DATA_CONST.__const: 0x4778
   __DATA_CONST.__cfstring: 0x46e0
   __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   Functions: 4188
   Symbols:   735
-  CStrings:  5233
+  CStrings:  5236
 
Functions:
~ sub_10001ae54 : 788 -> 848
~ sub_10003f88c -> sub_10003f8c8 : 1556 -> 1628
~ sub_10003ffd0 -> sub_100040054 : 352 -> 396
~ sub_100040530 -> sub_1000405e0 : 1552 -> 1624
~ sub_100040b40 -> sub_100040c38 : 1552 -> 1624
~ sub_100041170 -> sub_1000412b0 : 3104 -> 3248
~ sub_100041d90 -> sub_100041f60 : 3176 -> 3320
~ sub_1000429f8 -> sub_100042c58 : 1288 -> 1360
~ sub_100042fd4 -> sub_10004327c : 656 -> 668
~ sub_100062bdc -> sub_100062e90 : 280 -> 284
CStrings:
+ "APPLE11"
+ "CoreUI: Truncated '%s' compressed image block data name:'%s' pixelFormat:%d (rows %d rowbytes %zu, %zu bytes short)"
+ "kCoreThemeFeatureSetMetalGPUFamily11"
```
