## Diagnostic-8389

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__objc_methname`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-1374.0.5.0.0
-  __TEXT.__text: 0x1dc9c
-  __TEXT.__auth_stubs: 0xf70
-  __TEXT.__objc_stubs: 0xb00
+1374.0.27.0.0
+  __TEXT.__text: 0x1deb0
+  __TEXT.__auth_stubs: 0xf80
+  __TEXT.__objc_stubs: 0xb20
   __TEXT.__objc_methlist: 0x5d4
-  __TEXT.__const: 0x36d0
+  __TEXT.__const: 0x36e0
   __TEXT.__cstring: 0x11bd
-  __TEXT.__oslogstring: 0x54
+  __TEXT.__oslogstring: 0x18f
   __TEXT.__objc_classname: 0x1f4
   __TEXT.__objc_methname: 0x15fd
   __TEXT.__objc_methtype: 0x86b

   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x7c0
+  __DATA_CONST.__auth_got: 0x7c8
   __DATA_CONST.__got: 0x230
   __DATA_CONST.__auth_ptr: 0x198
   __DATA.__objc_const: 0xbf0
-  __DATA.__objc_selrefs: 0x4e8
+  __DATA.__objc_selrefs: 0x4f0
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x7e8
   __DATA.__data: 0x11f0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 857
-  Symbols:   196
-  CStrings:  438
+  Symbols:   197
+  CStrings:  447
 
Symbols:
+ __os_log_impl
Functions:
~ sub_100001920 : 280 -> 400
~ sub_100001ea0 -> sub_100001f18 : 756 -> 848
~ sub_100002194 -> sub_100002268 : 156 -> 228
~ sub_100002238 -> sub_100002354 : 472 -> 592
~ sub_100002410 -> sub_1000025a4 : 180 -> 308
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
