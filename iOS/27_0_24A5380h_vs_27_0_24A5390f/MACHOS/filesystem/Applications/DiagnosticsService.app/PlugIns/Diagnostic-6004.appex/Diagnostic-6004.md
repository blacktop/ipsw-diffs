## Diagnostic-6004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__objc_methname`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1374.0.5.0.0
-  __TEXT.__text: 0x14674
+1374.0.27.0.0
+  __TEXT.__text: 0x14888
   __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_stubs: 0xdc0
+  __TEXT.__objc_stubs: 0xde0
   __TEXT.__objc_methlist: 0x544
   __TEXT.__cstring: 0xa4c
   __TEXT.__objc_classname: 0x31e
-  __TEXT.__const: 0xb88
-  __TEXT.__oslogstring: 0xfe
+  __TEXT.__const: 0xb98
+  __TEXT.__oslogstring: 0x22e
   __TEXT.__objc_methname: 0x1368
   __TEXT.__objc_methtype: 0x50b
   __TEXT.__swift5_typeref: 0x14f2

   __DATA_CONST.__got: 0x2c0
   __DATA_CONST.__auth_ptr: 0x2e0
   __DATA.__objc_const: 0xe10
-  __DATA.__objc_selrefs: 0x500
+  __DATA.__objc_selrefs: 0x508
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x7f8
   __DATA.__data: 0x1120

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 482
   Symbols:   216
-  CStrings:  376
+  CStrings:  385
 
Functions:
~ sub_100001c18 : 280 -> 400
~ sub_100002198 -> sub_100002210 : 756 -> 848
~ sub_10000248c -> sub_100002560 : 156 -> 228
~ sub_100002530 -> sub_10000264c : 472 -> 592
~ sub_100002708 -> sub_10000289c : 180 -> 308
CStrings:
+ "Device does not have Exclaves. Skipping stat capture."
+ "Display pipe stats captured"
+ "Exclaves is not supported, skipping status."
+ "Exclaves is supported."
+ "Platform has display pipe stats, preparing to capture"
+ "Retrieving display pipe stats..."
+ "Returning %lu stats for display pipe client"
+ "Starting display pipe stat capture"
+ "count"
```
