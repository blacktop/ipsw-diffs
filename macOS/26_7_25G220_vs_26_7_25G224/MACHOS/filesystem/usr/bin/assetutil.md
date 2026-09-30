## assetutil

> `usr/bin/assetutil`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 975.2.0.0.0
-  __TEXT.__text: 0xe2054
+  __TEXT.__text: 0xe1dd4
   __TEXT.__auth_stubs: 0x24b0
   __TEXT.__objc_stubs: 0xb9a0
   __TEXT.__objc_methlist: 0x7100
-  __TEXT.__const: 0x77e98
+  __TEXT.__const: 0x77e88
   __TEXT.__gcc_except_tab: 0x844
   __TEXT.__objc_methname: 0x1127d
   __TEXT.__objc_classname: 0x1035
   __TEXT.__objc_methtype: 0x41c8
-  __TEXT.__cstring: 0x14e70
+  __TEXT.__cstring: 0x14e40
   __TEXT.__dlopen_cstrs: 0x4f
   __TEXT.__oslogstring: 0x28
   __TEXT.__swift5_typeref: 0x84

   __DATA_CONST.__auth_got: 0x1270
   __DATA_CONST.__got: 0x568
   __DATA_CONST.__auth_ptr: 0x100
-  __DATA_CONST.__const: 0x5230
+  __DATA_CONST.__const: 0x5218
   __DATA_CONST.__cfstring: 0x7ec0
   __DATA_CONST.__objc_classlist: 0x3a8
   __DATA_CONST.__objc_catlist: 0x20

   - /usr/lib/swift/libswift_Builtin_float.dylib
   Functions: 3916
   Symbols:   777
-  CStrings:  5771
+  CStrings:  5769
 
Functions:
~ sub_1000532c0 : 1628 -> 1556
~ sub_100053a4c -> sub_100053a04 : 396 -> 352
~ sub_100053fd8 -> sub_100053f64 : 1624 -> 1552
~ sub_100054630 -> sub_100054574 : 1624 -> 1552
~ sub_100054ca8 -> sub_100054ba4 : 3248 -> 3104
~ sub_100055958 -> sub_1000557c4 : 3320 -> 3176
~ sub_100056650 -> sub_10005642c : 1360 -> 1288
~ sub_100056c74 -> sub_100056a08 : 668 -> 656
~ sub_100079128 -> sub_100078eb0 : 88 -> 80
CStrings:
- "APPLE11"
- "kCoreThemeFeatureSetMetalGPUFamily11"
```
