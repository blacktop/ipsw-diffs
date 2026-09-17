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
- `__DATA_CONST.__objc_catlist`
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

-1056.0.22.0.0
-  __TEXT.__text: 0x4f664
+1056.40.5.0.0
+  __TEXT.__text: 0x4fa0c
   __TEXT.__auth_stubs: 0x22e0
-  __TEXT.__objc_stubs: 0x43a0
-  __TEXT.__objc_methlist: 0x10d0
-  __TEXT.__cstring: 0x5bab
+  __TEXT.__objc_stubs: 0x43e0
+  __TEXT.__objc_methlist: 0x10e8
+  __TEXT.__cstring: 0x5bdb
   __TEXT.__const: 0x10f8
-  __TEXT.__objc_methname: 0x4bed
+  __TEXT.__objc_methname: 0x4c2d
   __TEXT.__oslogstring: 0x2e71
   __TEXT.__objc_classname: 0x2b4
   __TEXT.__objc_methtype: 0xa9e

   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0xfc0
+  __TEXT.__unwind_info: 0xfc8
   __TEXT.__eh_frame: 0x638
   __DATA_CONST.__const: 0x1a88
-  __DATA_CONST.__cfstring: 0x7c80
+  __DATA_CONST.__cfstring: 0x7cc0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_intobj: 0x570
+  __DATA_CONST.__objc_intobj: 0x588
   __DATA_CONST.__objc_arraydata: 0x3e8
   __DATA_CONST.__objc_dictobj: 0x280
   __DATA_CONST.__objc_arrayobj: 0x240

   __DATA_CONST.__got: 0x610
   __DATA_CONST.__auth_ptr: 0x338
   __DATA.__objc_const: 0x2980
-  __DATA.__objc_selrefs: 0x12c0
+  __DATA.__objc_selrefs: 0x12d0
   __DATA.__objc_ivar: 0x2c4
   __DATA.__objc_data: 0x968
   __DATA.__data: 0x9f0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1130
+  Functions: 1133
   Symbols:   848
-  CStrings:  2349
+  CStrings:  2354
 
CStrings:
+ "0x"
+ "ARKIT"
+ "Timed out while attempting to transition. Error: "
+ "_markImagesUsedForApplicationSpecificBacktracesUsingCatalog:"
+ "isUserFault"
```
