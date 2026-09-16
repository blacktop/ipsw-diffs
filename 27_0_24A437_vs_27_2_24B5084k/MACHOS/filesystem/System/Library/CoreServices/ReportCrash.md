## ReportCrash

> `/System/Library/CoreServices/ReportCrash`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1056.2.1.0.0
-  __TEXT.__text: 0x4cd64
+1056.40.5.0.0
+  __TEXT.__text: 0x4cf44
   __TEXT.__auth_stubs: 0x2530
-  __TEXT.__objc_stubs: 0x4040
-  __TEXT.__objc_methlist: 0xfc0
-  __TEXT.__cstring: 0x5c0b
+  __TEXT.__objc_stubs: 0x4060
+  __TEXT.__objc_methlist: 0xfd0
+  __TEXT.__cstring: 0x5c4b
   __TEXT.__const: 0x1100
-  __TEXT.__objc_methname: 0x4760
+  __TEXT.__objc_methname: 0x4770
   __TEXT.__oslogstring: 0x2d31
   __TEXT.__objc_classname: 0x2b4
   __TEXT.__objc_methtype: 0xb7e

   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0xf90
+  __TEXT.__unwind_info: 0xf98
   __TEXT.__eh_frame: 0x638
   __DATA_CONST.__const: 0x1950
-  __DATA_CONST.__cfstring: 0x7de0
+  __DATA_CONST.__cfstring: 0x7e20
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x570
+  __DATA_CONST.__objc_intobj: 0x588
   __DATA_CONST.__objc_arraydata: 0x3a8
   __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_arrayobj: 0x228

   __DATA_CONST.__got: 0x580
   __DATA_CONST.__auth_ptr: 0x338
   __DATA.__objc_const: 0x2680
-  __DATA.__objc_selrefs: 0x1168
+  __DATA.__objc_selrefs: 0x1170
   __DATA.__objc_ivar: 0x288
   __DATA.__objc_data: 0x918
   __DATA.__data: 0x9f8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1079
+  Functions: 1081
   Symbols:   869
-  CStrings:  2288
+  CStrings:  2291
 
CStrings:
+ "ARKIT"
+ "Timed out while attempting to transition. Error: "
+ "isUserFault"
```
