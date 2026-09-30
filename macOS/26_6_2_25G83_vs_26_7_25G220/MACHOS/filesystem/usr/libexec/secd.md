## secd

> `usr/libexec/secd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-61901.160.44.0.0
-  __TEXT.__text: 0x2a33cc
+61901.160.44.701.3
+  __TEXT.__text: 0x2a33e0
   __TEXT.__auth_stubs: 0x40b0
-  __TEXT.__objc_stubs: 0x1d140
-  __TEXT.__objc_methlist: 0x159d0
+  __TEXT.__objc_stubs: 0x1d160
+  __TEXT.__objc_methlist: 0x159e8
   __TEXT.__const: 0x92c
   __TEXT.__objc_classname: 0x2584
-  __TEXT.__objc_methname: 0x2d474
+  __TEXT.__objc_methname: 0x2d484
   __TEXT.__objc_methtype: 0xa9cf
   __TEXT.__constg_swiftt: 0x274
   __TEXT.__swift5_typeref: 0x364

   __DATA_CONST.__objc_arraydata: 0x408
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA.__objc_const: 0x234c0
-  __DATA.__objc_selrefs: 0x95f8
+  __DATA.__objc_const: 0x234c8
+  __DATA.__objc_selrefs: 0x9600
   __DATA.__objc_ivar: 0x1a78
   __DATA.__objc_data: 0x5ca8
   __DATA.__data: 0x3040

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9941
+  Functions: 9942
   Symbols:   1835
-  CStrings:  16027
+  CStrings:  16028
 
Functions:
~ sub_100107fe0 : 88 -> 100
+ sub_10010805c
CStrings:
+ "isHomeAccessory"
```
