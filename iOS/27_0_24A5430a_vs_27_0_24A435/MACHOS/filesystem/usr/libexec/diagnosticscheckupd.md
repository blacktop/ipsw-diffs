## diagnosticscheckupd

> `/usr/libexec/diagnosticscheckupd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1374.2.2.0.0
-  __TEXT.__text: 0x4b2d8
+  __TEXT.__text: 0x4b448
   __TEXT.__auth_stubs: 0x15e0
   __TEXT.__objc_stubs: 0x5b80
   __TEXT.__objc_methlist: 0x380c
-  __TEXT.__cstring: 0x2ecd
+  __TEXT.__cstring: 0x2edd
   __TEXT.__objc_methname: 0x82a1
   __TEXT.__objc_classname: 0xbef
   __TEXT.__objc_methtype: 0x26bb
   __TEXT.__const: 0x2088
   __TEXT.__gcc_except_tab: 0xb84
-  __TEXT.__oslogstring: 0x374a
+  __TEXT.__oslogstring: 0x380a
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x1610
   __TEXT.__swift5_typeref: 0xc0e

   __TEXT.__unwind_info: 0x1378
   __TEXT.__eh_frame: 0x7e8
   __DATA_CONST.__const: 0x3018
-  __DATA_CONST.__cfstring: 0x1680
+  __DATA_CONST.__cfstring: 0x16e0
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x100
-  __DATA_CONST.__objc_intobj: 0xa38
-  __DATA_CONST.__objc_arraydata: 0x2c0
+  __DATA_CONST.__objc_intobj: 0xac8
+  __DATA_CONST.__objc_arraydata: 0x2f0
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_floatobj: 0x20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1862
+  Functions: 1864
   Symbols:   639
-  CStrings:  2390
+  CStrings:  2396
 
CStrings:
+ "BPCC"
+ "Failed to write btp0 for shelf life mode. Aborting shutdown."
+ "Failed to write btp1 for shelf life mode. Aborting shutdown."
+ "Multipack system detected. Using btp0/btp1 for shelf life mode."
+ "btp0"
+ "btp1"
```
