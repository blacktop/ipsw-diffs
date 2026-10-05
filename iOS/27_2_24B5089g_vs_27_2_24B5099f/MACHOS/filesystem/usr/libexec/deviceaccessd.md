## deviceaccessd

> `/usr/libexec/deviceaccessd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2701.3.0.0.0
-  __TEXT.__text: 0x92e38
+2701.6.0.0.0
+  __TEXT.__text: 0x93278
   __TEXT.__auth_stubs: 0x2280
-  __TEXT.__objc_stubs: 0x8360
-  __TEXT.__objc_methlist: 0x2808
+  __TEXT.__objc_stubs: 0x83a0
+  __TEXT.__objc_methlist: 0x2810
   __TEXT.__const: 0x1c88
-  __TEXT.__cstring: 0x16094
+  __TEXT.__cstring: 0x16154
   __TEXT.__objc_classname: 0x3f5
   __TEXT.__objc_methtype: 0x1b9a
-  __TEXT.__gcc_except_tab: 0x4300
-  __TEXT.__objc_methname: 0xa864
+  __TEXT.__gcc_except_tab: 0x432c
+  __TEXT.__objc_methname: 0xa8a4
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__swift5_typeref: 0x9ee
   __TEXT.__swift5_fieldmd: 0x490

   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift_as_cont: 0x3c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x2440
+  __TEXT.__unwind_info: 0x2460
   __TEXT.__eh_frame: 0x10a8
-  __DATA_CONST.__const: 0x2998
+  __DATA_CONST.__const: 0x29c0
   __DATA_CONST.__cfstring: 0x2240
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA_CONST.__objc_intobj: 0xa8
+  __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__auth_got: 0x1150
   __DATA_CONST.__got: 0x8d0
   __DATA_CONST.__auth_ptr: 0x2b8
   __DATA.__objc_const: 0x3698
-  __DATA.__objc_selrefs: 0x2858
+  __DATA.__objc_selrefs: 0x2868
   __DATA.__objc_ivar: 0x2f8
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x13e8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2551
+  Functions: 2554
   Symbols:   915
-  CStrings:  4074
+  CStrings:  4079
 
CStrings:
+ "-[DADaemonServer _moveWiFiProfileForDevice:fromBundleID:toBundleID:]"
+ "[WiFi] failed to move profile = '%@' from '%@' to '%@' error = '%@'"
+ "[WiFi] moved profile = '%@' from '%@' to '%@'"
+ "_moveWiFiProfileForDevice:fromBundleID:toBundleID:"
+ "setWithObject:"
```
