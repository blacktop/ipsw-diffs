## coreduetd

> `/usr/libexec/coreduetd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1967.0.0.0.0
-  __TEXT.__text: 0x21224
+1971.0.0.0.0
+  __TEXT.__text: 0x21494
   __TEXT.__auth_stubs: 0x9b0
-  __TEXT.__objc_stubs: 0x52a0
-  __TEXT.__objc_methlist: 0x1a18
+  __TEXT.__objc_stubs: 0x52e0
+  __TEXT.__objc_methlist: 0x1a38
   __TEXT.__objc_classname: 0x199
-  __TEXT.__cstring: 0x1c85
-  __TEXT.__objc_methname: 0x65ae
+  __TEXT.__cstring: 0x1c86
+  __TEXT.__objc_methname: 0x6609
   __TEXT.__objc_methtype: 0x1d60
   __TEXT.__const: 0x100
-  __TEXT.__oslogstring: 0x371d
+  __TEXT.__oslogstring: 0x377a
   __TEXT.__gcc_except_tab: 0x490
   __TEXT.__dlopen_cstrs: 0x116
-  __TEXT.__unwind_info: 0x828
+  __TEXT.__unwind_info: 0x830
   __DATA_CONST.__const: 0xf50
   __DATA_CONST.__cfstring: 0x16a0
   __DATA_CONST.__objc_classlist: 0x70

   __DATA_CONST.__auth_got: 0x4e8
   __DATA_CONST.__got: 0x4d8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x2508
-  __DATA.__objc_selrefs: 0x17e0
-  __DATA.__objc_ivar: 0x1a0
+  __DATA.__objc_const: 0x2528
+  __DATA.__objc_selrefs: 0x17f0
+  __DATA.__objc_ivar: 0x1a4
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x300
   __DATA.__bss: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 670
+  Functions: 674
   Symbols:   322
-  CStrings:  1776
+  CStrings:  1780
 
CStrings:
+ "CDDCommunicator: nearby re-poll computed defaultPaired nearby count = %lu (from %lu devices)"
+ "_nearbyRepollTimer"
+ "b"
+ "nearbyPairedDeviceCountForDevices:"
+ "repollNearbyPairedDevices"
+ "startNearbyRepollTimer"
- "R"
- "isConnected"
```
