## assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-916.45.110.0.0
-  __TEXT.__text: 0x1b004
+916.51.202.0.0
+  __TEXT.__text: 0x1b1f4
   __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_stubs: 0x53c0
+  __TEXT.__objc_stubs: 0x53a0
   __TEXT.__objc_methlist: 0xfe4
   __TEXT.__dlopen_cstrs: 0x11b
   __TEXT.__const: 0x140
-  __TEXT.__gcc_except_tab: 0x7b0
+  __TEXT.__gcc_except_tab: 0x7bc
   __TEXT.__objc_classname: 0x74e
-  __TEXT.__objc_methname: 0x5fe8
+  __TEXT.__objc_methname: 0x5fd8
   __TEXT.__objc_methtype: 0xa06
-  __TEXT.__oslogstring: 0x473d
+  __TEXT.__oslogstring: 0x476c
   __TEXT.__cstring: 0x1a89
   __TEXT.__unwind_info: 0x708
   __DATA_CONST.__const: 0xfd8

   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_intobj: 0xd8
+  __DATA_CONST.__objc_doubleobj: 0x10
+  __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__auth_got: 0x5f8
-  __DATA_CONST.__got: 0x790
+  __DATA_CONST.__got: 0x7a8
   __DATA.__objc_const: 0x3120
-  __DATA.__objc_selrefs: 0x16d0
+  __DATA.__objc_selrefs: 0x16c8
   __DATA.__objc_ivar: 0xa8
   __DATA.__objc_data: 0xeb0
   __DATA.__data: 0x360

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 402
-  Symbols:   443
-  CStrings:  1402
+  Symbols:   447
+  CStrings:  1401
 
Symbols:
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _PAMediaConversionServiceOptionColorSpaceKey
+ _PAMediaConversionServiceOptionFormatConversionOnlyKey
+ _PAMediaConversionServiceOptionScaleFactorKey
Functions:
~ sub_100002e70 -> sub_100002ec0 : 1540 -> 1600
~ sub_10000879c -> sub_100008828 : 376 -> 436
~ sub_100008914 -> sub_1000089dc : 408 -> 524
~ sub_100008aac -> sub_100008be8 : 1808 -> 1956
~ sub_1000091bc -> sub_10000938c : 196 -> 256
~ sub_100009280 -> sub_10000948c : 284 -> 336
CStrings:
+ "File Provider cache cleanup: unable to determine relationship of %@ to document storage root, leaving in place: %@"
- "File Provider cache cleanup: removed empty domain root directory %@"
- "standardizedURL"
```
