## secd

> `usr/libexec/secd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__data`
- `__DATA.__thread_vars`

```diff

-61901.160.44.701.4
-  __TEXT.__text: 0x2a31f8
+61901.160.44.702.5
+  __TEXT.__text: 0x2a3530
   __TEXT.__auth_stubs: 0x40b0
-  __TEXT.__objc_stubs: 0x1d120
-  __TEXT.__objc_methlist: 0x159c8
+  __TEXT.__objc_stubs: 0x1d1e0
+  __TEXT.__objc_methlist: 0x15a00
   __TEXT.__const: 0x92c
-  __TEXT.__objc_classname: 0x2584
-  __TEXT.__objc_methname: 0x2d464
-  __TEXT.__objc_methtype: 0xa9cf
+  __TEXT.__objc_classname: 0x2595
+  __TEXT.__objc_methname: 0x2d514
+  __TEXT.__objc_methtype: 0xa9ff
   __TEXT.__constg_swiftt: 0x274
   __TEXT.__swift5_typeref: 0x364
   __TEXT.__swift5_reflstr: 0xc7

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x20
-  __TEXT.__cstring: 0x209c8
+  __TEXT.__cstring: 0x209d3
   __TEXT.__oslogstring: 0x2ed46
   __TEXT.__swift5_capture: 0x1bc
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__gcc_except_tab: 0xb868
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__unwind_info: 0x6e80
+  __TEXT.__unwind_info: 0x6e90
   __TEXT.__eh_frame: 0xa58
   __DATA_CONST.__auth_got: 0x2068
-  __DATA_CONST.__got: 0x12f8
+  __DATA_CONST.__got: 0x1300
   __DATA_CONST.__auth_ptr: 0x1d8
   __DATA_CONST.__const: 0x15798
-  __DATA_CONST.__cfstring: 0x1b380
-  __DATA_CONST.__objc_classlist: 0x8f8
+  __DATA_CONST.__cfstring: 0x1b3c0
+  __DATA_CONST.__objc_classlist: 0x900
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x408
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA.__objc_const: 0x234c0
-  __DATA.__objc_selrefs: 0x95f0
+  __DATA.__objc_const: 0x23550
+  __DATA.__objc_selrefs: 0x9630
   __DATA.__objc_ivar: 0x1a78
-  __DATA.__objc_data: 0x5ca8
+  __DATA.__objc_data: 0x5cf8
   __DATA.__data: 0x3040
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x30

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9940
-  Symbols:   1835
-  CStrings:  16026
+  Functions: 9944
+  Symbols:   1836
+  CStrings:  16040
 
Symbols:
+ _OBJC_CLASS_$_NSURLComponents
CStrings:
+ "@40@0:8r*16Q24^@32"
+ "B32@0:8@16Q24"
+ "SecXPCNetworkURL"
+ "allowedURLFromCString:options:error:"
+ "componentsWithString:"
+ "host"
+ "http"
+ "https"
+ "isAllowedURL:options:"
+ "lowercaseString"
+ "scheme"
+ "scheme:isAllowedByOptions:"
+ "setError:code:"
+ "v32@0:8^@16q24"
```
