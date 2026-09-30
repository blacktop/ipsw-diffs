## deviceaccessd

> `/usr/libexec/deviceaccessd`

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
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2700.30.0.0.0
-  __TEXT.__text: 0x91ba4
+2700.34.0.0.0
+  __TEXT.__text: 0x91f34
   __TEXT.__auth_stubs: 0x2280
-  __TEXT.__objc_stubs: 0x7ee0
-  __TEXT.__objc_methlist: 0x2728
+  __TEXT.__objc_stubs: 0x7f40
+  __TEXT.__objc_methlist: 0x2740
   __TEXT.__const: 0x1c88
-  __TEXT.__cstring: 0x152c4
+  __TEXT.__cstring: 0x15394
   __TEXT.__objc_classname: 0x3e5
   __TEXT.__gcc_except_tab: 0x40c0
-  __TEXT.__objc_methname: 0xa3b4
+  __TEXT.__objc_methname: 0xa3e4
   __TEXT.__objc_methtype: 0x1b2a
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__swift5_typeref: 0x9ee

   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift_as_cont: 0x3c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1aa0
+  __TEXT.__unwind_info: 0x1ab0
   __TEXT.__eh_frame: 0x10a0
   __DATA_CONST.__const: 0x2920
-  __DATA_CONST.__cfstring: 0x21e0
+  __DATA_CONST.__cfstring: 0x2200
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x48
-  __DATA_CONST.__objc_arraydata: 0x78
+  __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__auth_got: 0x1150
   __DATA_CONST.__got: 0x8c8
   __DATA_CONST.__auth_ptr: 0x2b8
   __DATA.__objc_const: 0x3668
-  __DATA.__objc_selrefs: 0x2738
+  __DATA.__objc_selrefs: 0x2750
   __DATA.__objc_ivar: 0x2f4
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x1378

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2515
+  Functions: 2520
   Symbols:   914
-  CStrings:  3966
+  CStrings:  3973
 
CStrings:
+ "### _updateDeviceStateForBluetooth prox pairing device with APP Required flow"
+ "### centralManagerDidUpdateState powerState: %ld"
+ "Marking device state Activating for app-required mode: %@"
+ "_createCBCentralManager"
+ "_deviceConfirmsAuthorization:"
+ "com.apple.media-device-extension"
+ "requiresCompanionApp"
```
